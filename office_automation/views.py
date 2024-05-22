from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from Office.forms import tbl_leave_apply as  LeaveRecordForm
from Office.models import tbl_leave_apply as LeaveRecord
from Office.models import tbl_employee as Employee
from django.contrib.auth.models import User
import random

def dashboard(req: HttpRequest)-> HttpResponse:
    """
    This function handles the dashboard view for the application.
    It processes POST requests to create a new leave record and
    returns a render of the dashboard.html template with the appropriate data.

    Args:
    req (HttpRequest): The HTTP request object containing the user's input.

    Returns:
    HttpResponse: A rendered HTML response containing the dashboard view.

    Raises:
    Exception: If there is an error creating the leave record.

    """
    if req.method == 'POST':
        leave_type = req.POST.get("leave_type")
        employee = req.POST.get("e_id")
        start_date = req.POST.get("start")
        end_date = req.POST.get("end")
        month = req.POST.get("month")
        year =req.POST.get("year")
        number_of_leave_taken = req.POST.get("no")
        print(leave_type, employee, start_date, end_date, month, year, number_of_leave_taken)
        e_id = Employee.objects.get(employee = User.objects.get(id=req.user.id)).emp_id
        employee = Employee.objects.get(emp_id = employee)

        try:
            obj = LeaveRecord.objects.create(
                leave_type=leave_type,
                employee=employee, 
                start_date=start_date, 
                end_date=end_date, 
                month=month, 
                year=year, 
                number_of_leave_taken=number_of_leave_taken
            )

            employee = User.objects.get(id=req.user.id)
            employee = Employee.objects.get(employee=employee)

            return redirect("/leave_record")
        except Exception as e:
            # Handle the exception and return an appropriate error response
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

    l_form = LeaveRecordForm()
    u = User.objects.get(username=req.user)
    employee = Employee.objects.get(employee=u)
    leave_record = LeaveRecord.objects.filter(employee=employee)

    return render(req, "dashboard.html", {"form": type(l_form), "leave_record": leave_record, 
                                        #   "leave_left": leave_left
                                          })



def student_dashboard(req: HttpRequest)-> HttpResponse:
    return render(req, "student_dashboard.html")



def leave_record(req: HttpRequest)-> HttpResponse:
    """
    This function handles the view for displaying all leave records.

    Args:
    req (HttpRequest): The HTTP request object containing the user's input.

    Returns:
    HttpResponse: A rendered HTML response containing the leave_record view.

    Raises:
    None

    """
    data = LeaveRecord.objects.all()
    return render(req, "leave_record.html", {"data": data})

def admin_dashboard(req: HttpRequest) -> HttpResponse:
    """
    This function handles the admin dashboard view for the application.
    It checks if the user is a superuser and redirects them to the appropriate URL.
    If the user is not a superuser, it returns a response indicating that they do not have permission.

    Args:
    req (HttpRequest): The HTTP request object containing the user's input.

    Returns:
    HttpResponse: A redirect response if the user is a superuser, or a response indicating that the user does not have permission.

    Raises:
    None

    """
    if req.user.is_superuser:
        return redirect("admin:Office:tbl_leave_apply:list")
    else:
        return HttpResponse("You have no permission to go "\
                            "please login <a href='/auth/login'>here</a>...")

