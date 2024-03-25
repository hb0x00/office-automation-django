from django import forms
from django.urls import reverse
from .models import Employee, LeaveRecord
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ("branch",
                   )

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "email")

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

class LeaveRecordForm(forms.ModelForm):
    leave_type = forms.CharField(max_length=100)
    leave_reason = forms.CharField(max_length=100)

    class Meta:
        model = LeaveRecord
        fields = ("leave_type", "leave_reason",)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form form-control'})
        }

    def __str__(self):
        return self.employee.user.username

    def get_absolute_url(self):
        return reverse("LeaveRecord_detail", kwargs={"pk": self.pk})
