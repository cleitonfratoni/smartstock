from django.db import models

from inventory.models.supplier_model import Supplier

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    quantity = models.IntegerField()
    min_stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
