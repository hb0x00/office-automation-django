from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from Office.forms import EmployeeForm, UserForm
from django.contrib.auth.models import User
from Office.models import Employee


# Create your views here.


def authLogin(req: HttpRequest) -> HttpResponse:
    """
    This function is a simple endpoint for the login process.
    It returns a HTTP response with a message "hello login" if the login is successful,
    otherwise it renders the login page with any error messages.

    Parameters:
    req (HttpRequest): The HTTP request object containing information about the request.

    Returns:
    HttpResponse: A HTTP response object containing the message "hello login" if the login is successful,
    otherwise it renders the login page with any error messages.
    """
    if req.method == "POST":
        usrname = req.POST.get("uname")
        passwd = req.POST.get("password")
        print(f"{usrname}, {passwd}")

        user = authenticate(req, username=usrname, password=passwd)
        if user is not None:
            login(req, user)
            print("user")
            return redirect("/dashboard")
    return render(req, "login.html")

def authEmployeeRegister(req: HttpRequest)->HttpResponse:
    """
    This function is responsible for handling the registration of an employee.
    It takes an HttpRequest object as input and returns an HttpResponse object.

    Parameters:
    req (HttpRequest): The HTTP request object containing information about the request.

    Returns:
    HttpResponse: A HTTP response object containing a redirect to the login page if the registration is successful, otherwise it renders the registration page with any error messages.

    The function first retrieves the POST data from the request object. It then creates instances of UserForm and EmployeeForm, passing the POST data to their constructors.

    If the request method is POST, the function proceeds to hash the password using the make_password function from Django's hashers module. It then checks if the UserForm and EmployeeForm instances are valid. If both forms are valid, it saves the User instance, creates an Employee instance, associates the two instances, and saves the Employee instance. Finally, it returns a redirect to the login page.

    If the request method is not POST, the function renders the registration page with the provided UserForm and EmployeeForm instances, along with any error messages.
    """
    post_data = req.POST.copy()
    u_form = UserForm(post_data) 
    e_form = EmployeeForm(post_data)  
    if req.method == "POST":
        post_data["password"] = make_password(req.POST["password"])
        if e_form.is_valid() and u_form.is_valid():
            u = u_form.save()
            e = e_form.save(commit=False)
            e.employee = u
            e.save()
            return redirect("/auth/login")
    return render(req, "register.html", {"e_form": e_form, "u_form": u_form})

def lgout(req):
    """
    This function is responsible for logging out the user from the system.

    Parameters:
    req (HttpRequest): The HTTP request object containing information about the request.

    Returns:
    None: This function does not return any value. It simply logs out the user and redirects to the home page.

    The function first calls the logout function from Django's authentication module, passing the request object as an argument. This function removes the user session and logs out the user.

    After logging out the user, the function returns a redirect to the home page using the redirect function from Django's shortcuts module. This redirects the user to the home page after logging out.
    """
    logout(req)
    return redirect("/")
