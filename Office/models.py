from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

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
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=256, unique=True)
    department = models.CharField(max_length=100)
    batch = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=13)
    fee_pay_status = models.PositiveSmallIntegerField(default=0)  # 0 for unpaid, 1 for paid
    fee_pay_date = models.DateField(null=True, blank=True)
    fee_pay_amount = models.PositiveSmallIntegerField(null=True, blank=True)

    @property
    def is_fee_paid(self):
        if self.fee_pay_status == 1:
            return True
        else:
            return False


    
    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = self.generate_unique_id('STU', 'Student')
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_id(prefix, model_name):
        while True:
            # Generate a new id.
            possible_id = prefix + '-' + get_random_string(7).upper()
            try:
                # Check that the id doesn't already exist in the database.
                Student.objects.get(student_id=possible_id)
            except Student.DoesNotExist:
                return possible_id
            
    
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")
        
    def __str__(self):
        return f"{self.user} ({self.department}, Batch {self.batch})"
    
    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})