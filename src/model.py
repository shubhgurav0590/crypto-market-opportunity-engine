import joblib
import json
from datetime import datetime

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False

from src.config import (
    MODELS_DIR, TARGET_COL, FEATURE_COLS, MODEL_CONFIG
)
from src.features import validate_features

MODEL_REGISTRY = {
    "logreg": LogisticRegression,
    "random_forest": RandomForestClassifier,
}

if XGBOOST_AVAILABLE:
    MODEL_REGISTRY["xgboost"] = XGBClassifier


def train_model(df, model_name: str, version: str):
    if model_name not in MODEL_REGISTRY:
        raise ValueError(f"Model '{model_name}' not supported")

    X = validate_features(df)
    y = df[TARGET_COL]

    model = MODEL_REGISTRY[model_name](**MODEL_CONFIG[model_name])
    model.fit(X, y)

    model_path = MODELS_DIR / f"{model_name}_v{version}.pkl"
    joblib.dump(model, model_path)

    metadata = {
        "model": model_name,
        "version": version,
        "features": FEATURE_COLS,
        "trained_at": datetime.utcnow().isoformat(),
    }

    with open(MODELS_DIR / "metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    return model_path
if __name__ == "__main__":
    print("✅ model.py executed successfully")