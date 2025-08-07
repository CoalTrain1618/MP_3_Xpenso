# Test Cases

## Table of Contents

| Test #    | Feature Tested                      | Expected Behavior                                                      | Status |
|-----------|-------------------------------------|------------------------------------------------------------------------|--------|
| [TC1](#tc1)   | login - account create              | Able to click sign up link and be taken to sign up form page.           | PASS   |
| [TC2](#tc2)   | Create account (invalid)            | Input incorrect account details and attempt to create account.          | PASS   |
| [TC3](#tc3)   | Create account (valid)              | Input correct details and create account                                | PASS   |
| [TC4](#tc4)   | Email Verification (receive)        | Receive email with clickable link                                       | PASS   |
| [TC5](#tc5)   | Email Verification (confirm)        | User can confirm their verification successfully and login              | PASS   |
| [TC6](#tc6)   | Navigation                         | Check all navigation links work                                         | PASS   |
| [TC7](#tc7)   | Dashboard - Get Started modal       | Get Started modal displays and functions                                | PASS   |
| [TC8](#tc8)   | Submit invalid budget form          | Form should not post                                                   | PASS   |
| [TC9](#tc9)   | Submit valid budget form            | Create a budget                                                        | PASS   |
| [TC10](#tc10) | Edit Existing Budget                | User can edit existing budget and save                                  | PASS   |
| [TC11](#tc11) | Delete Budget                       | User can delete budget record                                          | PASS   |
| [TC12](#tc12) | Create invalid Expense              | Expense form will not accept data                                      | PASS   |
| [TC13](#tc13) | Add Expense                         | User can add an expense                                                | PASS   |
| [TC14](#tc14) | Edit Existing Expense               | User can edit existing expense and save record                          | PASS   |
| [TC15](#tc15) | Delete Expense                      | User can delete expense record                                         | PASS   |
| [TC16](#tc16) | Create invalid Income               | Income form will not accept data                                       | PASS   |
| [TC17](#tc17) | Add Income                          | User can add an Income                                                 | PASS   |
| [TC18](#tc18) | Edit Existing Income                | User can edit existing Income and save record                           | PASS   |
| [TC19](#tc19) | Delete Income                       | User can delete income record                                          | PASS   |
| [TC20](#tc20) | Profile page                        | User can see correct data displayed                                    | PASS   |
| [TC21](#tc21) | Profile email change                | User can remove email                                                  | PASS   |
| [TC22](#tc22) | Profile email primary change        | User can select another primary email                                  | PASS   |
| [TC23](#tc23) | Invalid Password Change             | User can't change password                                             | PASS   |
| [TC24](#tc24) | Valid Password Change               | User can change password                                               | PASS   |
| [TC25](#tc25) | Dashboard Summary                   | User can only select from their created budgets                        | PASS   |
| [TC26](#tc26) | Dashboard Summary                   | Selected budget will display user's summarised amounts                 | PASS   |
| [TC27](#tc27) | Dashboard Summary                   | Graph displays visual representation of expense count by category.      | PASS   |
| [TC28](#tc28) | Delete records                      | Deleting budget will delete all related expenses and incomes           | PASS   |
| [TC29](#tc29) | Account deletion                    | User will be able to delete account                                    | PASS   |
| [TC30](#tc30) | Admin Panel                         | Create account and records                                             | PASS   |
| [TC31](#tc31) | Admin Panel                         | Super User will be able to see created user in admin panel -> users    | PASS   |
| [TC32](#tc32) | Admin Panel                         | Super User can view budgets, expenses and incomes for each user        | PASS   |
| [TC33](#tc33) | Admin Panel                         | Super user can edit records in admin panel and user will see changes.  | PASS   |
| [TC34](#tc34) | Admin Panel                         | Super user can create record for user and user can see new addition    | PASS   |
| [TC35](#tc35) | Admin Panel                         | Super user can delete records created by user and user can see changes | PASS   |
| [TC36](#tc36) | Admin Panel                         | Super user can delete users                                            | PASS   |


---

## <a name="tc1"></a>TC1: login - account create

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC1                                                                                     |
| **Feature Tested**| login - account create                                                                  |
| **Expected**      | Able to click sign up link and be taken to sign up form page.                           |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Enter website and click sign up to create account.

**Steps:**

| Step | Action                              | Status |
|------|-------------------------------------|--------|
| 1    | Load Page                           | [x]    |
| 2    | Click sign up link                  | [x]    |
| 3    | Successfully load sign up form page | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc2"></a>TC2: Create account (invalid)

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC2                                                                                     |
| **Feature Tested**| Create account (invalid)                                                                |
| **Expected**      | Input incorrect account details and attempt to create account.                          |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Testing incorrect input into form fields and submit.

**Steps:**

| Step | Action                                         | Status |
|------|------------------------------------------------|--------|
| 1    | Enter Username                                 | [x]    |
| 2    | Enter email without @                          | [x]    |
| 3    | Enter two different passwords in the same form | [x]    |
| 4    | Enter passwords that go against password rules | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc3"></a>TC3: Create account (valid)

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC3                                                                                     |
| **Feature Tested**| Create account (valid)                                                                  |
| **Expected**      | Input correct details and create account                                                |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Testing correct input into signup form fields to create account.

**Steps:**

| Step | Action                                              | Status |
|------|-----------------------------------------------------|--------|
| 1    | Enter username                                      | [x]    |
| 2    | Enter email                                         | [x]    |
| 3    | Enter passwords                                     | [x]    |
| 4    | Submit form and be taken to email verification page | [x]    |

**Notes:**  
All steps successfully passed.

[Back to top](#test-cases)

---

## <a name="tc4"></a>TC4: Email Verification (receive)

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC4                                                                                     |
| **Feature Tested**| Email Verification (receive)                                                            |
| **Expected**      | Receive email with clickable link                                                       |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if verification email is received when user successfully submits the form.

**Steps:**

| Step | Action                                         | Status |
|------|------------------------------------------------|--------|
| 1    | Submit signup form                             | [x]    |
| 2    | Successfully load verification page            | [x]    |
| 3    | Receive custom verification email in time      | [x]    |
| 4    | Link is clickable and redirects to verification page | [x] |

**Notes:**  
All steps successfully passed.

[Back to top](#test-cases)

---

## <a name="tc5"></a>TC5: Email Verification (confirm)

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC5                                                                                     |
| **Feature Tested**| Email Verification (confirm)                                                            |
| **Expected**      | User can confirm their verification successfully and login                              |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if verification confirmation works and user can successfully sign in.

**Steps:**

| Step | Action                                         | Status |
|------|------------------------------------------------|--------|
| 1    | Correct information displays and user can confirm | [x]    |
| 2    | Redirected back to login with the success message | [x]    |
| 3    | User can enter login details and sign in       | [x]    |
| 4    | User is redirected to dashboard                | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc6"></a>TC6: Navigation

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC6                                                                                     |
| **Feature Tested**| Navigation                                                                              |
| **Expected**      | Check all navigation links work                                                         |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test each link re-directs to the correct page.

**Steps:**

| Step | Action                                   | Status |
|------|------------------------------------------|--------|
| 1    | Dashboard link redirects to Dashboard    | [x]    |
| 2    | Budget link redirects to Budget          | [x]    |
| 3    | Expense link redirects to expense page   | [x]    |
| 4    | Income link redirects to income page     | [x]    |
| 5    | Profile link redirects to profile page   | [x]    |
| 6    | Logout link redirects to profile page    | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc7"></a>TC7: Dashboard - Get Started modal

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC7                                                                                     |
| **Feature Tested**| Dashboard - Get Started modal                                                           |
| **Expected**      | Get Started modal displays and functions                                                |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if get started modal correctly displays and functions when used.

**Steps:**

| Step | Action                                    | Status |
|------|-------------------------------------------|--------|
| 1    | Click button to show modal                | [x]    |
| 2    | Content is displayed correctly            | [x]    |
| 3    | Link is interactable                      | [x]    |
| 4    | Link redirects user to create budget page | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc8"></a>TC8: Submit invalid budget form

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC8                                                                                     |
| **Feature Tested**| Submit invalid budget form                                                              |
| **Expected**      | Form should not post                                                                    |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if invalid data can be submitted.

**Steps:**

| Step | Action                            | Status |
|------|-----------------------------------|--------|
| 1    | Input minus value into amount field | [x]    |
| 2    | Fill out remaining form           | [x]    |
| 3    | Submit form                       | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc9"></a>TC9: Submit valid budget form

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC9                                                                                     |
| **Feature Tested**| Submit valid budget form                                                                |
| **Expected**      | Create a budget                                                                         |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to post valid form and create budget.

**Steps:**

| Step | Action                          | Status |
|------|---------------------------------|--------|
| 1    | Submit valid data into form     | [x]    |
| 2    | Save to create budget           | [x]    |
| 3    | User should be redirected to dashboard | [x] |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc10"></a>TC10: Edit Existing Budget

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC10                                                                                    |
| **Feature Tested**| Edit Existing Budget                                                                    |
| **Expected**      | User can edit existing budget and save                                                  |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can edit existing budget and save.

**Steps:**

| Step | Action                                             | Status |
|------|----------------------------------------------------|--------|
| 1    | Click edit button on budget record                 | [x]    |
| 2    | Try saving negative amount                         | [x]    |
| 3    | Input valid data, ensuring different amount to original and save | [x]    |
| 4    | Checked saved amount is updated                    | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc11"></a>TC11: Delete Budget

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC11                                                                                    |
| **Feature Tested**| Delete Budget                                                                           |
| **Expected**      | User can delete budget record                                                           |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can delete existing budget record.

**Steps:**

| Step | Action                                                           | Status |
|------|------------------------------------------------------------------|--------|
| 1    | Create second budget and save                                    | [x]    |
| 2    | Navigate back to budgets page and delete created record          | [x]    |
| 3    | Check budget list to ensure record is deleted                    | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc12"></a>TC12: Create invalid Expense

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC12                                                                                    |
| **Feature Tested**| Create invalid Expense                                                                  |
| **Expected**      | Expense form will not accept data                                                       |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can submit invalid expense form.

**Steps:**

| Step | Action                                                                                | Status |
|------|---------------------------------------------------------------------------------------|--------|
| 1    | Try submitting form with invalid data, one at a time                                  | [x]    |
| 2    | Minus amount, no category selected, no budget selected                                | [x] [x] [x] |
| 3    | Attempt submitting with both 'Save' & 'Add More'                                      | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc13"></a>TC13: Add Expense

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC13                                                                                    |
| **Feature Tested**| Add Expense                                                                             |
| **Expected**      | User can add an expense                                                                 |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Create an expense.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Add required fields                           | [x]    |
| 2    | Submit with add more                          | [x]    |
| 3    | Create another expense and save               | [x]    |
| 4    | On save, user should be redirected to dashboard| [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc14"></a>TC14: Edit Existing Expense

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC14                                                                                    |
| **Feature Tested**| Edit Existing Expense                                                                   |
| **Expected**      | User can edit existing expense and save record                                          |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can edit existing expense and save.

**Steps:**

| Step | Action                                             | Status |
|------|----------------------------------------------------|--------|
| 1    | Click edit button on existing expense record       | [x]    |
| 2    | Try saving negative amount                         | [x]    |
| 3    | Input valid data, ensuring different amount and save| [x]    |
| 4    | Checked saved amount is updated                    | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc15"></a>TC15: Delete Expense

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC15                                                                                    |
| **Feature Tested**| Delete Expense                                                                          |
| **Expected**      | User can delete expense record                                                          |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can delete existing expense record.

**Steps:**

| Step | Action                                                    | Status |
|------|-----------------------------------------------------------|--------|
| 1    | Create second expense and save                            | [x]    |
| 2    | Navigate back to expense page and delete created record   | [x]    |
| 3    | Check expense list to ensure record is deleted            | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc16"></a>TC16: Create invalid Income

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC16                                                                                    |
| **Feature Tested**| Create invalid Income                                                                   |
| **Expected**      | Income form will not accept data                                                        |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can submit invalid Income form.

**Steps:**

| Step | Action                                          | Status |
|------|-------------------------------------------------|--------|
| 1    | Try submitting form with invalid data, one at a time| [x] |
| 2    | Minus amount, no budget selected                | [x] [x]|
| 3    | Attempt submitting with both 'Save' & 'Add More'| [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc17"></a>TC17: Add Income

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC17                                                                                    |
| **Feature Tested**| Add Income                                                                              |
| **Expected**      | User can add an Income                                                                  |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Create an Income.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Add required fields                           | [x]    |
| 2    | Submit with add more                          | [x]    |
| 3    | Create another income and save                | [x]    |
| 4    | On save, user should be redirected to dashboard| [x]   |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc18"></a>TC18: Edit Existing Income

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC18                                                                                    |
| **Feature Tested**| Edit Existing Income                                                                    |
| **Expected**      | User can edit existing Income and save record                                           |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can edit existing Income and save.

**Steps:**

| Step | Action                                             | Status |
|------|----------------------------------------------------|--------|
| 1    | Click edit button on existing Income record        | [x]    |
| 2    | Try saving negative amount                         | [x]    |
| 3    | Input valid data, ensuring different amount and save| [x]    |
| 4    | Checked saved amount is updated                    | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc19"></a>TC19: Delete Income

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC19                                                                                    |
| **Feature Tested**| Delete Income                                                                           |
| **Expected**      | User can delete income record                                                           |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if user can delete existing income record.

**Steps:**

| Step | Action                                                   | Status |
|------|----------------------------------------------------------|--------|
| 1    | Create second income and save                            | [x]    |
| 2    | Navigate back to income page and delete created record   | [x]    |
| 3    | Check income list to ensure record is deleted            | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc20"></a>TC20: Profile page

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC20                                                                                    |
| **Feature Tested**| Profile page                                                                            |
| **Expected**      | User can see correct data displayed                                                     |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if correct user data is displayed to logged in user.

**Steps:**

| Step | Action                                   | Status |
|------|------------------------------------------|--------|
| 1    | Check username is logged in user's username | [x]  |
| 2    | Check Email matches logged in user's email  | [x]  |
| 3    | Log into different account and check again  | [x]  |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc21"></a>TC21: Profile email change

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC21                                                                                    |
| **Feature Tested**| Profile email change                                                                    |
| **Expected**      | User can remove email                                                                   |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User can remove their email and get prompted.

**Steps:**

| Step | Action                                            | Status |
|------|---------------------------------------------------|--------|
| 1    | Remove email on profile page                      | [x]    |
| 2    | User is prompted to add new email                 | [x]    |
| 3    | New email confirmation is sent to email           | [x]    |
| 4    | User can click re-send verification to receive new verification email | [x] |
| 5    | User can confirm the verification                 | [x]    |
| 6    | User's email is back to normal state              | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc22"></a>TC22: Profile email primary change

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC22                                                                                    |
| **Feature Tested**| Profile email primary change                                                            |
| **Expected**      | User can select another primary email                                                   |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User can add email and swap primary email.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Add secondary email to account                | [x]    |
| 2    | User verifies email                           | [x]    |
| 3    | User can highlight and make secondary email primary | [x] |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc23"></a>TC23: Invalid Password Change

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC23                                                                                    |
| **Feature Tested**| Invalid Password Change                                                                 |
| **Expected**      | User can't change password                                                              |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User can't change password.

**Steps:**

| Step | Action                                      | Status |
|------|---------------------------------------------|--------|
| 1    | Input current password                      | [x]    |
| 2    | User can input non-matching passwords       | [x]    |
| 3    | Does not submit                             | [x]    |
| 4    | Retry with matching passwords similar to username | [x] |
| 5    | Will not submit                             | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc24"></a>TC24: Valid Password Change

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC24                                                                                    |
| **Feature Tested**| Valid Password Change                                                                   |
| **Expected**      | User can change password                                                                |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User can change password.

**Steps:**

| Step | Action                          | Status |
|------|---------------------------------|--------|
| 1    | Input current password          | [x]    |
| 2    | Input matching passwords        | [x]    |
| 3    | Submit form to change password  | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc25"></a>TC25: Dashboard Summary

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC25                                                                                    |
| **Feature Tested**| Dashboard Summary                                                                       |
| **Expected**      | User can only select from their created budgets                                         |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User will only be able to select their budget.

**Steps:**

| Step | Action                                | Status |
|------|---------------------------------------|--------|
| 1    | Navigate to dashboard                 | [x]    |
| 2    | Select dropdown                       | [x]    |
| 3    | Ensure only their budgets can be seen | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc26"></a>TC26: Dashboard Summary

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC26                                                                                    |
| **Feature Tested**| Dashboard Summary                                                                       |
| **Expected**      | Selected budget will display user's summarised amounts                                  |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User can see the totals of records relating to the selected user's budget.

**Steps:**

| Step | Action                                | Status |
|------|---------------------------------------|--------|
| 1    | Select budget from drop down          | [x]    |
| 2    | Click calculate to submit form        | [x]    |
| 3    | Ensure totals are displayed           | [x]    |
| 4    | Totals of records match lists for budget | [x] |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc27"></a>TC27: Dashboard Summary

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC27                                                                                    |
| **Feature Tested**| Dashboard Summary                                                                       |
| **Expected**      | Graph displays visual representation of expense count by category.                      |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Ensure graph expense count works and matches actual count.

**Steps:**

| Step | Action                                             | Status |
|------|----------------------------------------------------|--------|
| 1    | Navigate to expense page                           | [x]    |
| 2    | Count how many times categories are assigned       | [x]    |
| 3    | Navigate to dashboard and select the same budget   | [x]    |
| 4    | Match noted expenses against data shown on graph   | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc28"></a>TC28: Delete records

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC28                                                                                    |
| **Feature Tested**| Delete records                                                                          |
| **Expected**      | Deleting budget will delete all related expenses and incomes                            |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User will delete budget and all records relating to the budget will also be deleted.

**Steps:**

| Step | Action                                   | Status |
|------|------------------------------------------|--------|
| 1    | Navigate to budget page                  | [x]    |
| 2    | Delete budget record from list           | [x]    |
| 3    | Check all expenses and incomes deleted   | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc29"></a>TC29: Account deletion

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC29                                                                                    |
| **Feature Tested**| Account deletion                                                                        |
| **Expected**      | User will be able to delete account                                                     |
| **Status**        | PASS                                                                                    |

**Test Description:**  
User will be able to delete their account and will not be able to log back in.

**Steps:**

| Step | Action                                                  | Status |
|------|---------------------------------------------------------|--------|
| 1    | Navigate to profile page                                | [x]    |
| 2    | Start account deletion process                          | [x]    |
| 3    | Finalise deletion by confirmation                       | [x]    |
| 4    | User should be logged out and redirected to sign in page| [x]    |
| 5    | Attempt to login to account                             | [x]    |
| 6    | Login to admin account and check for remnants           | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc30"></a>TC30: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC30                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Create account and records                                                              |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Create account for use in admin panel tests.

**Steps:**

| Step | Action                                          | Status |
|------|-------------------------------------------------|--------|
| 1    | Sign up and create account                      | [x]    |
| 2    | Create two budgets                              | [x]    |
| 3    | Create two expenses for each budget             | [x]    |
| 4    | Create two incomes for each budget              | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc31"></a>TC31: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC31                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Super User will be able to see created user in admin panel -> users                     |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Newly created user will be visible in admin panel users and will have assigned email address.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Navigate to users in admin panel              | [x]    |
| 2    | Check for newly created user                  | [x]    |
| 3    | Check user has assigned email                 | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc32"></a>TC32: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC32                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Super User can view budgets, expenses and incomes for each user                         |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Super User will be able to view all records created by a user.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Navigate to Budget, expenses and incomes      | [x]    |
| 2    | Ensure records in admin panel match users     | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc33"></a>TC33: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC33                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Super user can edit records in admin panel and user will see changes                    |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if admin can edit records, and user will be able to see reflected changes.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Navigate into users records, starting with Income | [x] |
| 2    | Alter data of fields and save                 | [x]    |
| 3    | Log in as user and check if they can see changes | [x] |
| 4    | Repeat for Expenses and budget                | [x]    |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc34"></a>TC34: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC34                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Super user can create record for user and user can see new addition                     |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Test to see if admin can create records for a user, user should be able to see the addition.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Navigate to budget and add a new budget for testuser | [x] |
| 2    | Add budget for 100 amount and September       | [x]    |
| 3    | Navigate to expenses and create an expense    | [x]    |
| 4    | Add expense for utilities for 20 amount and description of water | [x] |
| 5    | Add new Income for user                       | [x]    |
| 6    | Input 30 for amount and Sold item as source   | [x]    |
| 7    | Log into test user and confirm the records exist | [x] |
| 8    | Log in as different user and check creations do not exist for them | [x] |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc35"></a>TC35: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC35                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Super user can delete records created by user and user can see changes                  |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Navigate to Income, Expenses and budget and delete records. Log in as test user and see if changes are reflected.

**Steps:**

| Step | Action                                        | Status |
|------|-----------------------------------------------|--------|
| 1    | Navigate to income list in admin panel        | [x]    |
| 2    | Find previously created Income and delete     | [x]    |
| 3    | Repeat for Expenses and Budget                | [x]    |
| 4    | Log in as test user and see if records have been deleted | [x] |

**Notes:**  
All steps passed.

[Back to top](#test-cases)

---

## <a name="tc36"></a>TC36: Admin Panel

| Field             | Value                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------|
| **Test #**        | TC36                                                                                    |
| **Feature Tested**| Admin Panel                                                                             |
| **Expected**      | Super user can delete users                                                             |
| **Status**        | PASS                                                                                    |

**Test Description:**  
Delete user along with records.

**Steps:**

| Step | Action                                     | Status |
|------|--------------------------------------------|--------|
| 1    | Navigate to users in Admin panel           | [x]    |
| 2    | Delete testuser and confirm deletion       | [x]    |
| 3    | Check admin panel for any testuser records | [x]    |

**Notes:**  
All tests passed.

[Back to top](#test-cases)

----