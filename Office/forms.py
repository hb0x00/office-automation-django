from django import forms
from .models import Employee
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
