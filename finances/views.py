from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Budget, Income, Category, Expenses
from .forms import BudgetForm, IncomeForm, ExpenseForm

# Create your views here.

#_____________________________________________________________________

# Function for displaying dashboard
def DashboardView(request):
    return render(request, 'finances/dashboard.html')

#_____________________________________________________________________

class BudgetView(LoginRequiredMixin ,CreateView):
    """
    This budget view allows the user to submit budget data.
    The user will be redirected to dashboard on success.
    """
    model = Budget
    form_class = BudgetForm
    template_name = 'finances/budget_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Budget created successfully!")
        return super().form_valid(form)
    
#_____________________________________________________________________

class IncomeView(LoginRequiredMixin, CreateView):
    """
    This Income View will allow users to record an Income. 
    On success, logged in user will be redirected to dashboard.
    """
    model = Income
    fields = ['source', 'amount', 'budget']
    template_name = 'finances/income_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Income was Successfully created!")
        return super().form_valid(form)