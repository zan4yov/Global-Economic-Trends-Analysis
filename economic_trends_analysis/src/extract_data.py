from __future__ import annotations
import time
import requests
import pandas as pd
from typing import List, Dict
from .constants import INDICATORS
from .utils import get_env

WB_BASE = "https://api.worldbank.org/v2"

def _fetch_single_page(country: str, indicator: str, page: int = 1, per_page: int = 2000) -> Dict:
    url = f"{WB_BASE}/country/{country}/indicator/{indicator}?format=json&per_page={per_page}&page={page}"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.json()

def fetch_indicator_for_countries(countries: List[str], indicator_code: str, sleep_sec: float = 0.15) -> pd.DataFrame:
    frames = []
    for c in countries:
        # First page to know total pages
        j = _fetch_single_page(c, indicator_code, page=1)
        if not isinstance(j, list) or len(j) < 2 or j[1] is None:
            continue
        meta, data = j[0], j[1]
        pages = int(meta.get('pages', 1))
        frames.append(pd.json_normalize(data))
        for p in range(2, pages + 1):
            time.sleep(sleep_sec)  # polite
            j = _fetch_single_page(c, indicator_code, page=p)
            if isinstance(j, list) and len(j) >= 2 and j[1] is not None:
                frames.append(pd.json_normalize(j[1]))
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    df["indicator_id"] = indicator_code
    return df

def extract() -> pd.DataFrame:
    countries_env = get_env("COUNTRIES")
    countries = [c.strip() for c in countries_env.split(",")] if countries_env else None
    if not countries:
        from .constants import COUNTRIES as DEFAULT_C
        countries = DEFAULT_C

    # Pull all indicators
    all_frames = []
    for name, code in INDICATORS.items():
        df_i = fetch_indicator_for_countries(countries, code)
        if not df_i.empty:
            all_frames.append(df_i)
    if not all_frames:
        return pd.DataFrame()
    df = pd.concat(all_frames, ignore_index=True)

    # Select essential columns and standardize names
    keep = [
        "country.id", "country.value", "countryiso3code",
        "date", "value", "indicator_id"
    ]
    # some fields may be missing depending on the country/indicator
    for col in keep:
        if col not in df.columns:
            df[col] = None
    df = df[keep].rename(columns={
        "country.id": "country_code",
        "country.value": "country_name",
        "date": "year",
        "value": "indicator_value"
    })
    return df
