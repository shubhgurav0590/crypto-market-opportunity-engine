import json
import joblib
import pandas as pd
from src.config import MODELS_DIR
from src.features import validate_features

def load_model(model_name: str, version: str):
    model_path = MODELS_DIR / f"{model_name}_v{version}.pkl"
    return joblib.load(model_path)

def predict(df: pd.DataFrame, model_name: str, version: str):
    with open(MODELS_DIR / "metadata.json") as f:
        metadata = json.load(f)

    X = validate_features(df)

    model = load_model(model_name, version)
    return model.predict_proba(X)[:, 1]
if __name__ == "__main__":
    print("✅ inference.py executed successfully")