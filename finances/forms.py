from django import forms
from django.forms import ModelForm
from .models import Budget, Income, Category, Expenses

#Budget form for user to create budget.
class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'month', 'year']


#Income form for user to create Income