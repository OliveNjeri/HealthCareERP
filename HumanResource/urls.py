from django.urls import path
from . import views


urlpatterns = [
    path("", views.EmployeeList.as_view(), name="employees"),
    path("employees_list/", views.EmployeesList.as_view(), name="employees_list"),
    path("<int:id>/", views.employee_details, name="employee_details"),
    path("appointments/", views.appointments, name="appointments"),
    path("attendance/", views.attendance, name="attendance"),
    path("fired_employees/", views.FiredEmployeeList.as_view(), name="fired_employees"),
    path("fired_employees_details/<int:id>/", views.fired_employees_details, name="fired_employees_details"),
    path("employee_checkout/", views.employee_checkout, name="employee_checkout"),
    path("employee_checkout_details/<int:id>/", views.employees_checkout_details, name="employees_checkout_details"),
    path("job_applications/", views.job_applications, name="job_applications"),
    path("suggestions/", views.suggestions, name="suggestions"),
    path("suggestion_details/<int:id>/", views.suggestion_details, name="suggestion_details"),
    path("employee_leave/", views.EmployeeLeaveList.as_view(), name="employee_leave"),
    path("leave_details/<int:id>/", views.leave_details, name="leave_details"),
    path("job_applications/", views.job_applications, name="job_applications"),
    path("job_application_details/<int:id>/", views.job_application_details, name="job_application_details"),
]