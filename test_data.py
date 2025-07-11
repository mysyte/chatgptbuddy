import re

with open("miner_logs.txt", "r") as file:
    for line in file:
        match = re.search(r"15m\s+([0-9.]+)", line)
        if match:
            print(float(match.group(1)))
