"""
Runtime entrypoint for Crypto Market Opportunity Engine

This script:
- Loads environment variables
- Starts the live trading scheduler
- Keeps the process alive
"""

import sys
from pathlib import Path

# Ensure project root is in path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.live_scheduler import run_forever
from src.alerts import send_telegram_alert


def main():
    send_telegram_alert("🚀 Engine STARTED via logs/run.py")
    run_forever()


if __name__ == "__main__":
    main()


# To run the script, use the command:
# C:\Users\shubh\anaconda3\python.exe logs/run.py

# C:\Users\shubh\anaconda3\python.exe -m src.live_scheduler

