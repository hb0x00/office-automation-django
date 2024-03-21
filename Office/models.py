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

