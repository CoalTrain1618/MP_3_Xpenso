from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Budget, Income, Category, Expenses
from .forms import BudgetForm, IncomeForm, ExpenseForm, DashboardBudgetSelect

import datetime


User = get_user_model()

# Create your tests here.

class FinanceModelsTest(TestCase):

    #create and define example data to use in all tests
    def setUp(self):
        self.user = User.objects.create_user(username="testuser42", password="testpass")
        self.budget = Budget.objects.create(user_id=self.user, amount=1000, month=datetime.date.today().month,
                                            year=datetime.date.today().year)
        self.category = Category.objects.create(name="Groceries")

    #Test that busget is created with correct values
    def test_budget_creation(self):
        self.assertEqual(self.budget.amount, 1000)
        self.assertEqual(self.budget.month, datetime.date.today().month)
        self.assertEqual(self.budget.year, datetime.date.today().year)
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
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Budget.objects.filter(user_id=self.user, amount=500, month=datetime.date.today().month, 
                                              year=datetime.date.today().year).exists())

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
                'month': datetime.date.today().month,
                'year': datetime.date.today().year,
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
            month=datetime.date.today().month,
            year=datetime.date.today().year,
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
            month=datetime.date.today().month,
            year=datetime.date.today().year,
        )
        self.category = Category.objects.create(
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

class BudgetFormTest(TestCase):
    """
    This will test the validation of BudgetForm, to ensure all data is handled correctly.
    """
    # User creation
    def setUp(self):
        self.user = User.objects.create_user(username="testform", password="testpass")
        self.client.login(username="testform", password="testpass")
    
    def  test_budget_form_valid(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {
            'amount': 500,
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }
        form = BudgetForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_budget_form_invalid_amount(self):
        """
        Test that the form is picks up invalid data
        """
        form_data = {
            'amount': -100,
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }
        form = BudgetForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)
        self.assertEqual(form.errors['amount'], ["Amount must be greater than zero."])
    
# ________________________________________________________________________________

class ExpenseFormTest(TestCase):
    """
    This will test the validation of ExpenseForm, to ensure all data is handled correctly.
    """
    # User creation
    def setUp(self):
        self.user = User.objects.create_user(username="testexpense", password="testpass")
        self.client.login(username="testexpense", password="testpass")
        self.budget = Budget.objects.create(
            user_id=self.user,
            amount=1000,
            month=datetime.date.today().month,
            year=datetime.date.today().year,
        )
        self.category = Category.objects.create(name="Utilities")

    def test_expense_form_valid(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {
            'amount': 200,
            'expense_date': '2025-07-15',
            'category': self.category.pk,
            'description': 'Electricity bill',
            'budget': self.budget.pk,
        }
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_expense_form_invalid_amount(self):
        """
        Test that the form picks up invalid data for amount.
        """
        form_data = {
            'amount': -50,
            'expense_date': '2025-07-15',
            'category': self.category.pk,
            'description': 'Water bill',
            'budget': self.budget.pk,
        }
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)
        self.assertEqual(form.errors['amount'], ["Amount must be greater than zero."])

# ________________________________________________________________________________

class IncomeFormTest(TestCase):
    """
    This will test the validation of IncomeForm, to ensure all data is handled correctly.
    """
    # User creation
    def setUp(self):
        self.user = User.objects.create_user(username="testincome", password="testpass")
        self.client.login(username="testincome", password="testpass")
        self.budget = Budget.objects.create(
            user_id=self.user,
            amount=1000,
            month=datetime.date.today().month,
            year=datetime.date.today().year,
        )

    def test_income_form_valid(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {
            'amount': 300,
            'source': 'Freelance',
            'budget': self.budget.pk,
        }
        form = IncomeForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_income_form_invalid_amount(self):
        """
        Test that the form picks up invalid data for amount.
        """
        form_data = {
            'amount': -100,
            'source': 'Freelance',
            'budget': self.budget.pk,
        }
        form = IncomeForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)
        self.assertEqual(form.errors['amount'], ["Amount must be greater than zero."])

# ________________________________________________________________________________

class UserIsolationTestingBudget(TestCase):
    """
    This will test that users cannot access each other's budget data.
    """

    def setUp(self):
        
        self.user_a = User.objects.create_user(username="user_a", password="pass_a")
        self.user_b = User.objects.create_user(username="user_b", password="pass_b")
        
        # test Budgets
        self.budget_a = Budget.objects.create(
            user_id = self.user_a,
            amount = 1000,
            month = datetime.date.today().month,
            year = datetime.date.today().year,
        )
        self.budget_b = Budget.objects.create(
            user_id = self.user_b,
            amount = 1500,
            month = datetime.date.today().month,
            year = datetime.date.today().year,
        )

    def test_user_cannot_view_other_user_budget(self):
        """
        Test that user A cannot access user B's budget.
        """
        self.client.login(username="user_a", password="pass_a")
        url = reverse('edit_budget', args=[self.budget_b.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_user_only_see_their_budget(self):
        """
        Test that user A can only see their own budget.
        """
        self.client.login(username="user_b", password="pass_b")
        url = reverse('edit_budget', args=[self.budget_b.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# ________________________________________________________________________________

class UserIsolationTestingExpenses(TestCase):
    """
    This will test that users cannot access each other's data.
    """
    def setUp(self):
        self.user_a = User.objects.create_user(username='user_a', password='pass_a')
        self.user_b = User.objects.create_user(username='user_b', password='pass_b')

        # Test Budgets
        self.budget_a = Budget.objects.create(
            user_id=self.user_a,
            amount=1000,
            month=datetime.date.today().month,
            year=datetime.date.today().year
        )
        self.budget_b = Budget.objects.create(
            user_id=self.user_b,
            amount=1500,
            month=datetime.date.today().month,
            year=datetime.date.today().year
        )   

        # Test Category
        self.category = Category.objects.create(name="TestCat")

        # test expenses
        self.expense_a = Expenses.objects.create(
            user_id=self.user_a,
            amount=200,
            category=self.category,
            budget=self.budget_a,
            expense_date=datetime.date.today()
        )
        self.expense_b = Expenses.objects.create(
            user_id=self.user_b,
            amount=300,
            category=self.category,
            budget=self.budget_b,
            expense_date=datetime.date.today()
        )

    def test_user_cannot_view_other_user_expenses(self):
        """
        Test that user A cannot access user B's expenses.
        """
        self.client.login(username='user_a', password='pass_a')
        url = reverse('edit_expense', args=[self.expense_b.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_user_only_see_own_expenses(self):
        """
        Test that user A can only see their own expenses.
        """
        self.client.login(username='user_a', password='pass_a')
        url = reverse('edit_expense', args=[self.expense_a.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

# ________________________________________________________________________________

class UserIsolationTestingIncome(TestCase):
    """
    This will test that users cannot access each other's income data.
    """

    def setUp(self):

        self.user_a = User.objects.create_user(username="user_a", password="pass_a")
        self.user_b = User.objects.create_user(username="user_b", password="pass_b")

        # Test Budgets
        self.budget_a = Budget.objects.create(
            user_id = self.user_a,
            amount = 1000,
            month = datetime.date.today().month,
            year = datetime.date.today().year,
        )
        self.budget_b = Budget.objects.create(
            user_id = self.user_b,
            amount = 1500,
            month = datetime.date.today().month,
            year = datetime.date.today().year,
        )

        # Test Incomes
        self.income_a = Income.objects.create(
            user_id = self.user_a,
            amount = 100,
            source = "freelancing",
            budget = self.budget_a,
        )
        self.income_b = Income.objects.create(
            user_id = self.user_b,
            amount = 100,
            source = "freelancing",
            budget = self.budget_b,
        )

    def test_user_cannot_see_other_user_income(self):
        """
        Test that user A cannot access user B's income.
        """
        self.client.login(username="user_a", password="pass_a")
        url = reverse('edit_income', args=[self.income_b.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_user_only_see_their_income(self):
        """
        Test that user_b can only see their own income.
        """
        self.client.login(username="user_b", password="pass_b")
        url = reverse('edit_income', args=[self.income_b.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
# ________________________________________________________________________________

class  EdgeCaseTestBudget(TestCase):
    """
    Tests for edgecase testing budget
    """
    def setUp(self):

        self.user = User.objects.create_user(username="testuser", password="testpass")

#______________________   

    def test_max_digits_amount_field(self):
        """
        Testing max digit input
        """
        form_data = {
            'amount': 9999.99,
            'month': datetime.date.today().month,
            'year': datetime.date.today().year, 
        }
        
        self.client.login(username="testuser", password="testpass")
        form = BudgetForm(data=form_data)
        self.assertTrue(form.is_valid())
    
#______________________

    def test_exceeding_max_digit_amount_field(self):
        """
        Test exceeding the max digit input
        """
        form_data = {
            'amount': 99999.99, #added extra 9 for test
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }

        self.client.login(username="testuser", password="testpass")
        form = BudgetForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Ensure that there are no more than 6 digits in total.', form.errors['amount'][0])

#______________________

    def test_minimum_digit_amount_field(self):
        """
            Testing the minimum digit amount field
        """
        form_data = {
            'amount': 1,
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }

        self.client.login(username="testuser", password="testpass")
        form = BudgetForm(data=form_data)
        self.assertTrue(form.is_valid())

#______________________

    def test_below_minimum_digit_amount_field(self):
        """
        Test that the form does not accept zero as a valid amount.
        """
        form_data = {
            'amount': -1,
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }

        self.client.login(username="testuser", password="testpass")
        form = BudgetForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Amount must be greater than zero.', form.errors['amount'][0])

#______________________

    def test_zero_digit_amount_field(self):
        """
        Test that the form does not accept zero as a valid amount.
        """
        form_data = {
            'amount': 0,
            'month': datetime.date.today().month,
            'year': datetime.date.today().year,
        }

        self.client.login(username="testuser", password="testpass")
        form = BudgetForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Amount must be greater than zero.', form.errors['amount'][0])


# ________________________________________________________________________________

class EdgeCaseTestExpense(TestCase):
    """
    Tests for edgecase testing ExpenseForm
    """
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

        self.budget_test = Budget.objects.create(
            user_id = self.user,
            amount = 1000,
            month = datetime.date.today().month,
            year = datetime.date.today().year,
        )

        self.category = Category.objects.create(name='testCat')

#______________________

    def test_description_blank_input(self):
        """
        Test that the form accepts blank description.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 5,
            'category': self.category.pk,
            'description': '',
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

#______________________

    def test_description_max_length(self):
        """
        Test that the form accepts description with maximum length.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 5,
            'category': self.category.pk,
            'description': 'a' * 50,  # 50 characters
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

#______________________

    def test_description_exceeding_max_length(self):
        """
        Test that the form does not accept description exceeding max length.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 5,
            'category': self.category.pk,
            'description': 'a' * 51,  # 51 characters, exceeding max length
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('Ensure this value has at most 50 characters (it has 51).', form.errors['description'][0])

#______________________

    def test_amount_max_digits(self):
        """
        Test that the form is valid with maximum digits for amount.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 9999.99,  # max digits
            'category': self.category.pk,
            'description': 'Test expense',
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

#______________________

    def test_amount_exceeding_max_digits(self):
        """
        Test that the form does not accept amounts exceeding max digits.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 99999.99,  # exceeding max digits
            'category': self.category.pk,
            'description': 'TestExpense',
            'budget': self.budget_test.pk
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('Ensure that there are no more than 6 digits in total.', form.errors['amount'][0])

#______________________
    
    def test_minimum_amount(self):
        """
        Test that the form is valid with minimum amount.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 1,  
            'category': self.category.pk,
            'description': 'Test expense',
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())

#______________________

    def test_below_minimum_amount(self):
        """
        Test that the form does not accept amounts below minimum.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': -1, 
            'category': self.category.pk,
            'description': 'Test expense',
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('Amount must be greater than zero.', form.errors['amount'][0])

#______________________

    def test_zero_amount(self):
        """
        Test that the form does not accept zero as a valid amount.
        """
        form_data = {
            'expense_date': datetime.date.today(),
            'amount': 0,  
            'category': self.category.pk,
            'description': 'Test expense',
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = ExpenseForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid())
        self.assertIn('Amount must be greater than zero.', form.errors['amount'][0])

# ________________________________________________________________________________

class EdgeCaseTestIncome(TestCase):
    """
    Tests for edgecase testing IncomeForm
    """
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

        self.budget_test = Budget.objects.create(
            user_id = self.user,
            amount = 1000,
            month = datetime.date.today().month,
            year = datetime.date.today().year,
        )
    
#______________________

    def test_source_blank_input(self):
        """
        Test that the form accepts blank source.
        """
        form_data = {
            'amount': 100,
            'source': '',
            'budget': self.budget_test.pk,
        }

        self.client.login(username="testuser", password="testpass")
        form = IncomeForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid())