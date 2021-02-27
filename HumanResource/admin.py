from django.contrib import admin
from . models import Employee, Attendance, Suggestion, JobApplication, EmployeeCheckOut
from .models import Receiptionist, PendingAppointment, FiredEmployee, Appointment, ApprovedAppointment, EmployeeLeave
# Register your models here.
admin.site.register(Attendance)
admin.site.register(Suggestion)
admin.site.register(JobApplication)
admin.site.register(Receiptionist)
admin.site.register(ApprovedAppointment)
admin.site.register(PendingAppointment)

@admin.register(EmployeeLeave)
class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ("employee", "leave_request_date", "leave_reason", "approval_status")
    list_filter = ['approval_status']
    actions = ['approve_leave_request', 'decline_leave_request']

    def approve_leave_request(self, request, queryset):
        queryset.update(approval_status=True)

    def decline_leave_request(self, request, queryset):
        queryset.update(approval_status=False)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "phone", "gender", "employment_date", "city", "country")
    list_filter = ("gender", "employment_date",)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(EmployeeCheckOut)
class EmployeeCheckOutAdmin(admin.ModelAdmin):
    list_display = ("employee", "check_out_time")

admin.site.site_header = "HEALTHCARE ERP"

@admin.register(FiredEmployee)
class FiredEmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "employment_date", "position_worked", "firing_date", "firing_reason", "employee_comment")
    filter_by = ("firing_date")
    search_fields = ["employee_name"]
    filter_fields = ['firing_date']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("requested_by", "appointment_title", "description", "appointment_request_date", "approved")
    list_filter = ("approved",)
    actions = ['approve_appointment']

    def approve_appointment(self, request, queryset):
        queryset.update(approved=True)

