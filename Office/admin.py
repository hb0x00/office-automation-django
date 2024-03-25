from django.contrib import admin
from .models import Branch, Employee, LeaveRecord



# Register your models here.
admin.site.register([
    Branch, Employee, LeaveRecord
])
