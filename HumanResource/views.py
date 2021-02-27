from django.shortcuts import render
from django.views import generic  
from . models import Employee, Appointment, FiredEmployee, JobApplication, EmployeeCheckOut, Attendance
from . models import  Suggestion, EmployeeLeave
# Create your views here.
class EmployeeList(generic.ListView):
    queryset = Employee.objects.all()
    template_name = "hr/employees.html"

class EmployeesList(generic.ListView):
    queryset = Employee.objects.all()
    template_name = "hr/employees_list.html"

def employee_details(request, id):
    employee = Employee.objects.get(pk=id)
    context = {
        "employee": employee
    }
    return render(request, "hr/employee_details.html", context)

def attendance(request):
    attendances = Attendance.objects.all()
    context = {
        "attendances": attendances
    }
    return render(request, "hr/checkin.html", context)

class FiredEmployeeList(generic.ListView):
    queryset = FiredEmployee.objects.all()
    template_name = "hr/fired_employees.html"

def fired_employees_details(request, id):
    fired_employee = FiredEmployee.objects.get(pk=id)
    context = {
        "fired_employee": fired_employee
    }
    return render(request, "hr/fired_employee_details.html", context)

def employee_checkout(request):
    employee_checkouts = EmployeeCheckOut.objects.all()
    context = {
        "employee_checkouts": employee_checkouts
    }
    return render(request, "hr/checkout.html", context)

def employees_checkout_details(request, id):
    employee_checkout = EmployeeCheckOut.objects.get(pk=id)
    context = {
        "employee_checkout": employee_checkout
    }
    return render(request, "hr/employee_checkout_details.html", context)

def job_applications(request):
    job_applications = JobApplication.objects.all()
    context = {
        "job_applications": job_applications
    }
    return render(request, "hr/job_applications.html", context)

def suggestions(request):
    suggestions = Suggestion.objects.all()
    context = {
        "suggestions": suggestions
    }
    return render(request, "hr/suggestions.html", context)

def suggestion_details(request, id):
    suggestion = Suggestion.objects.get(pk=id)
    context = {
        "suggestion": suggestion
    }
    return render(request, "hr/suggestion_details.html", context)

def appointments(request):
    appointments = Appointment.objects.all()
    context = {
        "appointments": appointments
    }
    return render(request, "hr/appointments.html", context)

class EmployeeLeaveList(generic.ListView):
    queryset = EmployeeLeave.objects.all()
    template_name = "hr/leave_requests.html"

def leave_details(request, id):
    employee_leave = EmployeeLeave.objects.get(pk=id)
    context = {
        "employee_leave": employee_leave
    }
    return render(request, "hr/leave_details.html", context)
"""
class JobApplicationList(generic.ListView):
    queryset = JobApplication.objects.all()
    template_name = "hr/job_applications.html"
"""

def job_application(request):
    job_applications = JobApplication.objects.all()
    context = {
        "job_applications": job_applications
    }
    return render(request, "hr/job_applications.html", context)

def job_application_details(request, id):
    application = JobApplication.objects.get(pk=id)
    context = {
        "application": application
    }
    return render(request, "hr/job_application_details.html", context)