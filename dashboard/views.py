import subprocess
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .telegram_bot import send_message
from django.http import FileResponse, HttpResponse

# Track local subprocesses (scheduler + crash monitor)
process_store = {
    "crash": None,
    "scheduler": None,
}

# 🌐 Dashboard
@login_required
def dashboard(request):
    return render(request, "dashboard.html")

# ⛏️ Start Mining on EC2
@login_required
def start_mining(request):
    subprocess.Popen([
        "ssh",
        "-i", "/Users/badboigibby/Downloads/gibson-key.pem",
        "ec2-user@18.222.21.80",
        "bash ~/start-mine.sh"
    ])
    send_message("✅ Gibson Miner started mining Monero remotely on EC2 🛠️")
    return redirect("dashboard")

# 🛑 Stop Mining on EC2
@login_required
def stop_mining(request):
    subprocess.call([
        "ssh",
        "-i", "/Users/badboigibby/Downloads/gibson-key.pem",
        "ec2-user@18.222.21.80",
        "kill $(cat ~/xmrig.pid)"
    ])
    send_message("🛑 Mining stopped on EC2. See you soon.")
    return redirect("dashboard")

# 📅 Start Local Scheduler
@login_required
def start_scheduler(request):
    if process_store["scheduler"] is None:
        process_store["scheduler"] = subprocess.Popen(["python3", "scheduler.py"])
    return redirect("dashboard")

# 🛑 Stop Scheduler
@login_required
def stop_scheduler(request):
    if process_store["scheduler"]:
        process_store["scheduler"].terminate()
        process_store["scheduler"] = None
    return redirect("dashboard")

# 🔒 Start Crash Monitor
@login_required
def start_crash_monitor(request):
    if process_store["crash"] is None:
        process_store["crash"] = subprocess.Popen(["python3", "crash_monitor.py"])
    return redirect("dashboard")

# 🛑 Stop Crash Monitor
@login_required
def stop_crash_monitor(request):
    if process_store["crash"]:
        process_store["crash"].terminate()
        process_store["crash"] = None
    return redirect("dashboard")

# 📊 View Hashrate Graph
def plot_graph(request):
    return render(request, 'plot_graph.html')

from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os

def graph_view(request):
    return render(request, 'graph.html')

def graph_image(request):
    image_path = '/home/ec2-user/minerportal/static/hashrate.png'
    if os.path.exists(image_path):
        return FileResponse(open(image_path, 'rb'), content_type='image/png')
    return HttpResponse("Image not found", status=404)
