from django.contrib import admin
from .models import Branch, Employee, Student, tbl_leave_type, tbl_employee, tbl_leave_apply



# Register your models here.
admin.site.register([
    Branch, Student, tbl_leave_type, tbl_employee, tbl_leave_apply,
])
