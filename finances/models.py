from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Budget(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_set = models.DateField(auto_now_add=True)
    month = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()

class Income(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=60)
    date_set = models.DateField(auto_now_add=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

