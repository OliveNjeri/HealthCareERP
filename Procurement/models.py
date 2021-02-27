from django.db import models
from Staff.models import DepartmentDirector
from Hospital.models import DepartmentChairperson
# Create your models here.
CONTRACT_CHOICES = (
    ("Permanent Supplier", "Permanent Supplier"), 
    ("Temporary Supplier", "Temporary Supplier"),
)

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    type_of_supply = models.CharField(max_length=500)
    date_contracted = models.DateTimeField()
    contract_type = models.CharField(max_length=200, choices=CONTRACT_CHOICES)
    vetted_by = models.ForeignKey(DepartmentChairperson, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(DepartmentDirector, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.supplier_name

class Purchase(models.Model):
    purchase_number = models.CharField(max_length=200, unique=True)
    item = models.CharField(max_length=200)
    ordered_from = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(DepartmentChairperson, on_delete=models.CASCADE)
    order_approved_by = models.ForeignKey(DepartmentDirector, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField()
    delivery_by = models.DateTimeField()
    quantity = models.FloatField()
    unit_price = models.FloatField()
    total_price = models.FloatField()

    def __str__(self):
        return self.item + " " + str(self.total_price)

class Supply(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    delivered_on = models.DateTimeField()
    received_by = models.ForeignKey(DepartmentChairperson, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(DepartmentDirector, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit_price = models.FloatField()

    def __str__(self):
        return self.purchase.item

    class Meta:
        verbose_name = ("Supply")
        verbose_name_plural = ("Supplies")