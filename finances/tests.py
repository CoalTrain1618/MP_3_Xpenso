from django.urls import reverse
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

# ________________________________________________________________________________

class FinanceBudgetViewTests(TestCase):

    # Test user creation for test cases
    def setUp(self):
        self.user = User.objects.create_user(username='testuser43', password="testpass1")
        self.client.login(username='testuser43', password="testpass1")

    #__________

    def test_budget_create_view_get(self):
        """
        Test to ensure the budget form loads for logged in user.
        """
        url = reverse('budget_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "amount")

    #__________

    def test_budget_create_view_post(self):
        """
        Testing if budget is created on submission of form
        """
        url = reverse('budget_create')
        data = {
            'amount': 500,
            'month': 7,
            'year': 2025,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Budget.objects.filter(user_id=self.user, amount=500, month=7, year=2025).exists())

    #__________

    def test_budget_create_view_requires_login(self):
        """
        Test to ensure anonymous user are restricted, unless logged in.
        """
        self.client.logout()
        url = reverse('budget_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("accounts/login", response.url)

    #__________
    
    def test_budget_create_view_success_message(self):
        """
        Test that django message is displayed upon budget completion
        """
        url = reverse('budget_create')
        data = {'amount': 1000,
                'month': 8,
                'year': 2025,
                }
        response = self.client.post(url, data, follow=True)
        messages = list(response.context['messages'])
        self.assertTrue(any("Budget created successfully!" in str(m) for m in messages))

# ________________________________________________________________________________

class FinanceIncomeViewTest(TestCase):
    """
    The following test will be to test if IncomeView is functional and valid. 
    This test should showcase that a User can record and income, which will
    be successfully applied to the DB on submission.
    """

    # Creating mock user for testcase.
    def setUp(self):
        self.user = User.objects.create_user(username='testuser33', password="testpass4")
        self.client.login(username='testuser33', password="testpass4")
        self.budget = Budget.objects.create(
            user_id=self.user,
            amount=1000,
            month=7,
            year=2025
        )
    
    #__________

    def test_income_create_view_get(self):
        """
        Test to check if Income form displays correctly
        """
        url = reverse('income_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "amount")

    #__________

    def test_income_create_view_post(self):
        """
        Testing if Income is created on submission of form.
        """
        url = reverse('income_create')
        data = {
            'source': 'job',
            'amount': 500,
            'budget': self.budget.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Income.objects.filter(user_id=self.user, amount=500, budget=self.budget).exists())

    #__________

    def test_income_create_view_requires_login(self):
        """
        Test to ensure anonymous users are restricted, unless logged in.
        """
        self.client.logout()
        url = reverse('income_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("accounts/login", response.url)

    #__________

    def test_income_create_view_success_message(self):
        """
        Test that Django message is displayed upon income successful submission
        """
        url = reverse('income_create')
        data = {
            'source': 'job',
            'amount': 250,
            'budget': self.budget.pk,
        }
        response = self.client.post(url, data, follow=True)
        messages = list(response.context['messages'])
        self.assertTrue(any("Income successfully created!" in str(m) for m in messages))

# ________________________________________________________________________________

class FinanceExpenseViewTest(TestCase):
    """
    To test if ExpenseView allows user to create and submit data to the Expense 
    DB table. 
    """

    # Create mock user and data for testing
    def setUp(self):
        self.user = User.objects.create_user(username='testuser74', password='testpass11')
        self.client.login(username='testuser74', password='testpass11')
        self.budget = Budget.objects.create(
            user_id = self.user,
            amount=1000,
            month=7,
            year=2025
        )
        self.category = Category.objects.create(
            user_id=self.user,
            name = 'Fuel'
        )
    
    #__________

    def test_expense_create_view_get(self):
        """
        To check Expense form loads and displays correctly
        """
        url = reverse('expense_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'amount')

    #__________

    def test_expense_create_view_post(self):
        """
        Testing if Expense data is created on form submission
        """
        url = reverse('expense_create')
        data = {
            'amount': 30,
            'expense_date': '2025-07-15',
            'category': self.category.pk,
            'description': 'Fuel for car',
            'budget': self.budget.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Expenses.objects.filter(
            user_id=self.user,
            amount=30,
            expense_date='2025-07-15',
            category=self.category,
            description='Fuel for car',
            budget= self.budget,
        ))

    #__________

    def test_expense_create_view_requires_login(self):
        """
        Test to ensure anonymous users are restricted, unless logged in.
        """
        self.client.logout()
        url = reverse('expense_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("accounts/login", response.url)
    
    #__________

    def test_expense_create_view_success_message(self):
        """
        Test that Django message is displayed upon Expense successful submission
        """
        url = reverse('expense_create')
        data = {
            'amount': 30,
            'expense_date': '2025-07-15',
            'category': self.category.pk,
            'description': 'Fuel for car',
            'budget': self.budget.pk,
        }
        response = self.client.post(url, data, follow=True)
        messages = list(response.context['messages'])
        self.assertTrue(any("Expense successfully created!" in str(m) for m in messages))

# ________________________________________________________________________________
