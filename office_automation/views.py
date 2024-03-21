from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def dashboard(req: HttpRequest)-> HttpResponse:
    return render(req, "dashboard.html")
    # return 


def student_dashboard(req: HttpRequest)-> HttpResponse:
    return render(req, "student_dashboard.html")
    # return HttpResponse("hello student dashboard")

