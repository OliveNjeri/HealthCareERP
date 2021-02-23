from django.db import models
from django.utils import timezone
from Hospital.models import Doctor, Nurse, Ward
from HumanResource.models import Receiptionist
# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date_recorded = models.DateTimeField(default=timezone.now)
    postal_code = models.CharField(max_length=20)
    zip_code= models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_time = models.DateTimeField(default=timezone.now)
    visit_reason = models.TextField(default="Medical Checkup")
    recorded_by = models.ForeignKey(Receiptionist, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name

    class Meta:
        verbose_name = ("Patients Visits Detail")

class HealthHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    past_health_history = models.TextField(help_text="Describe your health history")

    def __str__(self):
        return self.patient.name

    class Meta:
        verbose_name = ("Patient Healthy History")
        verbose_name_plural = ("Patient Healthy Histories")

class PatientComment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment_on_service = models.TextField(help_text="what do you think about our services as a patient? ")
    recommend_us_to_others = models.TextField(help_text="Would you recommend us to other people? ")
    recommedations = models.TextField(help_text="What would you like us to improve on? ")  
    comment_date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.patient.name

    class Meta:
        verbose_name = ("Patient Comment") 

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_drug = models.CharField(max_length=500)
    prescribed_by = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_prescribed = models.DateTimeField(default=timezone.now)
    prescription_start_date = models.DateTimeField()
    prescription_end_date = models.DateTimeField()
    prescription_notes = models.TextField()

    def __str__(self):
        return self.patient.name + " " +self.prescribed_drug
    
    class Meta:
        verbose_name = ("Patients Drug Prescription")

class AdmittedPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    date_admitted = models.DateTimeField()

    def __str__(self):
        return self.patient.name

    class Meta:
        verbose_name = ("Admitted Patient")

class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    date_recorded = models.DateTimeField()

    def __str__(self):
        return self.patient.name

    class Meta:
        verbose_name = ("Patients Health Record")

class PatientDischarge(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    discharged_on = models.DateTimeField()

    def __str__(self):
        return self.patient.name + " " + self.discharged_on

    class Meta:
        verbose_name = ("Discharged Patient")
