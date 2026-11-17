
"""
FIN 43900 — Project 2
Point-in-Time Treasury Yield Signal

Adapted from the student's Lab 17 FRED/ALFRED audit.
AI-assisted implementation: Codex/ChatGPT.

Educational use only — not investment advice.
"""

import io
from datetime import date
from urllib.parse import quote

import pandas as pd
import requests


SERIES_ID = "DGS10"
SERIES_NAME = "10-Year Treasury Constant Maturity Rate"

SOURCE_URL = "https://fred.stlouisfed.org/series/DGS10"


def read_csv(url):
    response = requests.get(url, timeout=35)
    response.raise_for_status()

    frame = pd.read_csv(
        io.StringIO(response.text),
        na_values=["."]
    )

    if frame.shape[1] < 2:
        raise ValueError("Invalid FRED/ALFRED CSV.")

    dates = pd.to_datetime(
        frame.iloc[:, 0],
        errors="coerce"
    )

    values = pd.to_numeric(
        frame.iloc[:, 1],
        errors="coerce"
    )

    series = pd.Series(
        values.to_numpy(),
        index=dates,
        name=SERIES_ID
    ).dropna()

    series = series.loc[series.index.notna()]

    if series.empty:
        raise ValueError("No valid observations returned.")

    return series.sort_index()


def download_current():
    url = (
        "https://fred.stlouisfed.org/graph/"
        f"fredgraph.csv?id={quote(SERIES_ID)}"
    )
    return read_csv(url)


def download_vintage(as_of_date):
    vintage = pd.Timestamp(as_of_date).date().isoformat()

    if pd.Timestamp(vintage).date() > date.today():
        raise ValueError(
            "Decision date cannot be in the future."
        )

    url = (
        "https://alfred.stlouisfed.org/graph/"
        f"alfredgraph.csv?id={quote(SERIES_ID)}"
        f"&vintage_date={vintage}"
    )

    series = read_csv(url)

    # Prevent future observation dates entering the decision.
    return series.loc[
        series.index <= pd.Timestamp(vintage)
    ]


def build_signal(as_of_date, lookback=20):
    """
    Compare the last available DGS10 yield with the
    average of the last 20 available observations.

    DGS10 values are quoted in percentage points.
    The difference is converted to basis points.

    This is a monitoring indicator, not a return forecast.
    """

    if lookback < 2:
        raise ValueError("Lookback must be at least 2.")

    known = download_vintage(as_of_date)

    if len(known) < lookback:
        raise ValueError(
            "Not enough observations for the signal."
        )

    window = known.tail(lookback)

    latest_yield = float(window.iloc[-1])
    average_yield = float(window.mean())

    spread_bps = (
        latest_yield - average_yield
    ) * 100

    if spread_bps > 10:
        status = "Above recent average"
    elif spread_bps < -10:
        status = "Below recent average"
    else:
        status = "Near recent average"

    return {
        "series_id": SERIES_ID,
        "series_name": SERIES_NAME,
        "source": SOURCE_URL,
        "decision_date": str(
            pd.Timestamp(as_of_date).date()
        ),
        "observation_date": str(
            window.index[-1].date()
        ),
        "latest_yield": latest_yield,
        "average_yield": average_yield,
        "spread_bps": spread_bps,
        "status": status,
        "lookback": lookback,
        "history": window,
        "availability_rule": (
            "Use the ALFRED vintage corresponding "
            "to the decision date; exclude "
            "observations dated after that date."
        ),
    }