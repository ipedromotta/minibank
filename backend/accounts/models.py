from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    
class Transactions(models.Model):
    user = models.ForeignKey(CustomUser, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at',]
        verbose_name = ("Transações")
        verbose_name_plural = ("Transações")
        
    def __str__(self) -> str:
        return self.user.username
    
    def create_transaction(self, user, amount, type):
        self.user = user
        self.amount = amount
        self.type = type
        self.save()
