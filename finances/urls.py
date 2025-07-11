from django.urls import path
from . import views
from .views import BudgetView
from .views import IncomeView

urlpatterns = [
    path('income/add/', IncomeView.as_view(), name='income_create'),
    path('budget/add/', BudgetView.as_view(), name="budget_create"),
    path('dashboard/', views.DashboardView, name='dashboard'),
]