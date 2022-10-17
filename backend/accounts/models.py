from email.policy import default
from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
