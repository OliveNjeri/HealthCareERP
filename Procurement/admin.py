from django.contrib import admin
from . models import Supplier, Supply, Purchase
# Register your models here.
admin.site.register(Supplier)
admin.site.register(Supply)
admin.site.register(Purchase)