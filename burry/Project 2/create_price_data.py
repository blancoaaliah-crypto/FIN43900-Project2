
from pathlib import Path
import pandas as pd
import yfinance as yf

# Historical data for Project 2
# All observations must be on or before March 31, 2026.
TICKERS = {
    "SGOV": "Treasury bills",
    "IEF": "Treasury 10-year note",
    "LQD": "Investment-grade bond fund",
    "VT": "Global equity index fund",
}

START = "2021-01-01"
END_EXCLUSIVE = "2026-04-01"

OUTPUT = Path(__file__).parent / "monthly_prices.csv"

series = []

for ticker, name in TICKERS.items():
    print(f"Downloading {ticker}...")

    data = yf.download(
        ticker,
        start=START,
        end=END_EXCLUSIVE,
        auto_adjust=True,
        progress=False,
        threads=False,
    )

    if data.empty:
        raise RuntimeError(f"No data returned for {ticker}")

    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    close.index = pd.to_datetime(close.index)

    monthly = close.resample("ME").last()
    monthly.name = name
    series.append(monthly)

prices = pd.concat(series, axis=1).dropna()
prices.index.name = "Date"

if prices.empty or len(prices) < 38:
    raise RuntimeError("Insufficient shared monthly history")

if prices.index.max() > pd.Timestamp("2026-03-31"):
    raise RuntimeError("Future observations detected")

prices.to_csv(OUTPUT)

print(f"\nSaved: {OUTPUT}")
print(f"Monthly price rows: {len(prices)}")
print(f"First date: {prices.index.min().date()}")
print(f"Last date: {prices.index.max().date()}")
print("\nLast five rows:")
print(prices.tail().to_string())