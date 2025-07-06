import os
import time
import psutil
from dashboard.telegram_bot import send_crash_alert

def is_process_running(process_name):
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            cmdline = proc.info.get('cmdline')
            if cmdline and process_name in ' '.join(cmdline):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False


def monitor_loop():
    while True:
        if not is_process_running("xmrig"):
            send_crash_alert()
            break  # Only alert once
        time.sleep(30)

if __name__ == "__main__":
    monitor_loop()
