import subprocess
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .telegram_bot import send_message
import os, signal

process_store = {
    "crash": None,
    "scheduler": None,
}

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

# Already working:
@login_required
def start_mining(request):
    subprocess.Popen(["/bin/bash", "/Users/badboigibby/monero/start-mine.sh"])
    send_message("✅ Gibson Miner started mining Monero 🛠️")
    return redirect("dashboard")

@login_required
def stop_mining(request):
    subprocess.call(["pkill", "-f", "xmrig"])
    send_message("🛑 Mining stopped. See you soon.")
    return redirect("dashboard")

# 📆 Start Scheduler
@login_required
def start_scheduler(request):
    if process_store["scheduler"] is None:
        process_store["scheduler"] = subprocess.Popen(["python3", "scheduler.py"])
    return redirect("dashboard")

@login_required
def stop_scheduler(request):
    if process_store["scheduler"]:
        process_store["scheduler"].terminate()
        process_store["scheduler"] = None
    return redirect("dashboard")

# 🛑 Start Crash Monitor
@login_required
def start_crash_monitor(request):
    if process_store["crash"] is None:
        process_store["crash"] = subprocess.Popen(["python3", "crash_monitor.py"])
    return redirect("dashboard")

@login_required
def stop_crash_monitor(request):
    if process_store["crash"]:
        process_store["crash"].terminate()
        process_store["crash"] = None
    return redirect("dashboard")

def plot_graph(request):
    return render(request, 'plot_graph.html')
