from django.urls import path
from . import views
from .views import BudgetView
from .views import IncomeView
from .views import ExpenseView

urlpatterns = [
    path('expense/add/', ExpenseView.as_view(), name='expense_create'),
    path('income/add/', IncomeView.as_view(), name='income_create'),
    path('budget/income/<int:pk>/', views.delete_income, name="delete_income"),
    path('budget/add/', BudgetView.as_view(), name="budget_create"),
    path('budget/delete/<int:pk>/', views.delete_budget, name="delete_budget"),
    path('dashboard/', views.DashboardView, name='dashboard'),
]