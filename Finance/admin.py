from django.contrib import admin
from .models import SalaryPayment, EmployeeSalary
# Register your models here.
admin.site.register(EmployeeSalary)

@admin.register(SalaryPayment)
class SalaryPaymentAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "month", "year", "approved_by", "paid_on")
    filter_by = ("month", "year")
