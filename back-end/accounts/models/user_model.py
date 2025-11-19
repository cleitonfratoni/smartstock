from django.db import models
from django.contrib.auth.models import AbstractUser

class RoleEmployee(models.TextChoices):
        ADMINISTRATOR = 'ADM', 'Administrator'
        OPERATOR = 'OPR', 'Operator'

class User(AbstractUser):
    employee_register = models.IntegerField()
    role = models.CharField(max_length=3, choices=RoleEmployee.choices, default=RoleEmployee.OPERATOR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
