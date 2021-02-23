from django.db import models
from Procurement.models import Supplier
from HumanResource.models import Employee
from Patients.models import Prescription
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

class Pharmacist(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    graduation_year = models.DateTimeField(default=timezone.now)
    last_university_attended = models.CharField(max_length=500)
    highest_education_level = models.CharField(max_length=50, choices=HIGHEST_EDUCATION_CHOICES)
    shift = models.CharField(max_length=50, choices=SHIFT_CHOICES)
    schools_attended = models.CharField(max_length=500)
    specialization = models.CharField(max_length=500)
    places_worked = models.TextField()

    def __str__(self):
        return self.employee.name

class Drug(models.Model):
    name = models.CharField(max_length=500)
    received_quantity = models.FloatField()
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_received = models.DateTimeField(default=timezone.now)
    received_by = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DrugSale(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    buyer_name = models.CharField(max_length=200, null=True, blank=True)
    buyer_id = models.CharField(max_length=200, null=True, blank=True)
    sale_time = models.DateTimeField()
    quantity_sold = models.FloatField()
    unit_price = models.FloatField()
    total_price = models.FloatField()
    sold_by = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)

    def __str__(self):
        return self.drug.name + " , "+ self.prescription

    class Meta:
        verbose_name = ("Drugs Sale")