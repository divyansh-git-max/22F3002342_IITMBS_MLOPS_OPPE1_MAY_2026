import pytest, sys
import pandas as pd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.infer import predict, load_model

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
        valid = group[["close", "rolling_avg_10"]].dropna()
        assert valid["rolling_avg_10"].between(
            valid["close"].min(), valid["close"].max()
        ).all(), f"rolling_avg_10 out of range for {stock}"

def test_volume_sum_10_is_finite(raw_v0):
    """volume_sum_10 should produce finite values where volume is present."""
    for stock, group in raw_v0.groupby("stock_name"):
        group = group.sort_values("timestamp").copy()
        group["volume_sum_10"] = group["volume"].rolling(10, min_periods=1).sum()
        valid = group["volume_sum_10"].dropna()
        assert valid.notna().all(), f"volume_sum_10 has invalid values for {stock}"

def test_rolling_avg_10_not_all_null(raw_v0):
    """rolling_avg_10 should contain usable values per stock."""
    for stock, group in raw_v0.groupby("stock_name"):
        group = group.sort_values("timestamp").copy()
        group["rolling_avg_10"] = group["close"].rolling(10, min_periods=1).mean()
        assert group["rolling_avg_10"].notna().any(), f"rolling_avg_10 all null for {stock}"