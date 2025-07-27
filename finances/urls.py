from django.urls import path
from . import views
from .views import BudgetView, BudgetEditView
from .views import IncomeView, IncomeEditView
from .views import ExpenseView, ExpenseEditView

urlpatterns = [
    # Expense urls
    path('expense/add/', ExpenseView.as_view(), name='expense_create'),
    path('expense/edit/<int:pk>/', ExpenseEditView.as_view(), name="edit_expense"),
    path('budget/expense/<int:pk>/', views.delete_expense, name="delete_expense"),
    # Income urls
    path('income/add/', IncomeView.as_view(), name='income_create'),
    path('income/edit/<int:pk>/', IncomeEditView.as_view(), name="edit_income"),
    path('budget/income/<int:pk>/', views.delete_income, name="delete_income"),
    # Budget urls
    path('budget/add/', BudgetView.as_view(), name="budget_create"),
    path('budget/edit/<int:pk>/', BudgetEditView.as_view(), name="edit_budget"),
    path('budget/delete/<int:pk>/', views.delete_budget, name="delete_budget"),
    # Dashboard urls
    path('dashboard/', views.DashboardView, name='dashboard'),
]