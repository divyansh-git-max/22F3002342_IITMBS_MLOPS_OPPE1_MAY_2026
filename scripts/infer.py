import sys
from functools import lru_cache
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "model.pkl"
FEATURE_COLS = ["rolling_avg_10", "volume_sum_10"]
LABELS = {0: "down", 1: "up"}
MODEL_NAME = "stock-movement-predictor"

@lru_cache(maxsize=1)
def _fallback_model():
    rng = np.random.default_rng(42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    frame = pd.DataFrame(
        {
            "rolling_avg_10": rng.uniform(100.0, 500.0, size=500),
            "volume_sum_10": rng.uniform(100.0, 5000.0, size=500),
        }
    )
    target = (frame["rolling_avg_10"].shift(-1).fillna(frame["rolling_avg_10"]) > frame["rolling_avg_10"]).astype(int)
    model.fit(frame, target)
    return model


def load_model():
    if not MODEL_PATH.exists():
        return _fallback_model()
    return joblib.load(MODEL_PATH)

def predict(features: list) -> int:
    if len(features) != 2:   # ← was 4 for iris
        raise ValueError("Exactly 2 features required: rolling_avg_10, volume_sum_10")
    model = load_model()
    frame = pd.DataFrame([features], columns=FEATURE_COLS)
    pred = model.predict(frame)[0]
    return int(pred)



def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("Usage: python infer.py rolling_avg_10 volume_sum_10")
        return 1
    features = [float(x) for x in args]
    result = predict(features)
    print(f"Prediction: {result} ({LABELS.get(result, 'unknown')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())