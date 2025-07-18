from django import forms
from django.forms import ModelForm
from .models import Budget, Income, Category, Expenses
import datetime

#Budget form for user to create budget.
class BudgetForm(forms.ModelForm):
    month = forms.ChoiceField(choices=Budget.MONTH_CHOICES, initial=datetime.date.today().month)
    year = forms.ChoiceField(choices=Budget.YEAR_CHOICES, initial=datetime.date.today().year)
    
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


#Expense form  for user to create expenses
class ExpenseForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense_date', 'amount', 'category', 'description', 'budget']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['budget'].queryset = Budget.objects.filter(user_id=user)
        self.fields['category'].queryset = Category.objects.filter(user_id=user)

