# src/live_scheduler.py

import time
from datetime import datetime, timedelta, UTC

import src.config as config
from src.live_data import fetch_latest_candles
from src.features import generate_features
from src.inference import load_model
from src.alerts import send_telegram_alert


# =========================
# CONFIG
# =========================
MODEL_NAME = "random_forest"
VERSION = "1"
INTERVAL_MINUTES = 5


# =========================
# LOAD MODEL ONCE
# =========================
model = load_model(MODEL_NAME, VERSION)


# =========================
# TIME CONTROL
# =========================
def wait_until_next_candle(interval_minutes=5):
    now = datetime.now(UTC)
    next_min = (now.minute // interval_minutes + 1) * interval_minutes
    next_time = now.replace(
        minute=0, second=0, microsecond=0
    ) + timedelta(minutes=next_min)

    sleep_seconds = (next_time - now).total_seconds()
    time.sleep(max(sleep_seconds, 1))

BUY_THRESHOLD = 0.60
SELL_THRESHOLD = 0.40
# =========================
# SINGLE LIVE RUN
# =========================
def run_once():
    # 1️⃣ Fetch live candles
    raw_df = fetch_latest_candles()

    # 2️⃣ Generate features
    feat_df = generate_features(raw_df)

    # 3️⃣ Latest candle only
    X_live = feat_df[config.FEATURE_COLS].tail(1)

    # 4️⃣ Predict
    prob_up = model.predict_proba(X_live)[0, 1]

    # 5️⃣ Signal logic (FROM CONFIG)
    if prob_up >= BUY_THRESHOLD:
        signal = "BUY"
        confidence = "HIGH"
        bias = "Bullish"
    elif prob_up <= SELL_THRESHOLD:
        signal = "SELL"
        confidence = "HIGH"
        bias = "Bearish"
    else:
        signal = "HOLD"
        confidence = "LOW"
        bias = "Neutral"

    # 6️⃣ Candle time
    candle_time = X_live.index[-1]

    # 7️⃣ Alert
    msg = (
    f"📊 BTCUSDT — LIVE (5m)\n\n"
    f"🕒 Candle (UTC): {candle_time}\n"
    f"📈 Probability Up: {prob_up*100:.2f}%\n"
    f"📉 Probability Down: {(1-prob_up)*100:.2f}%\n\n"
    f"🎯 Signal: {signal}\n"
    f"⚠️ Confidence: {confidence}\n"
    f"📊 Bias: {bias}"
)


    send_telegram_alert(msg)


# =========================
# CONTINUOUS SCHEDULER
# =========================
def run_forever():
    send_telegram_alert("🟢 Live trading scheduler STARTED")

    while True:
        try:
            wait_until_next_candle(INTERVAL_MINUTES)
            run_once()
        except Exception as e:
            send_telegram_alert(f"❌ Scheduler error:\n{e}")
            time.sleep(60)


# =========================
# CLI ENTRY
# =========================
if __name__ == "__main__":
    run_forever()
