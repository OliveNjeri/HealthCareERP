from django.db import models
from django.utils import timezone
from Hospital.models import Doctor
from Patients.models import Patient
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

class LabTechnician(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    graduation_year = models.DateTimeField(default=timezone.now)
    last_university_attended = models.CharField(max_length=500)
    highest_education_level = models.CharField(max_length=50, choices=HIGHEST_EDUCATION_CHOICES)
    schools_attended = models.CharField(max_length=500)
    specialization = models.CharField(max_length=500)
    shift = models.CharField(max_length=50, choices=SHIFT_CHOICES)
    places_worked = models.TextField()

    def __str__(self):
        return self.employee.name 

    class Meta:
        verbose_name_plural = ("Lab Technicians")

class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sent_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_by = models.ForeignKey(LabTechnician, on_delete=models.CASCADE)
    test_date = models.DateTimeField()
    test_results = models.TextField()

    def __str__(self):
        return self.patient.name 

    class Meta:
        verbose_name_plural = ("Lab Tests")