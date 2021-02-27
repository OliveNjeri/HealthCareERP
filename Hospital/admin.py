from django.contrib import admin
from .models import Doctor, Nurse, Psychiatrist, Consultant
from . models import Department, DepartmentChairperson, Ward
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("employee", "graduation_year", "highest_education_level", "specialization")
    
@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ("employee", "graduation_year", "highest_education_level", "specialization")
    
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ("ward_number", "department", "capacity", "occupied_capacity", "nurse_on_duty")
    filter_by = ("department", "occupation_status")
    
@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ("employee", "graduation_year", "highest_education_level", "specialization")

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_name", "department_office", "number_of_workers")

@admin.register(DepartmentChairperson)
class DepartmentChairpersonAdmin(admin.ModelAdmin):
    list_display = ("chairperson", "department", "date_appointed")
