from django.contrib import admin
from . models import LabTechnician, LabTest
# Register your models here.
@admin.register(LabTechnician)
class LabTechnicianAdmin(admin.ModelAdmin):
    list_display = ("employee", "graduation_year", "highest_education_level", "specialization", "shift")
    filter_by = ("shift")

@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ("patient", "sent_by", "test_by", "test_date", "test_results")
    filter_by = ("test_date")

