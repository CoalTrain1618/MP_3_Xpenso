from django.urls import path
from . import views
from .views import BudgetView

urlpatterns = [
    path('budget/add/', BudgetView.as_view(), name="budget_create"),
    path('dashboard/', views.DashboardView, name='dashboard')
]