import time
import psutil
import matplotlib.pyplot as plt
from datetime import datetime

hashrate_log = []
timestamps = []

def get_hashrate():
    # Simulated dummy hashrate — replace with real method if available
    return 320.0 + (5 - time.time() % 10)  # Fluctuating sample

def log_hashrate():
    while True:
        hr = get_hashrate()
        hashrate_log.append(hr)
        timestamps.append(datetime.now().strftime('%H:%M:%S'))

        print(f"[{timestamps[-1]}] Hashrate: {hr:.2f} kH/s")

        # Save graph every 30 points (~5 minutes if interval is 10s)
        if len(hashrate_log) >= 30:
            save_plot()

        time.sleep(10)

def save_plot():
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps[-30:], hashrate_log[-30:], marker='o')
    plt.xticks(rotation=45)
    plt.ylabel("kH/s")
    plt.title("Monero Hashrate (Live)")
    plt.tight_layout()
    plt.savefig("hashrate_plot.png")
    plt.close()
