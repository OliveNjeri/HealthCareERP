from django.contrib import admin
from . models import Department, DepartmentDirector
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_name", "department_office", "number_of_employees", "description")



admin.site.register(DepartmentDirector)
