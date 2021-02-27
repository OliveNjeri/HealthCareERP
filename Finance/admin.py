from django.contrib import admin
from .models import SalaryPayment, EmployeeSalary, HealthBill, FinanceOfficer
from . models import DrugSell, PurchasePayment
# Register your models here.
@admin.register(DrugSell)
class DrugSellAdmin(admin.ModelAdmin):
    list_display = ("sales_code", "amount", "submitted_by", "received_by", "sales_date", "date_submitted")
    filter_by = ("sales_date", "date_submitted")

@admin.register(FinanceOfficer)
class FinanceOfficerAdmin(admin.ModelAdmin):
    list_display = ("employee", "graduation_year", "shift", "last_university_attended", "specialization")

@admin.register(PurchasePayment)
class PurchasePaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_number", "purchase", "amount", "payment_approved_by", "paid_on")
    filter_by = ("paid_on")


@admin.register(HealthBill)
class HealthBillAdmin(admin.ModelAdmin):
    list_display = ("patient", "bill", "mode_of_payment", "received_by", "paid_on")
    filter_by = ("paid_on")


@admin.register(EmployeeSalary)
class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department', 'salary')
    filter_by = ('department')


@admin.register(SalaryPayment)
class SalaryPaymentAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "month", "year", "approved_by", "paid_on")
    filter_by = ("month", "year")
