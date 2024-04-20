from django.contrib import admin
from .models import Branch, Employee, LeaveRecord, Student



# Register your models here.
admin.site.register([
    Branch, Employee, LeaveRecord, Student
])
