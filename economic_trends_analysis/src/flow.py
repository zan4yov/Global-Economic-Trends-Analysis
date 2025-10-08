from __future__ import annotations
from prefect import flow, task
import pandas as pd
from .extract_data import extract
from .transform_data import transform
from .load_data import load

@task(retries=2, retry_delay_seconds=10)
def t_extract() -> pd.DataFrame:
    return extract()

@task
def t_transform(df: pd.DataFrame) -> pd.DataFrame:
    return transform(df)

@task
def t_load(df: pd.DataFrame) -> None:
    load(df)

@flow(name="economic_trends_pipeline")
def main():
    df_raw = t_extract()
    df_clean = t_transform(df_raw)
    t_load(df_clean)

if __name__ == "__main__":
    main()
