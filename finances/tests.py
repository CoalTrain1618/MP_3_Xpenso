from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Budget, Income, Category, Expenses

User = get_user_model()

# Create your tests here.

class FinanceModelsTest(TestCase):

    #create and define example data to use in all tests
    def setUp(self):
        self.user = User.objects.create_user(username="testuser42", password="testpass")
        self.budget = Budget.objects.create(user_id=self.user, 
                                            amount=1000, month=7, year=2025)
        self.category = Category.objects.create(user_id=self.user, name="Groceries")

    