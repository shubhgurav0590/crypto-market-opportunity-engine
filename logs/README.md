# Crypto Market Opportunity Engine — Runtime Guide

This folder contains everything required to RUN the live trading system.

---

## 📁 Folder Purpose

The `logs/` folder is responsible for:
- Starting the live scheduler
- Managing runtime dependencies
- Providing operational instructions
- Storing runtime logs

---

## ✅ Prerequisites

1. Python 3.10+ (recommended: Anaconda)
2. Telegram Bot Token & Chat ID
3. Binance API access (public data only)

---

## 🔐 Environment Variables

Create a `.env` file at PROJECT ROOT:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here



<!-- install dependencies -->
<!-- pip install -r logs/requirements.txt -->

 To run the script, use the command:
# C:\Users\shubh\anaconda3\python.exe logs/run.py

# C:\Users\shubh\anaconda3\python.exe -m src.live_scheduler
 -->