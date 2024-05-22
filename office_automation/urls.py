# routing file that makes initial routes of the project

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views
from ProjectAuth.views import lgout

def base(req):
    return render(req, "index.html")

# initial routing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("ProjectAuth.urls")),
    path("dashboard/", views.dashboard, name=""),
    path("student/dashboard/", views.student_dashboard, name=""),
    path("", base, name=""),
    path("leave_record/", views.leave_record),
    path("admin_dashboard", views.admin_dashboard),
    path("logout", lgout)
]

admin.site.site_header = 'Office Automation'
admin.site.index_title = 'Features area'
