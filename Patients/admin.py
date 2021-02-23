from django.contrib import admin
from .models import Patient, PatientComment, PatientVisit, HealthHistory, Prescription
from .models import HealthRecord, AdmittedPatient, PatientDischarge
# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientComment)
admin.site.register(PatientDischarge)
admin.site.register(AdmittedPatient)
admin.site.register(HealthRecord)

@admin.register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_time", "visit_reason", "recorded_by")
    search_fields = ["patient"]

@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "past_health_history")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("patient", "prescribed_drug", "prescribed_by", "prescription_start_date", "prescription_end_date", "prescription_notes")
