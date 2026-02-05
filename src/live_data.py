# src/live_data.py
import requests
import pandas as pd

BINANCE_URL = "https://api.binance.com/api/v3/klines"

def fetch_latest_candles(
    symbol="BTCUSDT",
    interval="5m",
    limit=200
):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    r = requests.get(BINANCE_URL, params=params, timeout=10)
    r.raise_for_status()

    data = r.json()

    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume", "ignore"
    ])

    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df.set_index("open_time", inplace=True)

    numeric_cols = [
        "open", "high", "low", "close", "volume",
        "quote_asset_volume",
        "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume",
    ]
    df[numeric_cols] = df[numeric_cols].astype(float)

    return df
