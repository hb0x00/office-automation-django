from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

LeaveRecord = None
Employee = None

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

# model for employee
class tbl_employee(models.Model):
    # columns
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=60, choices=(
        ('computer engineering', 'computer engineering'),
        ('mechanical engineering', 'mechanical engineering'),
        ('electrical engineering', 'electrical engineering'),
        ('electronics and communication engineering', 'electronics and communication engineering'),
    ))
    emp_id = models.IntegerField(primary_key=True)
    email_id = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=13, null=True, blank=True)
    designation = models.CharField(max_length=100, choices=(
        ('Senior lecturer','Senior lecturer'),
        ('lecturer','lecturer'),
        ('HOD','HOD'),
    ), null=True, blank=True)

    # to rander properly in admin
    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.employee.username

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.emp_id})

# model to store employee leave record
class tbl_leave_type(models.Model):
    leave_id = models.IntegerField(primary_key=True)
    leave_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("tbl_leave_type")
        verbose_name_plural = ("tbl_leave_types")

    def __str__(self):
        """
        Returns a string representation of the leave type.

        Parameters:
        self (tbl_leave_type): The instance of the tbl_leave_type model.

        Returns:
        str: The name of the leave type.
        """
        return self.leave_name

    def get_absolute_url(self):
        """
        Returns the URL for the detail view of the tbl_leave_type instance.

        Parameters:
        self (tbl_leave_type): The instance of the tbl_leave_type model.

        Returns:
        str: The URL for the detail view of the tbl_leave_type instance.
        """
        return reverse("tbl_leave_type_detail", kwargs={"pk": self.leave_id})


# apply for leave
class tbl_leave_apply(models.Model):
    leave_type = models.CharField(max_length=100, 
        null=True, blank=True
    )
    employee = models.ForeignKey(tbl_employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    number_of_leave_taken = models.IntegerField()
    approved = models.BooleanField(default=False)    

    class Meta:
        verbose_name = ("tbl_leave_apply")
        verbose_name_plural = ("tbl_leave_apply")

    def __str__(self):
        """
        Returns a string representation of the leave apply instance.

        Parameters:
        self (tbl_leave_apply): The instance of the tbl_leave_apply model.

        Returns:
        str: A string containing the employee's name, start date of leave, and approval status.
        """
        return str(self.employee) + " " + str(self.start_date)[:10] + " Approved Status: " + str(self.approved)

    def get_absolute_url(self):
        """
        Returns the URL for the detail view of the tbl_leave_apply instance.

        Parameters:
        self (tbl_leave_apply): The instance of the tbl_leave_apply model.

        Returns:
        str: The URL for the detail view of the tbl_leave_apply instance.
        """
        return reverse("tbl_leave_apply_detail", kwargs={"pk": self.pk})




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