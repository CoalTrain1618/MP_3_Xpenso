from django.urls import path
from .views import BudgetView

urlpatterns = [
    path('budget/add/', BudgetView.as_view(), name="budget_create"),
]