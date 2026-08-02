"""Compute rolling features from raw CSVs -> save parquet -> feast apply."""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FEATURE_COLS = ["rolling_avg_10", "volume_sum_10"]


def feast_executable() -> Path:
    if sys.platform.startswith("win"):
        return Path(sys.executable).with_name("feast.exe")
    return Path(sys.executable).with_name("feast")


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

    if importlib.util.find_spec("feast") is None:
        raise SystemExit(
            "Feast is not installed in this environment. "
            "Install the project dependencies, then rerun this script."
        )

    feast_bin = feast_executable()
    if not feast_bin.exists():
        raise SystemExit(
            f"Feast CLI was not found at {feast_bin}. Install feast into this environment and rerun."
        )

    subprocess.run(
        [str(feast_bin), "-c", str(PROJECT_ROOT / "feast_repo"), "apply"],
        check=True,
    )
    print("Feast apply done.")