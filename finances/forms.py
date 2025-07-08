from django import forms
from django.forms import ModelForm
from .models import Budget, Income, Category, Expenses

#Budget form for user to create budget.
class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'month', 'year']


#Income form for user to create Income
class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'budget']

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['budget'].queryset= Budget.objects.filter(user_id=user)
