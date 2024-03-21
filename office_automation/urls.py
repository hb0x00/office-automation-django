from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

def base(req):
    return render(req, "base.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("ProjectAuth.urls")),
    path("dashboard/", views.dashboard, name=""),
    path("student/dashboard/", views.student_dashboard, name=""),
    path("", base, name="")
]
