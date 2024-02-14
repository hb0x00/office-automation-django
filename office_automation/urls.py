from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def base(req):
    return render(req, "base.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("ProjectAuth.urls")),
    path("", base, name="")
]
