from django.contrib import admin
from . models import Employee, Attendance, Suggestion, JobApplication, EmployeeCheckOut
from .models import Receiptionist, PendingAppointment, FiredEmployee, Appointment, ApprovedAppointment, EmployeeLeave
# Register your models here.
admin.site.register(Attendance)
admin.site.register(Suggestion)
admin.site.register(JobApplication)
admin.site.register(Receiptionist)
admin.site.register(Appointment)
admin.site.register(ApprovedAppointment)
admin.site.register(PendingAppointment)
admin.site.register(EmployeeLeave)
admin.site.register(FiredEmployee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "phone", "gender", "employment_date", "city", "country")


@admin.register(EmployeeCheckOut)
class EmployeeCheckOutAdmin(admin.ModelAdmin):
    list_display = ("employee", "check_out_time")

admin.site.site_header = "HEALTHCARE ERP"
