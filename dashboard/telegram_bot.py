# dashboard/telegram_bot.py

import os
import time
from telegram import Bot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get token and chat ID from .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Initialize the bot
bot = Bot(token=TOKEN)
start_time = time.time()

# Send a basic message
def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

# Format uptime in hours and minutes
def format_uptime(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    return f"{hrs}h {mins}m"

# Estimate profit based on hashrate
def calculate_profit(hashrate_khs):
    monero_per_kh = 0.0000027  # Estimated Monero earned per KH/s
    usd_per_monero = 170.00    # Estimated USD per Monero
    return hashrate_khs * monero_per_kh * usd_per_monero

# Send real-time mining status
def send_mining_status(hashrate, total_hashes):
    uptime = format_uptime(time.time() - start_time)
    profit = calculate_profit(hashrate)

    message = f"""
🦹 <b>Mining Status</b>
--------------------------
📈 <b>Hashrate:</b> {hashrate:.2f} kH/s
🔁 <b>Total Hashes:</b> {total_hashes:,}
⏱️ <b>Uptime:</b> {uptime}
💰 <b>Estimated Profit:</b> ${profit:.2f}
"""
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="HTML")

# Send crash alert
def send_crash_alert():
    bot.send_message(chat_id=CHAT_ID, text="🚨 <b>Mining has stopped or crashed!</b>", parse_mode="HTML")

# Send daily mining summary
def send_daily_summary(hashrate, total_hashes):
    profit = calculate_profit(hashrate)
    message = f"""
📊 <b>Daily Summary</b>
--------------------------
📈 <b>Avg Hashrate:</b> {hashrate:.2f} kH/s
🔁 <b>Total Hashes:</b> {total_hashes:,}
💰 <b>Daily Profit:</b> ${profit:.2f}
"""
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="HTML")
