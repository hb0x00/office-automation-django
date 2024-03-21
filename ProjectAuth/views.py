from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from Office.forms import EmployeeForm, UserForm
from django.contrib.auth.models import User
from Office.models import Employee
# Create your views here.


def authHome(req: HttpRequest) -> HttpResponse:
    return HttpResponse("hello auth")

def signup(req: HttpRequest)-> HttpResponse:
    return HttpResponse("hello signup")

def authLogin(req: HttpRequest)-> HttpResponse:
    if req.method == "POST":
        usrname = req.POST.get("uname")
        passwd = req.POST.get("password")
        print(f"{usrname}, {passwd}")

        user = authenticate(req, username=usrname, password=passwd)
        if user is not None:
            login(req, user)
            print("user")
            return HttpResponse("sucesssssxsssssss")
    return render(req, "login.html")

def authEmployeeRegister(req: HttpRequest)->HttpResponse:
    u_form = UserForm(req.POST)
    e_form = EmployeeForm(req.POST)
    if req.method == "POST":
        # u_form.save()
        print(e_form.is_valid(), u_form.is_valid())
        if e_form.is_valid() and u_form.is_valid():
            u = u_form.save()
            e = e_form.save(commit=False)
            e.user = u
            e.save()
            return HttpResponse("success") 


        print(e_form.data, u_form.data)

    return render(req, "register.html", {"e_form": e_form, "u_form": u_form})
