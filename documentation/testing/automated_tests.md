# Automated Testing Document

---

## Contents

- [Introduction](#introduction)
- [Model Tests](#model-tests)
- [View Tests](#view-tests)
    - [BudgetView](#budgetview)
    - [IncomeView](#incomeview)
    - [ExpenseView](#expenseview)
- [Form Validation Tests](#form-validation-tests)
    - [BudgetForm](#budgetform)
    - [ExpenseForm](#expenseform)
    - [IncomeForm](#incomeform)
- [User Isolation Tests](#user-isolation-tests)
    - [Budget](#userisolation-budget)
    - [Expenses](#userisolation-expenses)
    - [Income](#userisolation-income)
- [Edge Case Tests](#edge-case-tests)
    - [ExpenseForm](#edge-case-expenseform)
    - [IncomeForm](#edge-case-incomeform)

---

## Introduction

For this project, I used Test Driven Development (TDD) to ensure code quality and maintainability. TDD means writing tests before writing the actual code, helping define the behaviour of each part of the project from the outset.

**Benefits of TDD and automated tests:**
- Catch mistakes early, before they escalate.
- Enable safer changes and improvements, as tests flag any breaking changes.
- Save time by automating checks for correctness.
- Improve reliability and prepare the project for future updates.

---

## Model Tests

I wrote unit tests for all main models in the finance app: **Budget, Income, Category, and Expenses**. These tests verify:
- Correct model creation.
- Proper relationships (e.g., linking income to budgets, expenses to categories).
- Accurate data storage in the database.

**Test Command:**  
`python manage.py test finances`  
All tests passed, confirming the core app functionality works and future changes can be made confidently.

---

## View Tests

### BudgetView

**Scenario:**  
Users should be able to access `budget_form.html`, input amount, month, and year, and only see their own budgets. On submission, they are redirected (e.g., to dashboard) with a success message.

**Expected Outcomes:**
- Only logged-in users can access the budget creation page.
- The form displays on GET requests.
- Submitting valid data creates a new Budget for the logged-in user.
- User is redirected to the dashboard after submission.
- A success message is displayed.

#### Test Outcomes

| Test | Outcome | Errors | Remedial Work |
|------|---------|--------|--------------|
| 1    | Fail    | - `TemplateDoesNotExist` (finances/budget_form.html)<br>- `NoReverseMatch` ('dashboard' URL missing)<br>- Dependant test failure | - Create `budget_form.html`<br>- Create dashboard template, URL, and view |
| 2    | Fail    | - `ImportError` (import 'h') | - Fix typo in views.py import |
| 3    | Fail    | - `TemplateDoesNotExist` | - Move `budget_form.html` to `finances/templates` directory, adjust structure |
| 4    | Fail    | - `TemplateDoesNotExist` | - Move templates into `finance` folder within `templates` |
| 5    | Pass    | - None | - N/A |

---

### IncomeView

**Scenario:**  
Logged-in users record income via `income_form.html` using fields: `amount`, `source`, and `budget selection`. The view ensures users only access their own data. On success, users are redirected to the dashboard with a message.

**Expected Outcomes:**
- Authorised users can input income.
- Submission posts data to Income DB table.

#### Test Outcomes

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

### ExpenseView

**Scenario:**  
Authorised users record expenses via a form (`expense_form.html`) with fields: `amount`, `expense_date`, `category`, `description`, `budget`. On submission, the data is posted to the Expenses DB table.

**Expected Outcomes:**
- Authorised users can input expense data.
- Submission posts data to Expenses DB table.

#### Test Outcomes

| Test | Outcome | Errors | Remedial Work |
|------|---------|--------|--------------|
| 1    | Fail    | - Incorrect URL names in navigation (`create_budget` vs `budget_create`)<br>- Missing Category object FK in tests.py | - Correct URL names<br>- Add user ID FK to Category object |
| 2    | Fail    | - No HttpResponse from Expense view | - Add proper return in Expense view |
| 3    | Pass    | - None | - N/A |

---

## Form Validation Tests

### BudgetForm

**Purpose:**  
Test validation to ensure only valid data is accepted.

**Expected Outcome:**  
- Valid data (positive amount) passes.
- Negative amount raises validation error.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

### ExpenseForm

**Expected Outcome:**  
The first test should pass, confirming that the ExpenseForm is valid when all fields are filled in with correct data. The second test should fail as expected, with the form picking up the negative amount and raising the “Amount must be greater than zero.” error. This ensures the form validation is working and only allows valid expense entries.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

### IncomeForm

**Expected Outcome:**  
The first test should pass, showing that the IncomeForm accepts valid data and is correctly validated. The second test should fail as expected, with the form catching the negative amount and displaying the “Amount must be greater than zero.” error message. This confirms the form validation is working and prevents users from entering invalid income amounts.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

## User Isolation Tests

Tests to ensure users are restricted to their own records, protecting user security.

### UserIsolationTestingBudget

**Expected Outcome:**  
The first test should fail with a 404 when user A tries to access user B’s budget, confirming that users cannot view or edit each other’s data. The second test should pass, as user B is allowed to access and edit their own budget. This makes sure user isolation is enforced and only the relevant data is visible to each user.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

### UserIsolationTestingExpenses

**Expected Outcome:**  
The first test should fail with a 404 when user A tries to access user B’s expenses, making sure users can’t view or edit each other’s records. The second test should pass, as user A is allowed to access their own expense. This confirms that user isolation is enforced and only the correct data is available to each user.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

### UserIsolationTestingIncome

**Expected Outcome:**  
The first test should fail with a 404 when user A tries to access user B’s income data, ensuring users can’t view or edit each other’s income records. The second test should pass, as user B is able to access their own income. This confirms user isolation is working and only the correct income data is accessible to each user.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

## Edge Case Tests

Edge case tests pressure test validation at maximum and minimum values, protecting forms from unexpected errors and potential malicious input.

### EdgeCaseTestExpenseForm

**Expected Outcome:**  
The form should accept blank descriptions and descriptions up to 50 characters, but reject anything longer. Amounts are valid up to 9999.99 and must be greater than zero, so tests with values at the limit should pass, while negative, zero, or overly large amounts should fail with the correct error messages. This confirms the form properly handles all common and edge case inputs.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---

### EdgeCaseTestIncomeForm

**Expected Outcome:**  
The form should reject blank sources and sources longer than 60 characters, while accepting valid source names within the limit. Amounts up to 9999.99 are valid, but anything zero, negative, or exceeding the digit limit should fail with the right error message. This shows the form catches all edge cases and only allows sensible income entries.

#### Test Results

| Test | Outcome |
|------|---------|
| 1    | Pass    |

---
