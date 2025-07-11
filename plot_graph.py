import matplotlib.pyplot as plt
import re
import os

def extract_hashrates(filename):
    hashrates = []
    with open(filename, 'r') as file:
        for line in file:
            # match the line pattern with 10s hashrate only (first number after "15m")
            match = re.search(r"15m\s+([0-9.]+)", line)
            if match:
                hashrate = float(match.group(1))
                hashrates.append(hashrate)
    return hashrates

def plot():
    data = extract_hashrates("miner_logs.txt")
    if not data:
        print("❌ No data to plot.")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(data, marker='o', linestyle='-', color='green')
    plt.title("Miner Hashrate (15m average)")
    plt.xlabel("Log Entry")
    plt.ylabel("Hashrate (H/s)")
    plt.grid(True)
    plt.tight_layout()

    output_path = "/home/ec2-user/minerportal/static/hashrate.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print("✅ Graph saved to", output_path)

plot()
