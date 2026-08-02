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