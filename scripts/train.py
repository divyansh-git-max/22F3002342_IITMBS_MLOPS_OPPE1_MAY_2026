"""
Stock Movement Predictor — 2 iterations, Feast features, MLflow HPT
"""
import warnings; warnings.filterwarnings("ignore")
import sys
import joblib
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from feast import FeatureStore
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                              recall_score, f1_score, classification_report)
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR     = PROJECT_ROOT / "data"
MODEL_DIR    = PROJECT_ROOT / "models"
OUTPUT_DIR   = PROJECT_ROOT / "outputs"
FEAST_REPO   = PROJECT_ROOT / "feast_repo"
FEATURES_PATH = PROJECT_ROOT / "data" / "features" / "stock_features.parquet"

MLFLOW_URI  = "http://127.0.0.1:8100"
EXPERIMENT  = "stock-movement-oppe"
MODEL_NAME  = "stock-movement-predictor"
FEATURE_COLS = ["rolling_avg_10", "volume_sum_10"]

N_ESTIMATORS = [50, 100, 200]
MAX_DEPTHS   = [3, 5, 10]

mlflow.set_tracking_uri(MLFLOW_URI)
mlflow.set_experiment(EXPERIMENT)


# ── DATA LOADING ──────────────────────────────────────────────────────────────
def load_stock_data(folders: list) -> pd.DataFrame:
    dfs = []
    for folder in folders:
        for csv_file in Path(folder).glob("*.csv"):
            stock_name = csv_file.stem.split("__")[0]
            df = pd.read_csv(csv_file, parse_dates=["timestamp"])
            df["stock_name"] = stock_name
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


def create_target(df: pd.DataFrame) -> pd.DataFrame:
    """target=1 if close[t+5] > close[t]. Sort per stock, drop NaN."""
    result = []
    for _, group in df.groupby("stock_name"):
        g = group.sort_values("timestamp").copy()
        g["target"] = (g["close"].shift(-5) > g["close"]).astype(float)
        result.append(g)
    df = pd.concat(result, ignore_index=True)
    return df.dropna(subset=["target"])


def get_feast_features(df: pd.DataFrame) -> pd.DataFrame:
    """Load the prepared feature table that Feast materializes for training."""
    if not FEATURES_PATH.exists():
        raise SystemExit(
            f"Missing feature parquet at {FEATURES_PATH}. Run scripts/prepare_features.py first."
        )

    feat_df = pd.read_parquet(FEATURES_PATH)
    feat_df["event_timestamp"] = pd.to_datetime(feat_df["event_timestamp"], utc=True)
    entity_df = df[["stock_name", "timestamp"]].copy()
    entity_df["timestamp"] = pd.to_datetime(entity_df["timestamp"], utc=True)
    entity_df = entity_df.rename(columns={"timestamp": "event_timestamp"})

    return entity_df.merge(
        feat_df,
        on=["stock_name", "event_timestamp"],
        how="left",
        validate="one_to_one",
    )


def chronological_split(df: pd.DataFrame, test_size=0.2):
    df = df.sort_values("timestamp").reset_index(drop=True)
    split = int(len(df) * (1 - test_size))
    return df.iloc[:split], df.iloc[split:]


# ── TRAINING LOOP ─────────────────────────────────────────────────────────────
best_model    = None
best_accuracy = 0.0
best_run_id   = None

iterations = [
    {"name": "iter1_v0",    "folders": [DATA_DIR / "v0"],
     "feast_version": "v0"},
    {"name": "iter2_v0_v1", "folders": [DATA_DIR / "v0", DATA_DIR / "v1"],
     "feast_version": "v1"},
]

for iteration in iterations:
    print(f"\n{'='*50}\n{iteration['name']}")

    # Prepare features for this iteration
    import subprocess
    subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / "prepare_features.py"),
         iteration["feast_version"]],
        check=True
    )

    raw_df  = load_stock_data(iteration["folders"])
    raw_df  = create_target(raw_df)

    # Get features via Feast (point-in-time correct)
    feat_df = get_feast_features(raw_df)
    feat_df = feat_df.dropna(subset=FEATURE_COLS)

    # Join target back
    raw_df["timestamp_utc"] = pd.to_datetime(raw_df["timestamp"], utc=True)
    merged = feat_df.merge(
        raw_df[["stock_name", "timestamp_utc", "target"]],
        left_on=["stock_name", "event_timestamp"],
        right_on=["stock_name", "timestamp_utc"],
        how="left"
    ).dropna(subset=["target"])

    merged["timestamp"] = merged["event_timestamp"].dt.tz_localize(None)
    train_df, test_df = chronological_split(merged)

    X_train = train_df[FEATURE_COLS]
    y_train = train_df["target"].astype(int)
    X_test  = test_df[FEATURE_COLS]
    y_test  = test_df["target"].astype(int)

    print(f"Train={len(X_train)} | Test={len(X_test)}")

    for n_est in N_ESTIMATORS:
        for depth in MAX_DEPTHS:
            run_name = f"{iteration['name']}_nest{n_est}_depth{depth}"
            with mlflow.start_run(run_name=run_name):
                model = RandomForestClassifier(
                    n_estimators=n_est, max_depth=depth,
                    random_state=42, n_jobs=-1
                )
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                acc  = accuracy_score(y_test, y_pred)
                prec = precision_score(y_test, y_pred, average="weighted", zero_division=0)
                rec  = recall_score(y_test, y_pred, average="weighted", zero_division=0)
                f1   = f1_score(y_test, y_pred, average="weighted", zero_division=0)

                mlflow.log_params({"n_estimators": n_est, "max_depth": depth,
                                   "data_version": iteration["name"], "random_state": 42})
                mlflow.log_metrics({"accuracy": acc, "precision": prec,
                                    "recall": rec, "f1": f1})

                OUTPUT_DIR.mkdir(exist_ok=True)
                rp = OUTPUT_DIR / f"{run_name}_report.txt"
                rp.write_text(classification_report(y_test, y_pred))
                mlflow.log_artifact(str(rp))
                mlflow.sklearn.log_model(model, "model",
                                          registered_model_name=MODEL_NAME)

                print(f"  {run_name} | acc={acc:.4f} | f1={f1:.4f}")

                if acc > best_accuracy:
                    best_accuracy = acc
                    best_model    = model
                    best_run_id   = mlflow.active_run().info.run_id

# ── SAVE & REGISTER CHAMPION ──────────────────────────────────────────────────
MODEL_DIR.mkdir(exist_ok=True)
joblib.dump(best_model, MODEL_DIR / "model.pkl")

# Set champion alias
client = mlflow.tracking.MlflowClient()
mv = client.search_model_versions(f"name='{MODEL_NAME}'")
best_version = [v for v in mv if v.run_id == best_run_id][0]
client.set_registered_model_alias(MODEL_NAME, "champion", best_version.version)

print(f"\nBest: acc={best_accuracy:.4f} | run={best_run_id}")
print(f"Champion version: {best_version.version}")