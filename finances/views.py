from django.shortcuts import render, redirect, get_object_or_404
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = Budget.objects.filter(user_id=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Budget created successfully!")
        return super().form_valid(form)

def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user_id=request.user)
    if request.method == "POST":
        budget.delete()
        messages.success(request, 'Budget deleted successfully!')
    return redirect('budget_create')

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
        messages.success(self.request, "Income successfully created!")
        response = super().form_valid(form)
        if 'add_more' in self.request.POST:
            return redirect('income_create')
        else:
            return response

class ExpenseView(LoginRequiredMixin, CreateView):
    """
    This view allows users to post expense data to the expense Model. 
    It only allows authorised users to see their own expenses. 
    """
    model = Expenses
    fields = ['amount', 'expense_date', 'category', 'description', 'budget']
    template_name = 'finances/expense_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Expense successfully created!")
        response = super().form_valid(form)
        if 'add_more' in self.request.POST:
            return redirect('expense_create')
        else:
            return response
        