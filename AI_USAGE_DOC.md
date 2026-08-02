# AI Usage Documentation
**Student Roll Number:** 22f3002342  
**Exam:** OPPE-1 Mock | MAY 2026  
**Repo:** 22f3002342_IITMBS_MLOPS_OPPE1_MAY_2026_MOCK

---

## AI Tools Utilized

| # | Tool Name | Purpose | Shared Chat Link |
|---|-----------|---------|-----------------|
| 1 | Antigravity (Google Gemini) | Code generation, debugging, boilerplate for DVC/MLflow/CI | [paste link] |

> Tool didn't supported the link so here is chat below

---

## Prompts and Responses Used

### Tool: Antigravity (Google Gemini and claude sonnet 4.6)

---

**Prompt 1**  
```
Now Here is the instruction for the dataset, so i will be telling the oppe instructions and all but first of all i will tell you that i have initialize mlflow server , created git hub repo , gave the access to instructor and vm in also setup, all the dependencies have been installed in both project repo and ssh, then the ssh tunnel is also started with gcs remote initialized with dvc and congiguration is done. now the actual instruction for dataset and then i will tell the instruction for assignment:

INSTRUCTION FOR DATASET:
for the first iteration of the model (v0), use data in StockAnalyticaData/v0 data folder comprising of these stocks:

AARTIIND
ABCAPITAL
For the second iteration of the model (v1), add StockAnalyticaData/v1 data to StockAnalyticaData/v0 - the data from v1 data folder comprising of these stocks:

ABFRL

ADANIENT

ADANIGAS

and the sample for dataset containing all the features and note there are first 5 sample for each dataset:
1.  data/v0 : AARTIIND__EQ__NSE__NSE__MINUTE.csv 
timestamp,open,high,low,close,volume
2017-01-02 09:15:00+05:30,340.0,340.0,340.0,340.0,11.0
2017-01-02 09:16:00+05:30,340.0,340.0,340.0,340.0,0.0
2017-01-02 09:17:00+05:30,340.0,340.0,340.0,340.0,0.0
2017-01-02 09:18:00+05:30,340.0,343.7,340.0,343.7,1.0
2017-01-02 09:19:00+05:30,343.7,343.7,343.7,343.7,1.0
2017-01-02 09:20:00+05:30,341.0,341.0,341.0,341.0,932.0
2017-01-02 09:21:00+05:30,341.0,341.0,339.0,339.0,7.0
2017-01-02 09:22:00+05:30,339.0,339.15,338.0,338.0,26.0
2017-01-02 09:23:00+05:30,338.0,338.95,338.0,338.95,4.0
2017-01-02 09:24:00+05:30,337.3,338.5,337.3,337.5,131.0
2. data/v0: ABCAPITAL__EQ__NSE__NSE__MINUTE.csv
timestamp,open,high,low,close,volume
2017-09-01 09:44:00+05:30,250.0,250.0,250.0,250.0,1734282.0
2017-09-01 09:45:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:46:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:47:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:48:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:49:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:50:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:51:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:52:00+05:30,250.0,250.0,250.0,250.0,0.0
2017-09-01 09:53:00+05:30,250.0,250.0,250.0,250.0,0.0

And this v1 of the dataset:
 1. data/v1: ABFRL__EQ__NSE__NSE__MINUTE.csv
timestamp,open,high,low,close,volume
2017-01-02 09:15:00+05:30,138.5,138.65,138.5,138.5,450.0
2017-01-02 09:16:00+05:30,138.5,138.5,138.2,138.2,152.0
2017-01-02 09:17:00+05:30,138.2,138.25,138.2,138.25,150.0
2017-01-02 09:18:00+05:30,138.25,138.4,138.2,138.2,193.0
2017-01-02 09:19:00+05:30,138.05,138.1,138.0,138.0,694.0
2017-01-02 09:20:00+05:30,138.0,138.0,137.55,137.55,166.0
2017-01-02 09:21:00+05:30,137.55,137.55,137.55,137.55,500.0
2017-01-02 09:22:00+05:30,137.6,137.9,137.6,137.9,425.0
2017-01-02 09:23:00+05:30,137.9,137.9,137.55,137.55,500.0
2017-01-02 09:24:00+05:30,137.55,138.0,137.55,138.0,290.0
2. data/v1 : ADANIENT__EQ__NSE__NSE__MINUTE.csv
timestamp,open,high,low,close,volume
2017-01-02 09:15:00+05:30,77.75,77.75,77.4,77.45,63111.0
2017-01-02 09:16:00+05:30,77.45,77.6,77.35,77.35,33705.0
2017-01-02 09:17:00+05:30,77.3,77.45,77.2,77.25,31347.0
2017-01-02 09:18:00+05:30,77.2,77.3,77.1,77.15,13325.0
2017-01-02 09:19:00+05:30,77.15,77.3,77.1,77.3,34188.0
2017-01-02 09:20:00+05:30,77.25,77.25,77.05,77.05,18157.0
2017-01-02 09:21:00+05:30,77.0,77.2,77.0,77.2,26836.0
2017-01-02 09:22:00+05:30,77.2,77.2,76.9,77.0,30348.0
2017-01-02 09:23:00+05:30,76.9,77.0,76.6,76.65,32247.0
2017-01-02 09:24:00+05:30,76.7,76.85,76.55,76.8,20594.0
3. data/v1: ADANIGAS__EQ__NSE__NSE__MINUTE.csv
timestamp,open,high,low,close,volume
2018-11-05 09:44:00+05:30,72.0,72.0,72.0,72.0,266609.0
2018-11-05 09:45:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:46:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:47:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:48:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:49:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:50:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:51:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:52:00+05:30,72.0,72.0,72.0,72.0,0.0
2018-11-05 09:53:00+05:30,72.0,72.0,72.0,72.0,0.0

So the dataset was quite large thats considerting this is small subset of data all files are in csv 


Now the oppe assignment instruction:
First i will start with the problem statement: Your job is to build the stock movement predictor with end 2 end mlops tooling (DVC, feast, mlflow, ci with CML) on gcp --- same type of instruction which are there before as well you know the context. 

And for the instrcution explicitily mentioned like one of the instruction is; split the dataset into train and test split as well , dont assume the data is sorted in chronological form in the file.......

As of now just tell me the instruction are clear to you or not....

Next i will sent you the oppe-instructions , Note you are not agent you will not edit the files or code same behavior as we are doing before....
problem statement :
Problem Description
You are working as an MLOps engineer in an investment firm. Your task is to build a predictor for stock movements in the next 5 minutes.

Using minute-level and historical data, predict at every minute whether a particular stock will trade up or down 5 minutes later.

The features you will compute and use for prediction, along with raw data, are described below:
[Screenshot]

* Where 
t
t is the time instant of the prediction.

Target and Training Details
Predict 1 if the stock will close 5 minutes later at a price higher than the current price, and 0 otherwise.
Use the past 10 minutes of data to predict the outcome 5 minutes into the future.
Create the prediction/target column for the entire dataset based on actual stock price values. Use this as the ground truth for training and testing.
Train the predictor in two iterations:
Iteration 1: Use v0 data only.
Iteration 2: Use the merged data of v0 and v1.
If data is missing, process the last 10 available data points.

Pipeline overview:
Pipeline Overview
Note: This diagram shows the high-level flow only. Refer to the Deliverables section below for specific implementation instructions, requirements, and marking criteria before you start building.

Raw Data: v0 and v1 CSV files from the MLOPS_MAY_2026_OPPE1 repository (main branch).
DVC (Data Versioning): Track both data versions using Google Cloud Storage (GCS) as the remote storage backend.
Feast (Feature Store): Compute, store, and serve rolling features for training.
Training (2 Iterations):
Iteration 1: v0 data only.
Iteration 2: Merged v0 and v1 data.
MLflow (Tracking & Registry): Log hyperparameter tuning runs and register the best model to the Model Registry.
CI (Continuous Integration): Run on the main branch to:
Fetch the best model from MLflow.
Fetch test data from DVC.
Run sanity tests per feature.
CML (Report Generation): Post metrics and plots as a comment on the GitHub Pull Request (PR).

So There are 6 deliverables:
D1 is done
now starts with D2: data versioning with DVC
Track both provided data versions (v0 and v1) as distinct, reproducible snapshots using DVC, so either version can be restored from its Git-committed pointer.

Initialize DVC and add each data version, committing the resulting .dvc pointer files to Git.
Configure Google Cloud Storage (GCS) as the remote storage backend and push both versions using dvc push.
Demonstrate that you can check out a specific version and pull it back from the remote using dvc pull.

D3: Feast Feature Store Integration 
Compute the rolling features and register them in a Feast Feature Store so they can be stored and served for training.

Define an entity (stock_name) and feature views for rolling_avg_10 and volume_sum_10.
Apply and materialize the feature definitions to the store.
Retrieve a point-in-time correct training dataset from Feast to avoid look-ahead leakage.
D4: Training & Evaluation — 2 Incremental Iterations
Execute training and evaluation scripts that produce valid predictions across two incremental data iterations, demonstrating how the model responds as more data becomes available.

Iteration 1: Train and evaluate on v0 data only.
Iteration 2: Retrain and evaluate on the merged v0 + v1 data.
Use a proper train/test split and report evaluation metrics for each iteration.

D 5: Hyperparameter Tuning & Experiment Tracking with MLflow 
Run a hyperparameter tuning sweep and track every run with MLflow, so runs can be compared and the best model promoted.

Log parameters, metrics, and artifacts for each tuning run to MLflow Tracking.
Select the best run based on your chosen evaluation metric.
Register the best model to the MLflow Model Registry so CI can fetch it by name.
D6 : CI on Main Branch with CML Report Generation 
Configure a Continuous Integration (CI) workflow that runs on the main branch and executes the following pipeline on each trigger:

Fetch the best model from the MLflow Model Registry.
Pull the versioned test data from DVC (the Git-pinned snapshot, ensuring a reproducible evaluation).
Run predictions and compute evaluation metrics on the test data.
Include at least one sanity test per feature to validate each feature against the raw data.
Generate a CML report and post the metrics and plots as a comment on the GitHub PR.


now here is catch considering the model usage low kindly code where the changes are applicable and aviod creating same file as you created before.... just tell me that [you can use this exact file (previous one)]
```
**Response Log:**  
[## D3 — Feast

**`feast_repo/feature_store.yaml`** [NEW FILE]
```yaml
project: stock_predictor
registry: feast_repo/registry.db
provider: local
offline_store:
    type: file
entity_key_serialization_version: 2
```

**`feast_repo/features.py`** [NEW FILE]
```python
from datetime import timedelta
from pathlib import Path
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64

PROJECT_ROOT = Path(__file__).resolve().parent.parent

stock_entity = Entity(name="stock_name", description="Stock ticker symbol")

stock_source = FileSource(
    path=str(PROJECT_ROOT / "data" / "features" / "stock_features.parquet"),
    timestamp_field="event_timestamp",
)

stock_features_view = FeatureView(
    name="stock_features",
    entities=[stock_entity],
    ttl=timedelta(days=9999),
    schema=[
        Field(name="rolling_avg_10", dtype=Float64),
        Field(name="volume_sum_10",  dtype=Float64),
    ],
    source=stock_source,
    online=False,
)
```

**`scripts/prepare_features.py`** [NEW FILE]
```python
"""Compute rolling features from raw CSVs → save parquet → feast apply."""
import sys
import subprocess
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FEATURE_COLS = ["rolling_avg_10", "volume_sum_10"]


def load_stock_data(folders: list) -> pd.DataFrame:
    dfs = []
    for folder in folders:
        for csv_file in Path(folder).glob("*.csv"):
            stock_name = csv_file.stem.split("__")[0]
            df = pd.read_csv(csv_file, parse_dates=["timestamp"])
            df["stock_name"] = stock_name
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["stock_name", "timestamp"]).reset_index(drop=True)
    result = []
    for _, group in df.groupby("stock_name"):
        g = group.copy()
        g["rolling_avg_10"] = g["close"].rolling(window=10, min_periods=1).mean()
        g["volume_sum_10"]  = g["volume"].rolling(window=10, min_periods=1).sum()
        result.append(g)
    out = pd.concat(result, ignore_index=True)
    out = out.rename(columns={"timestamp": "event_timestamp"})
    out["event_timestamp"] = pd.to_datetime(out["event_timestamp"], utc=True)
    return out[["stock_name", "event_timestamp", "rolling_avg_10", "volume_sum_10"]]


if __name__ == "__main__":
    version = sys.argv[1] if len(sys.argv) > 1 else "v0"
    folders = [PROJECT_ROOT / "data" / "v0"]
    if version == "v1":
        folders.append(PROJECT_ROOT / "data" / "v1")

    df = load_stock_data(folders)
    feat_df = compute_features(df)

    out_path = PROJECT_ROOT / "data" / "features" / "stock_features.parquet"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    feat_df.to_parquet(out_path, index=False)
    print(f"Saved {len(feat_df)} rows → {out_path}")

    subprocess.run(["feast", "-c", str(PROJECT_ROOT / "feast_repo"), "apply"], check=True)
    print("Feast apply done.")
```

**Run D3 commands [POWERSHELL]:**
```powershell
# Install feast
pip install feast

# Iteration 1 — v0 only
python scripts/prepare_features.py v0

# Iteration 2 — v0 + v1
python scripts/prepare_features.py v1

git add feast_repo/ data/features/ scripts/prepare_features.py
git commit -m "D3: Add Feast feature store with rolling_avg_10 and volume_sum_10"
git push origin main
```

---

## D4 + D5 — `scripts/train.py` [COMPLETE REWRITE]

```python
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
    """Retrieve point-in-time correct features from Feast."""
    store = FeatureStore(repo_path=str(FEAST_REPO))
    entity_df = df[["stock_name", "timestamp"]].copy()
    entity_df = entity_df.rename(columns={"timestamp": "event_timestamp"})
    entity_df["event_timestamp"] = pd.to_datetime(
        entity_df["event_timestamp"], utc=True
    )
    training_df = store.get_historical_features(
        entity_df=entity_df,
        features=["stock_features:rolling_avg_10",
                  "stock_features:volume_sum_10"],
    ).to_df()
    return training_df


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
        ["python", str(PROJECT_ROOT / "scripts" / "prepare_features.py"),
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
```

**Run [POWERSHELL]:**
```powershell
python scripts/train.py
git add outputs/ models/model.pkl
dvc add models/model.pkl
git add models/model.pkl.dvc
git commit -m "D4+D5: Train stock predictor with Feast features + MLflow HPT"
dvc push && git push origin main
```

---

## D6 — CI Changes

### Expose MLflow publicly for CI [CLOUD SHELL]
```bash
# Add firewall tag to VM
gcloud compute instances add-tags oppe-mlflow-vm \
  --tags=oppe-mlflow --zone=us-central1-a \
  --project=project-42aa52a6-0cc6-4d7b-863

# Allow port 8100
gcloud compute firewall-rules create allow-mlflow-oppe \
  --project=project-42aa52a6-0cc6-4d7b-863 \
  --direction=INGRESS --action=ALLOW --rules=tcp:8100 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=oppe-mlflow
```

Add GitHub secret:
```
Name:  MLFLOW_TRACKING_URI
Value: http://35.184.116.2:8100
```

### `scripts/infer.py` — update for stock features [USE PREVIOUS STRUCTURE, update these parts]
```python
# Change these from previous infer.py:
FEATURE_COLS = ["rolling_avg_10", "volume_sum_10"]
LABELS = {0: "down", 1: "up"}
MODEL_NAME = "stock-movement-predictor"

def predict(features: list) -> int:
    if len(features) != 2:   # ← was 4 for iris
        raise ValueError("Exactly 2 features required: rolling_avg_10, volume_sum_10")
    model = load_model()
    frame = pd.DataFrame([features], columns=FEATURE_COLS)
    pred = model.predict(frame)[0]
    return int(pred)
```

### `tests/test_infer.py` — sanity tests per feature [UPDATE]
```python
import pytest, sys
import pandas as pd
import numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.inference import predict, load_model

# ── Model tests ───────────────────────────────────────────────────────────────
def test_model_loads():
    assert load_model() is not None

def test_predict_returns_binary():
    result = predict([340.0, 1000.0])
    assert result in {0, 1}

def test_invalid_feature_count():
    with pytest.raises(ValueError):
        predict([340.0])  # only 1 feature

# ── Sanity tests per feature (raw data) ──────────────────────────────────────
@pytest.fixture(scope="module")
def raw_v0():
    data_dir = Path(__file__).resolve().parent.parent / "data" / "v0"
    dfs = []
    for f in data_dir.glob("*.csv"):
        df = pd.read_csv(f)
        df["stock_name"] = f.stem.split("__")[0]
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def test_rolling_avg_10_within_price_range(raw_v0):
    """rolling_avg_10 must be between min and max close price per stock."""
    for stock, group in raw_v0.groupby("stock_name"):
        group = group.sort_values("timestamp").copy()
        group["rolling_avg_10"] = group["close"].rolling(10, min_periods=1).mean()
        assert group["rolling_avg_10"].between(
            group["close"].min(), group["close"].max()
        ).all(), f"rolling_avg_10 out of range for {stock}"

def test_volume_sum_10_non_negative(raw_v0):
    """volume_sum_10 must be >= 0."""
    for stock, group in raw_v0.groupby("stock_name"):
        group = group.sort_values("timestamp").copy()
        group["volume_sum_10"] = group["volume"].rolling(10, min_periods=1).sum()
        assert (group["volume_sum_10"] >= 0).all(), f"Negative volume_sum_10 for {stock}"

def test_rolling_avg_10_not_all_null(raw_v0):
    """rolling_avg_10 should have no NaN (min_periods=1)."""
    for stock, group in raw_v0.groupby("stock_name"):
        group["rolling_avg_10"] = group["close"].rolling(10, min_periods=1).mean()
        assert group["rolling_avg_10"].isna().sum() == 0
```

### `ci.yml` — update eval step only [REST REUSE FROM BEFORE]
```yaml
# Replace the "Run model evaluation" step with:
- name: Fetch champion model from MLflow and evaluate
  env:
    MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
  run: python scripts/ci_evaluate.py
```

### `scripts/ci_evaluate.py` [NEW FILE]
```python
"""CI evaluation: fetch champion from MLflow, run on test data."""
import os
import mlflow
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
from pathlib import Path

PROJECT_ROOT  = Path(__file__).resolve().parent.parent
MLFLOW_URI    = os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:8100")
MODEL_NAME    = "stock-movement-predictor"
FEATURE_COLS  = ["rolling_avg_10", "volume_sum_10"]

mlflow.set_tracking_uri(MLFLOW_URI)

# Load champion from MLflow registry
try:
    model = mlflow.sklearn.load_model(f"models:/{MODEL_NAME}@champion")
    print("Loaded champion from MLflow registry")
except Exception as e:
    print(f"MLflow load failed: {e} — falling back to model.pkl")
    model = joblib.load(PROJECT_ROOT / "models" / "model.pkl")

# Load test data (v0, DVC pulled)
dfs = []
for f in (PROJECT_ROOT / "data" / "v0").glob("*.csv"):
    df = pd.read_csv(f, parse_dates=["timestamp"])
    df["stock_name"] = f.stem.split("__")[0]
    dfs.append(df)
df = pd.concat(dfs, ignore_index=True).sort_values(["stock_name", "timestamp"])

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
```
---

## Final CI.YML — Only update these two steps from the mock version

```yaml
# Replace step 7 "Train model in CI" with:
- name: Fetch champion model from MLflow and evaluate
  env:
    MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
  run: python scripts/ci_evaluate.py

# In "Build report" step — change the inline Python to:
- name: Build report
  if: always()
  run: |
    echo "## Stock Movement Predictor CI Report" > report.md
    echo '```' >> report.md
    cat pytest.log >> report.md
    echo '```' >> report.md
    echo "### Evaluation Metrics" >> report.md
    cat metrics.txt >> report.md
```
---
---

**Prompt 8** *(D5 — GitHub Actions CI)*  
```
Write a GitHub Actions workflow (ci.yml) that:
1. Triggers on every push
2. Sets up Python 3.10
3. Installs dependencies
4. Authenticates to GCS using a service account key secret
5. Pulls test data using DVC
6. Runs pytest on the inference tests
7. Runs model evaluation script
```
**Response Log:**  
[paste AI response here]

---

**Prompt 9** *(Debugging — if any)*  
```
[paste exact error message you got]
```
**Response Log:**  
[paste AI response here]

---

### Tool: GitHub Copilot (GPT-5.3-Codex)

---

**Prompt 1** *(Environment check - Feast install confusion)*  
```
how feast
Name: feast
Version: 0.65.0
...
this means feast is installed ryt?
```
**Response Log:**  
- Copilot confirmed that `pip show feast` indicates Feast is installed in the queried environment.
- Copilot also highlighted an interpreter mismatch risk (pip from one environment, python from another).

---

**Prompt 2** *(Runtime mismatch error)*  
```
(.venv) PS ...> pip show feast
...
(.venv) PS ...> python -m feast -c feast_repo apply
...python.exe: No module named feast

but seee
```
**Response Log:**  
- Copilot diagnosed that `python` and `pip` were resolving to different interpreters.
- It verified that one shell was using Windows Store Python, while Feast was installed elsewhere.
- It provided the reliable command path using explicit venv python.

---

**Prompt 3** *(Direct fix request)*  
```
yes resolve this asap
```
**Response Log:**  
- Copilot installed Feast in the project venv and validated interpreter paths.
- It found `python -m feast` was not valid for this package layout and switched invocation to the venv `feast.exe` entrypoint.
- Code changes applied:
	- `scripts/prepare_features.py`: use venv-safe Feast CLI execution.
	- `scripts/train.py`: use `sys.executable` instead of bare `python` for subprocess calls.

---

**Prompt 4** *(Command usability confirmation)*  
```
so can i now run the script into my terminal .venv?
```
**Response Log:**  
- Copilot confirmed yes, and recommended explicit interpreter usage:
	- `.\\.venv\\Scripts\\python.exe scripts\\prepare_features.py v0`
- It explained this avoids path/interpreter drift across terminals.

---

**Prompt 5** *(Need exact commands)*  
```
yes please give cmds
```
**Response Log:**  
- Copilot provided exact PowerShell commands for activation and execution.
- It also gave fallback explicit venv commands when shell activation is unreliable.

---

**Prompt 6** *(Major training failure)*  
```
resolve this error: ...
numpy._core._exceptions._ArrayMemoryError: Unable to allocate 1.69 TiB ...
```
**Response Log:**  
- Copilot traced root cause to Feast historical retrieval causing a very large Dask join.
- It replaced the expensive retrieval path in `scripts/train.py` with direct loading of precomputed feature parquet (`data/features/stock_features.parquet`) and controlled merge.
- It re-ran training successfully end-to-end and confirmed model registration outputs.

---

**Prompt 7** *(Pre-CI alignment question)*  
```
so conserding all such changes ... did u suggest any changes regarding ci.yml, test_infer.py and infer.py ci_evalure.py ??
```
**Response Log:**  
- Copilot reviewed all requested files and identified required adjustments:
	- fix inference CLI usage text,
	- standardize test filename,
	- ensure CI/evaluation compatibility,
	- clarify `infer.py` vs `inference.py` mismatch.

---

**Prompt 8** *(Apply remaining items)*  
```
ok do it for 2 3 4 5 i have did workflow part
```
**Response Log:**  
- Copilot implemented the requested updates:
	- `scripts/infer.py`: corrected 2-feature CLI behavior and fallback model setup.
	- `scripts/ci_evaluate.py`: added guardrails for missing model/data paths.
	- renamed `tests/test.infer.py` -> `tests/test_infer.py`.
	- added compatibility wrapper `scripts/inference.py`.
- Copilot then ran tests, fixed failing assertions to reflect real data behavior, and verified:
	- `pytest tests/test_infer.py -q` -> `6 passed`.

---

## Notes
- All code was reviewed and understood before committing
- AI was used for boilerplate and pattern generation; logic was verified manually