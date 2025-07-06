import time
from apscheduler.schedulers.background import BackgroundScheduler
from dashboard.telegram_bot import send_daily_summary

# Dummy values — replace with real-time logic if available
def job_daily_summary():
    hashrate = 325.4  # Replace with actual average
    total_hashes = 8342822  # Replace with actual value
    send_daily_summary(hashrate, total_hashes)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_daily_summary, 'cron', hour=0, minute=0)  # 12:00 AM
    scheduler.start()
    print("✅ Daily scheduler started.")

    # Keep process running
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
