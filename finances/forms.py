from django import forms
from django.forms import ModelForm
from .models import Budget, Income, Category, Expenses

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'month', 'year']

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['Budget'].queryset = Budget.objects.filter()
        