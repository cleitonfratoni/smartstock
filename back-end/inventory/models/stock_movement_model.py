from django.db import models

from accounts.models.user_model import User
from inventory.models.product_model import Product

class InOrOut(models.IntegerChoices):
    IN = 1, 'In'
    OUT = 2, 'Out'

class StockMovement(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    movement_type = models.IntegerField(choices=InOrOut.choices)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
