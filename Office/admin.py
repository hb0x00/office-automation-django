from django.contrib import admin
from .models import Branch, Employee

# Register your models here.
admin.site.register([
    Branch, Employee
])
