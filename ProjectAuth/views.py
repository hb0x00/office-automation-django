from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def authHome(req: HttpRequest) -> HttpResponse:
    return HttpResponse("hello auth")

def signup(req: HttpRequest)-> HttpResponse:
    return HttpResponse("hello signup")

def login(req: HttpRequest)-> HttpResponse:
    return render(req, "login.html")