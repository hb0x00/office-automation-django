from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def authHome(req: HttpRequest) -> HttpResponse:
    return HttpResponse("hello auth")