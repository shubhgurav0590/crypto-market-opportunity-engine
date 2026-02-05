import pandas as pd
import numpy as np

from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands
from ta.trend import EMAIndicator

from src.config import FEATURE_CONFIG, FEATURE_COLS


# =====================
# Feature generators
# =====================

def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    df["log_return"] = np.log(df["close"] / df["close"].shift(1))
    return df


def add_volatility(df: pd.DataFrame) -> pd.DataFrame:
    window = FEATURE_CONFIG["vol_window"]
    df["volatility"] = df["log_return"].rolling(window).std()
    return df


def add_rsi(df: pd.DataFrame) -> pd.DataFrame:
    window = FEATURE_CONFIG["rsi_window"]
    rsi = RSIIndicator(df["close"], window=window)
    df["rsi"] = rsi.rsi()          # old RSI
    df["rsi_14"] = df["rsi"]       # alias for model compatibility
    return df


def add_bollinger(df: pd.DataFrame) -> pd.DataFrame:
    bb = BollingerBands(df["close"])
    df["bb_high"] = bb.bollinger_hband()
    df["bb_low"] = bb.bollinger_lband()
    return df


def add_ema_features(df: pd.DataFrame) -> pd.DataFrame:
    ema_fast = EMAIndicator(df["close"], window=12).ema_indicator()
    ema_slow = EMAIndicator(df["close"], window=26).ema_indicator()

    df["ema_diff"] = ema_fast - ema_slow
    return df


def add_volume_features(df: pd.DataFrame) -> pd.DataFrame:
    df["vol_ratio"] = df["volume"] / df["volume"].rolling(20).mean()
    return df


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    for lag in [1, 2, 3]:
        df[f"ema_diff_lag_{lag}"] = df["ema_diff"].shift(lag)

    for lag in [1, 2]:
        df[f"rsi_14_lag_{lag}"] = df["rsi_14"].shift(lag)

    df["vol_ratio_lag_1"] = df["vol_ratio"].shift(1)
    return df


def add_trend(df: pd.DataFrame) -> pd.DataFrame:
    df["trend"] = (df["ema_diff"] > 0).astype(int)
    return df


# =====================
# Main pipeline
# =====================

def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = add_returns(df)
    df = add_volatility(df)
    df = add_rsi(df)
    df = add_bollinger(df)

    df = add_ema_features(df)
    df = add_volume_features(df)
    df = add_lag_features(df)
    df = add_trend(df)

    df.dropna(inplace=True)
    return df


# =====================
# Validation
# =====================

def validate_features(df: pd.DataFrame) -> pd.DataFrame:
    missing = set(FEATURE_COLS) - set(df.columns)
    if missing:
        raise ValueError(f"❌ Missing features: {missing}")

    X = df[FEATURE_COLS]

    non_numeric = X.select_dtypes(exclude=["number"]).columns.tolist()
    if non_numeric:
        raise ValueError(f"❌ Non-numeric features found: {non_numeric}")

    return X


# =====================
# CLI test
# =====================

if __name__ == "__main__":
    print("✅ features.py loaded with ALL features")
