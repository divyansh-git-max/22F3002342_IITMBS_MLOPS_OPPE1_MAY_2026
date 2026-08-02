"""CI evaluation: fetch champion from MLflow, run on test data."""
import os
import mlflow
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from pathlib import Path

PROJECT_ROOT  = Path(__file__).resolve().parent.parent
MLFLOW_URI    = os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:8100")
MODEL_NAME    = "stock-movement-predictor"
FEATURE_COLS  = ["rolling_avg_10", "volume_sum_10"]
USE_MLFLOW    = os.getenv("CI_EVAL_USE_MLFLOW", "true").lower() == "true"
MAX_ROWS_PER_STOCK = int(os.getenv("CI_EVAL_MAX_ROWS_PER_STOCK", "0"))

mlflow.set_tracking_uri(MLFLOW_URI)

fallback_path = PROJECT_ROOT / "models" / "model.pkl"

# Load champion from MLflow registry (optional in CI fast mode)
if USE_MLFLOW:
    try:
        model = mlflow.sklearn.load_model(f"models:/{MODEL_NAME}@champion")
        print("Loaded champion from MLflow registry")
    except Exception as e:
        print(f"MLflow load failed: {e} — falling back to model.pkl")
        if not fallback_path.exists():
            raise SystemExit("No champion model in MLflow and models/model.pkl was not found.")
        model = joblib.load(fallback_path)
else:
    if not fallback_path.exists():
        raise SystemExit("CI_EVAL_USE_MLFLOW=false but models/model.pkl was not found.")
    model = joblib.load(fallback_path)
    print("Loaded model from models/model.pkl (MLflow skipped by CI_EVAL_USE_MLFLOW=false)")

# Load test data (v0, DVC pulled)
dfs = []
for f in (PROJECT_ROOT / "data" / "v0").glob("*.csv"):
    df = pd.read_csv(f, parse_dates=["timestamp"])
    df["stock_name"] = f.stem.split("__")[0]
    dfs.append(df)

if not dfs:
    raise SystemExit("No CSV files found under data/v0. Ensure dvc pull completed.")

df = pd.concat(dfs, ignore_index=True).sort_values(["stock_name", "timestamp"])

if MAX_ROWS_PER_STOCK > 0:
    df = (
        df.groupby("stock_name", group_keys=False)
        .tail(MAX_ROWS_PER_STOCK)
        .reset_index(drop=True)
    )
    print(f"Fast eval enabled: using last {MAX_ROWS_PER_STOCK} rows per stock")

# Compute features
result = []
for _, g in df.groupby("stock_name"):
    g = g.copy()
    g["rolling_avg_10"] = g["close"].rolling(10, min_periods=1).mean()
    g["volume_sum_10"]  = g["volume"].rolling(10, min_periods=1).sum()
    g["target"] = (g["close"].shift(-5) > g["close"]).astype(float)
    result.append(g)

df = pd.concat(result).dropna(subset=["target"])
split = int(len(df) * 0.8)
test_df = df.iloc[split:]

X_test = test_df[FEATURE_COLS]
y_test = test_df["target"].astype(int)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1  = f1_score(y_test, y_pred, average="weighted", zero_division=0)

print(f"Test Accuracy: {acc:.4f}")
print(f"Test F1:       {f1:.4f}")

# Save metrics for CML report
Path("metrics.txt").write_text(f"accuracy: {acc:.4f}\nf1: {f1:.4f}\n")