from django.db import models
from HumanResource.models import Employee
from Staff.models import DepartmentDirector, Department
# Create your models here.
class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return self.employee.name +" Ksh. " +str(self.salary)

    class Meta:
        verbose_name_plural = ("Employees Salaries")

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