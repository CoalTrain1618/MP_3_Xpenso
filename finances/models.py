from django.db import models
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

User = get_user_model()

#_____________________________________________________________________

class Budget(models.Model):

    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]

    YEAR_CHOICES = [(y, y) for y in range(datetime.date.today().year, datetime.date.today().year + 5)]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_set = models.DateField(auto_now_add=True)
    month = models.IntegerField(choices=MONTH_CHOICES, default=datetime.date.today().month)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.date.today().month)

    def month_year(self):
        return f"{self.get_month_display()} {self.year}"

    def __str__(self):
        return f"{self.month_year()} ({self.user_id})"

#_____________________________________________________________________

class Income(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=60)
    date_set = models.DateField(auto_now_add=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} ({self.user_id})"
#_____________________________________________________________________

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

#_____________________________________________________________________

class Expenses(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=50, null=True, blank=True)
    date_set = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} ({self.user_id})"