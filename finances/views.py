from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
import json
from .models import Budget, Income, Category, Expenses
from .forms import BudgetForm, IncomeForm, ExpenseForm,DashboardBudgetSelect

# Create your views here.

#_____________________________________________________________________

# Function for displaying dashboard

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
    form_class = IncomeForm
    template_name = 'finances/income_form.html'
    success_url = reverse_lazy('dashboard')

    # Passes user as requested user to IncomeForm for user specific filtering
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Income successfully created!")
        response = super().form_valid(form)
        if 'add_more' in self.request.POST:
            return redirect('income_create')
        else:
            return response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomes'] = Income.objects.filter(user_id=self.request.user)
        return context

def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user_id=request.user)
    if request.method == "POST":
        income.delete()
        messages.success(request, 'Income deleted successfully!')
    return redirect('income_create')

#_____________________________________________________________________

class ExpenseView(LoginRequiredMixin, CreateView):
    """
    This view allows users to post expense data to the expense Model. 
    It only allows authorised users to see their own expenses. 
    """
    model = Expenses
    form_class = ExpenseForm
    template_name = 'finances/expense_form.html'
    success_url = reverse_lazy('dashboard')

    # Passes user as requested user to ExpenseForm for user specific filtering
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Expense successfully created!")
        response = super().form_valid(form)
        if 'add_more' in self.request.POST:
            return redirect('expense_create')
        else:
            return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expenses.objects.filter(user_id=self.request.user)
        return context
    
def delete_expense(request, pk):
    expense = get_object_or_404(Expenses, pk=pk, user_id=request.user)
    if request.method == "POST":
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
    return redirect('expense_create')

#_____________________________________________________________________

def DashboardView(request):
    """
    This function based view will hand the summary of the users financial
    data. The function based view allows us to handle multiple form POST requests. 
    """
    # Variables
    budget_select_form = DashboardBudgetSelect(user=request.user, prefix='budget_select')
    selected_budget = None
    total_expenses = None
    total_incomes = None
    # Prepare category names and default (zero) data for charts
    categories = Category.objects.all()
    category_names = [cat.name for cat in categories]
    category_name_data = [0 for _ in category_names]

    #___________

    # Function for calculating Expense total
    def budget_expense_total(user, month, year):
        expenses = Expenses.objects.filter(user_id=user, budget__month=month, budget__year=year,)
        result = expenses.aggregate(Sum('amount'))
        total = result['amount__sum']
        if total is None:
            return 0 
        return total

    # Function for calculating Income total here
    def budget_income_total(user, month, year):
        incomes = Income.objects.filter(user_id=user, budget__month=month, budget__year=year)
        result = incomes.aggregate(Sum('amount'))
        total = result['amount__sum']
        if total is None:
            return 0
        return total
    
    # Function to process category data into chart
    def category_chart_data(user, month, year):
        expenses = Expenses.objects.filter(user_id=user, budget__month=month, budget__year=year,)
        categories = Category.objects.all()
        # list for chart labels
        category_names = [cat.name for cat in categories]
        # dic to increment value based on how many times a category in recorded expenses
        category_count = {name: 0 for name in category_names}
        for expense in expenses:
            cat_name = expense.category.name
            if cat_name in category_count:
                category_count[cat_name] += 1
        # Extracts value list from dictionary ready for chart data
        category_name_data = [category_count[name] for name in category_names]
        return category_names, category_name_data 

    #___________

    # Handles which post request should action, based on prefix 
    if request.method == "POST":
        if "budget_select-budget" in request.POST:
            budget_select_form = DashboardBudgetSelect(user=request.user, data=request.POST, prefix="budget_select")
            if budget_select_form.is_valid():
                selected_budget = budget_select_form.cleaned_data['budget']
                month = selected_budget.month
                year = selected_budget.year
                total_expenses = budget_expense_total(user=request.user, month=month, year=year)
                total_incomes = budget_income_total(user=request.user, month=month, year=year)
                category_names, category_name_data = category_chart_data(user=request.user, month=month, year=year)
                print(category_names, category_name_data)
    
    #___________

    # Variables
    context = {
        "budget_select_form": budget_select_form,
        "selected_budget": selected_budget,
        "total_expenses": total_expenses,
        "total_incomes": total_incomes,
        "category_names": json.dumps(category_names),
        "category_name_data": json.dumps(category_name_data),
    }
        
            
    return render(request, 'finances/dashboard.html', context)