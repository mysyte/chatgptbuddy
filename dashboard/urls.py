from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("start/", views.start_mining, name="start_mining"),
    path("stop/", views.stop_mining, name="stop_mining"),
    path("scheduler/start/", views.start_scheduler, name="start_scheduler"),
    path("scheduler/stop/", views.stop_scheduler, name="stop_scheduler"),
    path("crash/start/", views.start_crash_monitor, name="start_crash"),
    path("crash/stop/", views.stop_crash_monitor, name="stop_crash"),
    path("graph/", views.plot_graph, name="plot_graph"),

]
