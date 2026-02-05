# src/config.py

FEATURE_CONFIG = {
    "return_window": 5,
    "vol_window": 10,
    "rsi_window": 14,
}

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = PROJECT_ROOT / "models"

TARGET_COL = "target"

FEATURE_COLS = [
    "ema_diff",
    "rsi_14",
    "vol_ratio",
    "ema_diff_lag_1",
    "ema_diff_lag_2",
    "ema_diff_lag_3",
    "rsi_14_lag_1",
    "rsi_14_lag_2",
    "vol_ratio_lag_1",
    "trend",
]

FEATURE_SCHEMA = {
    col: "numeric" for col in FEATURE_COLS
}

MODEL_CONFIG = {
    "logreg": {"max_iter": 1000},
    "random_forest": {"n_estimators": 200, "max_depth": 6},
    "xgboost": {"n_estimators": 300, "max_depth": 5, "learning_rate": 0.05},
}
# =========================
# SIGNAL THRESHOLDS (LIVE)
# =========================
BUY_THRESHOLD = 0.60
SELL_THRESHOLD = 0.40
