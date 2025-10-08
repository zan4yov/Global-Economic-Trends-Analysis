from __future__ import annotations
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from .utils import get_env, BASE_DIR, ensure_dirs

def load(df: pd.DataFrame) -> None:
    if df is None or df.empty:
        print("No data to load.")
        return

    ensure_dirs()

    # Save CSV (friendly for Power BI)
    csv_path = BASE_DIR / "data" / "economic_metrics.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved CSV: {csv_path}")

    # Save to SQLite (optional)
    db_url = get_env("DB_URL", "sqlite:///data/economic_trends.db")
    engine = create_engine(db_url, future=True)
    with engine.begin() as conn:
        df.to_sql("economic_metrics", conn, if_exists="replace", index=False)
    print(f"Loaded table 'economic_metrics' to DB: {db_url}")
