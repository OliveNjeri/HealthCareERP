from django.db import models
from django.utils import timezone
from HumanResource.models import Employee
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

class CommonInfo(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    graduation_year = models.DateTimeField(default=timezone.now)
    last_university_attended = models.CharField(max_length=500)
    highest_education_level = models.CharField(max_length=50, choices=HIGHEST_EDUCATION_CHOICES)
    schools_attended = models.CharField(max_length=500)
    specialization = models.CharField(max_length=500)
    places_worked = models.TextField()

    class Meta:
        abstract = True

class Department(models.Model):
    department_name = models.CharField(max_length=200)
    department_office = models.CharField(max_length=200)
    number_of_workers = models.IntegerField()
    
    def __str__(self):
        return self.department_name

class DepartmentChairperson(models.Model):
    chairperson = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE, null=True)
    date_appointed = models.DateTimeField()
    
    def __str__(self):
        return self.department.department_name + " Chairperson"

    class Meta:
        verbose_name = ("Department Chairperson")

class Doctor(CommonInfo):

    def __str__(self):
        return self.employee.name

class Nurse(CommonInfo):

    def __str__(self):
        return self.employee.name

class Consultant(CommonInfo):
  
    def __str__(self):
        return self.employee.name

class Psychiatrist(CommonInfo):

    def __str__(self):
        return self.employee.name

OCCUPATION_CHOICES = (
    ("Fully Occupied", "Fully Occupied"),
    ("Not Fully Occupied", "Not Fully Occupied"),
    ("Empty", "Empty"),
)

class Ward(models.Model):
    ward_number = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    occupied_capacity = models.IntegerField()
    occupation_status = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)
    nurse_on_duty = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return self.ward_number

