from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
import json
from .models import Budget, Income, Category, Expenses
from .forms import BudgetForm, IncomeForm, ExpenseForm, DashboardBudgetSelect

# Create your views here.

# _____________________________________________________________________


class BudgetView(LoginRequiredMixin, CreateView):
    """
    This budget view allows the user to submit budget data.
    The user will be redirected to dashboard on success.
    """
    model = Budget
    form_class = BudgetForm
    template_name = 'finances/budget_form.html'
    success_url = reverse_lazy('dashboard')

    # Method to add context variable to template for budgets
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budgets'] = Budget.objects.filter(user_id=self.request.user)
        return context

    # Handles form submission: assigns the user,
    # saves the budget, displays a success message,
    # and redirects to the dashboard upon successful creation.
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Budget created successfully!")
        return super().form_valid(form)


# Method to allow user to delete created budgets
def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user_id=request.user)
    if request.method == "POST":
        budget.delete()
        messages.success(request, 'Budget deleted successfully!')
    return redirect('budget_create')


# View to handle edit records for CRUD functionality
class BudgetEditView(LoginRequiredMixin, UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'finances/budget_form.html'
    success_url = reverse_lazy('budget_create')

    def get_queryset(self):
        return Budget.objects.filter(user_id=self.request.user)

# _____________________________________________________________________


class IncomeView(LoginRequiredMixin, CreateView):
    """
    This Income View will allow users to record an Income.
    On success, logged in user will be redirected to dashboard.
    """
    model = Income
    form_class = IncomeForm
    template_name = 'finances/income_form.html'
    success_url = reverse_lazy('dashboard')

    # Passes requested user to IncomeForm for user specific filtering
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # Method to add context variable to template for Income
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomes'] = Income.objects.filter(user_id=self.request.user)
        return context

    # Handles form submission: assigns the user,
    # saves the income, displays a success message,
    # and redirects if the user wishes to add more income records.
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Income successfully created!")
        response = super().form_valid(form)
        if 'add_more' in self.request.POST:
            return redirect('income_create')
        else:
            return response


# Method to allow users to delete created income records
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user_id=request.user)
    if request.method == "POST":
        income.delete()
        messages.success(request, 'Income deleted successfully!')
    return redirect('income_create')


# View to handle edit records for CRUD functionality
class IncomeEditView(LoginRequiredMixin, UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = "finances/income_form.html"
    success_url = reverse_lazy('income_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomes'] = Income.objects.filter(user_id=self.request.user)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Income.objects.filter(user_id=self.request.user)

# _____________________________________________________________________


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

    # Handles form submission: sets the user,
    # saves the expense, shows a success message,
    # and redirects if the user wants to add more expenses.
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        messages.success(self.request, "Expense successfully created!")
        response = super().form_valid(form)
        if 'add_more' in self.request.POST:
            return redirect('expense_create')
        else:
            return response

    # Method to pass expenses as context variable to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expenses.objects.filter(
            user_id=self.request.user
            )
        return context


# Method which allows user to delete created expense records
def delete_expense(request, pk):
    expense = get_object_or_404(Expenses, pk=pk, user_id=request.user)
    if request.method == "POST":
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
    return redirect('expense_create')


# View to handle edit records for CRUD functionality
class ExpenseEditView(LoginRequiredMixin, UpdateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = "finances/expense_form.html"
    success_url = reverse_lazy('expense_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expenses'] = Expenses.objects.filter(
            user_id=self.request.user
            )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Expenses.objects.filter(user_id=self.request.user)

# _____________________________________________________________________


def DashboardView(request):
    """
    This function based view will hand the summary of
    the users financial data. The function based view
    allows us to handle multiple form POST requests.
    """
    # Variables
    budget_select_form = DashboardBudgetSelect(
        user=request.user, prefix='budget_select'
    )
    selected_budget = None
    total_expenses = None
    total_incomes = None
    budget_amount = None
    # Prepare category names and default (zero) data for charts
    categories = Category.objects.all()
    category_names = [cat.name for cat in categories]
    category_name_data = [0 for _ in category_names]

    # ___________

    # Function to calculate budget's Expense total
    def budget_expense_total(user, month, year):
        expenses = Expenses.objects.filter(
            user_id=user, budget__month=month, budget__year=year
        )
        result = expenses.aggregate(Sum('amount'))
        total = result['amount__sum']
        if total is None:
            return 0
        return total

    # Function to calculate budget's Income total here
    def budget_income_total(user, month, year):
        incomes = Income.objects.filter(
            user_id=user, budget__month=month, budget__year=year
        )
        result = incomes.aggregate(Sum('amount'))
        total = result['amount__sum']
        if total is None:
            return 0
        return total

    # Function to process category data into chart
    def category_chart_data(user, month, year):
        expenses = Expenses.objects.filter(
            user_id=user, budget__month=month, budget__year=year
        )
        categories = Category.objects.all()
        # list for chart labels
        category_names = [cat.name for cat in categories]
        # dic to increment value based on how
        # many times a category in recorded expenses
        category_count = {name: 0 for name in category_names}
        for expense in expenses:
            cat_name = expense.category.name
            if cat_name in category_count:
                category_count[cat_name] += 1
        # Extracts value list from dictionary ready for chart data
        category_name_data = [category_count[name] for name in category_names]
        return category_names, category_name_data

    # ___________

    # Handles which post request should action, based on prefix
    if request.method == "POST":
        if "budget_select-budget" in request.POST:
            budget_select_form = DashboardBudgetSelect(
                user=request.user, data=request.POST, prefix="budget_select"
            )
            if budget_select_form.is_valid():
                selected_budget = budget_select_form.cleaned_data['budget']
                month = selected_budget.month
                year = selected_budget.year
                budget_amount = selected_budget.amount
                total_expenses = budget_expense_total(
                    user=request.user, month=month, year=year
                )
                total_incomes = budget_income_total(
                    user=request.user, month=month, year=year
                )
                category_names, category_name_data = category_chart_data(
                    user=request.user, month=month, year=year
                )
                print(category_names, category_name_data)

    # ___________

    # Variables
    context = {
        "budget_select_form": budget_select_form,
        "selected_budget": selected_budget,
        "total_expenses": total_expenses,
        "total_incomes": total_incomes,
        "budget_amount": budget_amount,
        "category_names": json.dumps(category_names),
        "category_name_data": json.dumps(category_name_data),
    }

    return render(request, 'finances/dashboard.html', context)
