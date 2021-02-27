from django.db import models
#from Staff.models import AdministrativeStaff
from django.utils import timezone
# Create your models here.
RELIGION_CHOICES = (
    ("Christian", "Christian"),
    ("Muslim", "Muslim"),
    ("Hindu", "Hindu"),
)
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)
SHIFT_CHOICES = (
    ("Morning", "Morning"),
    ("Evening", "Evening"),
    ("Day", "Day"),
    ("Night", "Night"),
)
HIGHEST_EDUCATION_CHOICES = (
    ("Bachelor's Degree", "Bachelor's Degree"),
    ("Masters Degree", "Masters Degree"),
    ("PhD", "PhD"),
)
DEPARTMENT_CHOICES = (
    ("Hospital", "Hospital"),
    ("Pharmacy", "Pharmacy"),
    ("Finance", "Finance"),
    ("Laboratory", "Laboratory"),
    ("Procurement", "Procurement"),
)
class Employee(models.Model):
    employment_number = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    department = models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    employment_date = models.DateTimeField()
    date_of_birth = models.DateTimeField()
    religion = models.CharField(max_length=200, choices=RELIGION_CHOICES)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    skin_color = models.CharField(max_length=200)
    hair_color = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    personal_description = models.TextField(max_length=2000)
    profile_photo = models.ImageField(upload_to="pics")
    last_university_attended = models.CharField(max_length=500)
    highest_education_level = models.CharField(max_length=50, choices=HIGHEST_EDUCATION_CHOICES)
    graduation_year = models.DateTimeField(default=timezone.now)
    schools_attended = models.CharField(max_length=500)
    specialization = models.CharField(max_length=500)
    places_worked = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Employee Detail")
        verbose_name_plural = ("Employees Details")

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.employee.name

    class Meta:
        verbose_name = ("Employees Checkin Record")
        verbose_name_plural = ("Employees Checkin Records")

class EmployeeCheckOut(models.Model):
    employee = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    check_out_time = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ("Employees Checkout Detail")
        verbose_name_plural = ("Employees Checkout Details")

class Suggestion(models.Model):
    issue_title = models.CharField(max_length=200)
    issue_description = models.TextField()
    report_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.issue_title

class JobApplication(models.Model):
    applicant_name = models.CharField(max_length=200)
    applicant_phone = models.CharField(max_length=200)
    applicant_email = models.EmailField()
    position = models.CharField(max_length=200)
    highest_education_level = models.CharField(max_length=200)
    education_specialization = models.CharField(verbose_name="Education Specialization", max_length=200)
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant_name

    class Meta:
        verbose_name = ("Job Application")
        verbose_name_plural = ("Job Applications")

class Receiptionist(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.CharField(max_length=200, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.employee.name

class Appointment(models.Model):
    requested_by = models.CharField(max_length=200)
    appointment_title = models.CharField(max_length=200)
    description = models.TextField()
    appointment_request_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.appointment_title

class ApprovedAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    appointed_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(Receiptionist, on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment.appointment_title

class PendingAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    why_not_approved = models.TextField()

    def __str__(self):
        return self.appointment.appointment_title

class EmployeeLeave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_request_date = models.DateTimeField(default=timezone.now)
    leave_reason = models.TextField()
    days_to_be_off = models.IntegerField(verbose_name="how many days do you want to off")
    approval_status = models.BooleanField(default=False)

    def __str__(self):
        return self.employee.name
    
    class Meta:
        verbose_name = ("Employees Leave Request")
        verbose_name_plural = ("Employees Leave Requests")

class FiredEmployee(models.Model):
    employee_name = models.CharField(max_length=200)
    employment_date = models.DateTimeField()
    position_worked = models.CharField(max_length=200)
    firing_date = models.DateTimeField(default=timezone.now)
    firing_reason = models.TextField()
    employee_comment = models.TextField()

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = ("Fired Employee")
        verbose_name_plural = ("Fired Employees")