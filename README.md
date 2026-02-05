# 🚀 Crypto Market Opportunity Engine (V1)

A **V1 rule-guided machine learning engine** that analyzes crypto market data, applies feature engineering and a single predictive model, and generates **risk-filtered trade signals**.

This version focuses on **clarity, explainability, and a solid baseline**, rather than complex automation.

---

## 📌 Problem Statement

Crypto markets are noisy and highly volatile.  
Naive trading signals often lead to:
- Overtrading
- False positives
- Poor risk control

**Objective (V1):**  
Build a clean and interpretable opportunity engine that:
- Converts raw market data into meaningful features
- Uses a single ML model for prediction
- Applies rule-based risk filtering
- Produces controlled and explainable signals

---

## 🧠 V1 Design Philosophy

V1 intentionally prioritizes:
- Simplicity over complexity  
- Explainability over black-box models  
- Rule-guided ML over full automation  

This makes the system easier to debug, safer to operate, and easier to extend in future versions.

> Advanced concepts like model ensembles, regime detection, and confidence voting are **out of scope for V1**.

---

## 🏗️ V1 System Flow

Market Data (OHLCV)
↓
Feature Engineering
↓
Single ML Model
↓
Rule-Based Risk Gate
↓
Signal Generation
↓
Telegram Alert Delivery



---

## ⚙️ Core Components (V1)

### 1️⃣ Feature Engineering
Transforms OHLCV data into:
- Returns
- Rolling statistics
- Volatility measures
- Momentum indicators

---

### 2️⃣ Single Machine Learning Model
- One supervised ML model
- Trained on engineered features
- Optimized for interpretability and speed
- Outputs directional or probability-based signals

---

### 3️⃣ Risk Gate (Rule-Based)
Signals are filtered using:
- Volatility thresholds
- Basic market stability checks

This prevents trading during highly unstable market conditions.

---

### 4️⃣ Alert Engine (Telegram Integration)
- Generates final trade signals after risk filtering
- Sends alerts via **Telegram Bot**
- Keeps alert delivery logic decoupled from model logic
- Designed for simple, real-time signal notification

Telegram is used in V1 as a lightweight alerting mechanism, not as a full monitoring system.

---

## 🔐 Environment & Security

Sensitive credentials are never committed to the repository.

- `.env` → local only (git ignored)
- `.env.example` → documents required variables

Example `.env.example`:
```env
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
