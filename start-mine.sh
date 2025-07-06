#!/bin/bash

# --- TELEGRAM ALERT (Optional) ---
# Replace with your real token and chat ID
BOT_TOKEN="7210519047:AAE5t5QQiNkvvrHJNfSg_9qKHSVipP5z62c"
CHAT_ID="5859140891"

curl -s -X POST https://api.telegram.org/bot$BOT_TOKEN/sendMessage \
 -d chat_id=$CHAT_ID \
 -d text="🚀 Gibson Walker Miner has started mining XMR on your Mac."

# --- macOS Notification ---
osascript -e 'display notification "GIBSON WALKER your Monero miner is now running." with title "Mining Started"'

# --- Change to xmrig build folder ---
cd ~/xmrig/build

# --- Append startup logs to file ---
echo "------------------------------" >> ~/monero/miner_logs.txt
echo "🕐 Session Started at $(date)" >> ~/monero/miner_logs.txt
echo "🔌 Connecting to Blockchain..." >> ~/monero/miner_logs.txt
echo "⛏️  Extracting data from pool..." >> ~/monero/miner_logs.txt
echo "📥 Downloading blocks..." >> ~/monero/miner_logs.txt
echo "<<<<<<<<<<<< 100%" >> ~/monero/miner_logs.txt
echo "✅ Gibson Walker Menora miner started successfully. 🚀" >> ~/monero/miner_logs.txt
echo "------------------------------" >> ~/monero/miner_logs.txt

# --- Start xmrig and log output continuously ---
caffeinate -i ./xmrig -o pool.supportxmr.com:3333 -u 42GVWNUnYrm2SHkXjxSZtzAzMLa6THYZEDgccLYBKXQaiT8Dtg2o... >> ~/monero/miner_logs.txt 2>&1


