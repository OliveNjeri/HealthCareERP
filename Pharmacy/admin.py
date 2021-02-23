from django.contrib import admin
from .models import Pharmacist, Drug, DrugSale
# Register your models here.
admin.site.register(Drug)
admin.site.register(DrugSale)
admin.site.register(Pharmacist)