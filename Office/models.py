from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):

    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("branch")
        verbose_name_plural = ("branches")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("branch_detail", kwargs={"pk": self.pk})


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})

# model to store employee leave record
class LeaveRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # get employee set as the user who is logged in
    leave_type = models.CharField(max_length=100)
    leave_date = models.DateField(auto_now_add=True)
    leave_reason = models.CharField(max_length=100)
    leave_left = models.IntegerField(null=True, default=4)

    class Meta:
        verbose_name = ("Leave Record")
        verbose_name_plural = ("Leave Records")

    def __str__(self):
        return str(self.leave_date)

    def get_absolute_url(self):
        return reverse("LeaveRecord_detail", kwargs={"pk": self.pk})
    

# model form to get leave record through user input



# model to store employee attendance record
class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_date = models.DateField(auto_now_add=True)
    attendance_status = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Attendance Record")
        verbose_name_plural = ("Attendance Records")

    def __str__(self):
        return self.employee.user.username

    def get_absolute_url(self):
        return reverse("AttendanceRecord_detail", kwargs={"pk": self.pk})