# Automated Testing Document

## Introduction
For this project, I wanted to use Test Driven Development (TDD) to make sure my code works as expected and is easy to maintain. TDD means writing tests before writing the actual code, which helps me think about what each part of the project should do from the start.

Using TDD and automated tests brings a lot of benefits: 
- I can spot mistakes early, before they become bigger problems.
- It’s easier to change or improve my code later, because the tests will catch anything that breaks.
- I spend less time manually checking if things work, since the tests do it for me.
- My project is more reliable and ready for future updates.


### Finances app - Testing Models
I wrote unit tests for all the main models in my finance app, including Budget, Income, Category, and Expenses. These tests check that each model can be created correctly, that relationships between models (like linking an income to a budget or an expense to a category) work as expected, and that the right data is stored in the database.

After running the tests with `python manage.py test finances`, all tests passed successfully. This gives me confidence that the core parts of my app are working as intended and that future changes can be made safely, knowing that the tests will catch any major issues.

### Finance app - Testing Views

#### Initial Test - BudgetView
I want the user to go to the budget_form.html, input amount, month and year. I want them to only see their budget. Upon sumbission, they get redirected, maybe back to dashboard, where the list will be, and a success message.

Test Outcome: Failure 

Expected Outcomes:
- Only logged-in users can access the budget creation page.
- The for display for a GET request.
- Submitting valid data creates a new Budget for the logged in user.
- The user is redirected to the dashboard after submission.
- A success message is displayed.

Test Outcomes:
During the test, three errors were produced. 
- TemplateDoesNotExist: 
    - The template finances/budget_form.html could not be found, causing the test to fail. 
- NoReverseMatch: 
    - The url pattern named 'dashboard' could not be found.
- Dependant test failure:
    - Since two test failed, the proceeding failed.
