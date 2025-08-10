from django import forms
from django.forms import ModelForm
from .models import Budget, Income, Category, Expenses
import datetime


class CleanAmountMixin:
    """
    Mixin to validate that the amount is greater than zero.
    """
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise forms.ValidationError(
                "Amount must be greater than zero."
            )
        return amount


class BudgetForm(CleanAmountMixin, forms.ModelForm):
    """
    Form for creating a new budget.
    """
    month = forms.ChoiceField(
        choices=Budget.MONTH_CHOICES,
        initial=datetime.date.today().month,
    )
    year = forms.ChoiceField(
        choices=Budget.YEAR_CHOICES,
        initial=datetime.date.today().year,
    )

    class Meta:
        model = Budget
        fields = ['amount', 'month', 'year']


class IncomeForm(CleanAmountMixin, ModelForm):
    """
    Form for creating a new income entry.
    """
    class Meta:
        model = Income
        fields = ['amount', 'source', 'budget']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['budget'].queryset = Budget.objects.filter(
            user_id=user
        )


class ExpenseForm(CleanAmountMixin, ModelForm):
    """
    Form for creating a new expense.
    """
    class Meta:
        model = Expenses
        fields = [
            'expense_date', 'amount', 'category', 'description',
            'budget'
        ]
        widgets = {
            'expense_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Limit form choices to user's budgets and all categories
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['budget'].queryset = Budget.objects.filter(
            user_id=user
        )
        self.fields['category'].queryset = Category.objects.all()


class DashboardBudgetSelect(forms.Form):
    """
    Form for selecting a budget in the dashboard.
    """
    budget = forms.ModelChoiceField(queryset=Budget.objects.none())

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['budget'].queryset = Budget.objects.filter(
                user_id=user
            )
