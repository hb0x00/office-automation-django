from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from Office.forms import LeaveRecordForm
from Office.models import LeaveRecord
from Office.models import Employee
from django.contrib.auth.models import User
import random

def dashboard(req: HttpRequest)-> HttpResponse:
    # validate and render LeaveRecordForm
    if req.method == 'POST':
        leave_reason = req.POST.get("leave_reason")
        leave_type = req.POST.get("leave_type")
        print(type(req.user.id))
        employee = User.objects.get(id=req.user.id)
        employee = Employee.objects.get(user=employee)

        print(leave_type, leave_reason, employee)
        db_entry = LeaveRecord.objects.create(leave_reason=leave_reason, employee=employee, leave_type=leave_type)
        db_entry.save()

        return  HttpResponse("sucess.......")

        l_form = LeaveRecordForm(data)
        print(l_form.data)
        if l_form.is_valid():
            l_form.save()
            return HttpResponse("successsssxsssssss")
        else:
            print(l_form.errors)
            return HttpResponse(l_form.errors)
        
    l_form = LeaveRecordForm()
    u = User.objects.get(username=req.user)
    employee = Employee.objects.get(user=u)
    leave_record = LeaveRecord.objects.filter(employee=employee)
    leave_left_obj = random.choice(leave_record)
    leave_left = leave_left_obj.leave_left
    return render(req, "dashboard.html", {"form": l_form, "leave_record": leave_record, 
                                          "leave_left": leave_left
                                          })
    # return HttpResponse("hello dashboard")

# def leave_record(request):

    return render(req, "dashboard.html")
    # return 


def student_dashboard(req: HttpRequest)-> HttpResponse:
    return render(req, "student_dashboard.html")
    # return HttpResponse("hello student dashboard")

