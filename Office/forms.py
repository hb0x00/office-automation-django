from django import forms
from django.urls import reverse
from .models import Employee, LeaveRecord, tbl_employee, tbl_leave_apply
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = tbl_employee
        # fields = "__all__"
        fields = ("contact_number", "designation", "branch", "emp_id")

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password")

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

