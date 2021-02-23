from django.db import models
from HumanResource.models import Employee
from django.utils import timezone
# Create your models here.
HIGHEST_EDUCATION_CHOICES = (
    ("Bachelor's Degree", "Bachelor's Degree"),
    ("Masters Degree", "Masters Degree"),
    ("PhD", "PhD"),
)

SHIFT_CHOICES = (
    ("Morning", "Morning"),
    ("Evening", "Evening"),
    ("Day", "Day"),
    ("Night", "Night"),
)

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_office = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.department_name

class DepartmentDirector(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_appointed = models.DateTimeField()

    def __str__(self):
        return self.department.department_name + " Director"

    class Meta:
        verbose_name = ("Department Director") 
        verbose_name_plural = ("Department Directors") 

