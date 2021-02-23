from django.contrib import admin
from .models import Doctor, Nurse, Psychiatrist, Consultant, Department, DepartmentChairperson, Ward
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Psychiatrist)
admin.site.register(Ward)
admin.site.register(Consultant)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_name", "department_office", "number_of_workers")


@admin.register(DepartmentChairperson)
class DepartmentChairpersonAdmin(admin.ModelAdmin):
    list_display = ("chairperson", "department", "date_appointed")
