from django.db import models
from HumanResource.models import Employee
from Staff.models import DepartmentDirector, Department
from Patients.models import Patient
from Procurement.models import Purchase
from Pharmacy.models import Pharmacist
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
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return self.employee.name +" Ksh. " +str(self.salary)

    class Meta:
        verbose_name_plural = ("Employees Salaries")

class FinanceOfficer(models.Model):
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

    class Meta:
        verbose_name_plural = ("Finance Officers")

class SalaryPayment(models.Model):
    payment_number = models.CharField(max_length=100)
    name = models.ForeignKey(EmployeeSalary, on_delete=models.CASCADE)
    amount = models.FloatField()
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    approved_by = models.ForeignKey(DepartmentDirector, on_delete=models.CASCADE)
    paid_on = models.DateTimeField()

    def __str__(self):
        return self.payment_number

    class Meta:
        verbose_name_plural = ("Salaries Payments")

PAYMENT_CHOICES = (
    ("Cash Payment", "Cash Payment"),
    ("Wire Transfer", "Wire Transfer"),
    ("Cheque Payment", "Cheque Payment"),
    ("Mobile Money", "Mobile Money"),
)
class HealthBill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bill = models.FloatField()
    mode_of_payment = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    received_by = models.ForeignKey(FinanceOfficer, on_delete=models.CASCADE)
    paid_on = models.DateTimeField()

    class Meta:
        verbose_name_plural = ("Patients Bills")

class DrugSell(models.Model):
    sales_code = models.CharField(max_length=50)
    amount = models.FloatField()
    submitted_by = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    received_by = models.ForeignKey(FinanceOfficer, on_delete=models.CASCADE)
    sales_date = models.DateTimeField()
    date_submitted = models.DateTimeField()

    def __str__(self):
        return self.sales_code
    
    class Meta:
        verbose_name_plural = ("Drug Sales")

class PurchasePayment(models.Model):
    payment_number = models.CharField(max_length=50)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_approved_by = models.ForeignKey(DepartmentDirector, on_delete=models.CASCADE)
    paid_on = models.DateTimeField()

    def __str__(self):
        return self.payment_number + " " + self.purchase.item
