# End-to-End Stock Movement Predictor Pipeline (OPPE-1)

**Student Name:** Divyansh Ajay  
**Roll Number:** 22f3002342  
**Course:** IITM BS MLOps (May 2026)

---

## 📌 Problem Statement
The objective of this project is to build a machine learning predictor for stock movements. Given minute-level historical stock data, the model predicts whether a particular stock will trade up or down exactly 5 minutes into the future (Target `1` if close price increases, `0` otherwise). 

The predictor uses a rolling 10-minute window of historical data to make its predictions. The project implements a complete, end-to-end MLOps pipeline on Google Cloud Platform (GCP) encompassing data versioning, feature stores, experiment tracking, and continuous integration.

---

## 🏗️ Architecture & Tools Used
- **Cloud Infrastructure:** GCP Compute Engine (Debian 12 Virtual Machine)
- **Data Versioning:** DVC (Google Cloud Storage Remote)
- **Feature Store:** Feast (Local Offline Parquet Store)
- **Experiment Tracking:** MLflow (SQLite backend + GCS artifact store)
- **Continuous Integration (CI):** GitHub Actions
- **Authentication:** GCP Workload Identity Federation (WIF)
- **Reporting:** CML (Continuous Machine Learning)

---

## 🚀 Pipeline Deliverables

### 1. Data Versioning (DVC)
- The raw dataset consists of minute-level CSV files (Timestamp, Open, High, Low, Close, Volume) partitioned into two iterative batches (`v0` and `v1`).
- **DVC** tracks these folders. The data is stored remotely in a GCS bucket, allowing reproducibility by restoring specific Git-committed `.dvc` pointers via `dvc pull`.

### 2. Feature Engineering (Feast)
- Extracted features include `rolling_avg_10` (10-minute moving average of the close price) and `volume_sum_10` (10-minute rolling sum of volume).
- **Feast** is utilized as the offline feature store with `stock_name` defined as the primary entity. 
- During training, Feast's `get_historical_features` executes a point-in-time correct join to prevent look-ahead bias. The data is globally sorted by timestamp to ensure memory-efficient merges via Dask.

### 3. Training & Experiment Tracking (MLflow)
- The `RandomForestClassifier` is trained across two iterations to simulate continuous learning:
  - **Iteration 1:** Trained on `v0` data (AARTIIND, ABCAPITAL).
  - **Iteration 2:** Retrained on merged `v0 + v1` data (Adding ABFRL, ADANIENT, ADANIGAS).
- A chronologically ordered 80/20 train/test split is enforced.
- **MLflow** tracks hyperparameter tuning (`n_estimators`, `max_depth`). The best-performing model is registered to the MLflow Model Registry under the `champion` alias.

### 4. Continuous Integration & Reporting (GitHub Actions + CML)
- On every push to the `main` branch, the `.github/workflows/ci.yml` workflow is triggered.
- **WIF Auth:** The workflow authenticates to GCP securely using Workload Identity Federation, completely avoiding static JSON service account keys.
- **Evaluation:** The pipeline fetches the `champion` model dynamically from the public-facing MLflow VM server, pulls test data via DVC, and evaluates Accuracy and F1 score via `scripts/ci_evaluate.py`.
- **Reporting:** Using **CML**, metrics and sanity test logs are automatically posted as a markdown comment on the GitHub Pull Request.

---

## 📁 Repository Structure
```text
├── .dvc/                  # DVC configurations
├── .github/workflows/     # GitHub Actions CI pipeline (ci.yml)
├── data/                  # Raw CSV files tracked by DVC (v0, v1)
├── feast_repo/            # Feast Feature Store configurations and entities
├── models/                # Serialized model fallback (model.pkl)
├── scripts/
│   ├── prepare_features.py # Computes rolling features and saves to Parquet
│   ├── train.py            # Executes HPT, uses Feast, logs to MLflow
│   ├── infer.py            # CLI inference script
│   ├── inference.py        # Compatibility entrypoint for infer.py
│   └── ci_evaluate.py      # CI evaluation script utilizing MLflow Champion model
├── tests/                 # Pytest sanity tests (e.g., feature boundary validations)
├── requirements.txt       # Python dependencies 
└── README.md              # Project documentation
```

---

## 💻 Running the Pipeline Locally (Windows Environment)

Ensure your virtual environment is active. All commands below explicitly use the `.venv` executable to prevent module resolution errors.

### 1. Pull Data
```powershell
dvc pull
```

### 2. Generate Features & Apply Feast
For Iteration 1 (`v0`):
```powershell
.\.venv\Scripts\python.exe scripts\prepare_features.py v0
.\.venv\Scripts\python.exe -m feast -c feast_repo apply
```
For Iteration 2 (`v0 + v1`):
```powershell
.\.venv\Scripts\python.exe scripts\prepare_features.py v1
.\.venv\Scripts\python.exe -m feast -c feast_repo apply
```

### 3. Train Model & Register in MLflow
```powershell
.\.venv\Scripts\python.exe scripts\train.py
```

### 4. Run Inference CLI
The inference script expects exactly 2 features (`rolling_avg_10` and `volume_sum_10`):
```powershell
.\.venv\Scripts\python.exe scripts\infer.py 340.0 1000.0
```
*Or using the compatibility entrypoint:*
```powershell
.\.venv\Scripts\python.exe scripts\inference.py 340.0 1000.0
```

### 5. Run Tests
```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_infer.py -q
```

---

## ⚙️ CI Workflow Notes
The workflow file is located at `.github/workflows/ci.yml`.

To reduce runtime and prevent timeouts, the CI evaluation script (`scripts/ci_evaluate.py`) supports a fast evaluation mode configured via environment variables:
- `CI_EVAL_USE_MLFLOW=false`: Skips the remote MLflow model fetch.
- `CI_EVAL_MAX_ROWS_PER_STOCK=25000`: Caps the number of rows processed per stock during evaluation.

---

## 🔧 Troubleshooting

### `No module named feast`
If you encounter this error, it means your terminal's `python` command is not pointing to the correct virtual environment. 
**Solution:** Always invoke python directly from the venv path:
```powershell
.\.venv\Scripts\python.exe scripts\prepare_features.py v0
```

### Feast CLI Invocation Issues
Avoid relying on a globally installed Feast CLI. This repository calls Feast directly through the `.venv`-installed python module (`python -m feast`).

### Slow CI Evaluation
If the GitHub Actions workflow takes too long, utilize the fast mode environment variables (already configured in the workflow), or reduce the `CI_EVAL_MAX_ROWS_PER_STOCK` value further.
