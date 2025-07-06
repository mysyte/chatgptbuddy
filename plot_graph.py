import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

LOG_FILE = "miner_logs.txt"

def extract_hashrate_from_line(line):
    if "kH/s" in line:
        try:
            parts = line.split()
            for part in parts:
                if "kH/s" in part:
                    return float(part.replace("kH/s", "").replace(",", ""))
        except:
            return None
    return None

def get_hashrate_data():
    hashrates = []
    with open(LOG_FILE, "r") as file:
        for line in file:
            rate = extract_hashrate_from_line(line)
            if rate is not None:
                hashrates.append(rate)
    return hashrates[-50:]  # Last 50 entries

def animate(i):
    data = get_hashrate_data()
    ax.clear()
    ax.plot(data)
    ax.set_title("Live Monero Hashrate")
    ax.set_ylabel("kH/s")
    ax.set_xlabel("Time")
    ax.grid(True)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, interval=3000)  # Every 3 seconds
plt.tight_layout()
plt.show()
