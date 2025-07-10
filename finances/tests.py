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

    #Test that busget is created with correct values
    def test_budget_creation(self):
        self.assertEqual(self.budget.amount, 1000)
        self.assertEqual(self.budget.month, 7)
        self.assertEqual(self.budget.year, 2025)
        self.assertEqual(self.budget.user_id, self.user)

    #Test that income is created and linked to budget and user
    def test_income_creation(self):
        income = Income.objects.create(user_id=self.user, amount=500, source="job", budget=self.budget)
        self.assertEqual(income.amount, 500)
        self.assertEqual(income.budget, self.budget)
        self.assertEqual(income.user_id, self.user)

    #Test that a category is created with correct name and with user link
    def test_category_creation(self):
        self.assertEqual(self.category.name, "Groceries")
        self.assertEqual(self.category.user_id, self.user)
    
    #Test that an expense is created and linked to the correct user
    def test_expense_creation(self):
        expense = Expenses.objects.create(user_id=self.user, amount=200, category=self.category, budget=self.budget)
        self.assertEqual(expense.amount, 200)
        self.assertEqual(expense.category, self.category)
        self.assertEqual(expense.budget, self.budget)
        self.assertEqual(expense.user_id, self.user)


class FinanceCreateViewTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser43', passwords="testpass1")
        self.client.login(username='testuser43', passwords="testpass1")