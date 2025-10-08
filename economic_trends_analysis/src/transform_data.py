from __future__ import annotations
import pandas as pd
from typing import Optional
from .constants import INDICATORS
from .utils import get_env

def _coerce_year(s: pd.Series) -> pd.Series:
    # World Bank years are strings like "2024"
    return pd.to_numeric(s, errors="coerce").astype("Int64")

def transform(df_raw: pd.DataFrame) -> pd.DataFrame:
    if df_raw is None or df_raw.empty:
        return pd.DataFrame()

    # Drop null values
    df = df_raw.dropna(subset=["indicator_value"]).copy()

    # Cast year
    df["year"] = _coerce_year(df["year"])

    # Filter by year range from env if provided
    start_year = get_env("START_YEAR")
    end_year = get_env("END_YEAR")
    if start_year:
        df = df[df["year"] >= int(start_year)]
    if end_year:
        df = df[df["year"] <= int(end_year)]

    # Pivot to wide: one row per country/year with columns for each indicator
    code_to_name = {v: k for k, v in INDICATORS.items()}
    df["indicator_name"] = df["indicator_id"].map(code_to_name)

    wide = df.pivot_table(
        index=["countryiso3code","country_code","country_name","year"],
        columns="indicator_name",
        values="indicator_value",
        aggfunc="first"
    ).reset_index()

    # Sort for readability
    wide = wide.sort_values(["country_name","year"]).reset_index(drop=True)

    # Reorder columns
    cols = ["countryiso3code","country_code","country_name","year","gdp_growth","inflation","unemployment"]
    for c in cols:
        if c not in wide.columns:
            wide[c] = pd.NA
    wide = wide[cols]

    return wide
