## Code Validation

### HTML  

<sub>All HTML files were validated using the [W3C Markup Validation Service](https://validator.w3.org/).</sub>

<details>
<summary><strong>login.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-login-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>signup.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/validation-results/html-signup-error-validation.png" alt="" width="550"/>

- **How I fixed it:**  
Added ID to respective password helper and then replaced the password helper small element with a div.

- **Final result:** Passed  
<img src="../images/validation-results/html-signup-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>Verified_email_required.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-verified_email_required-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>dashboard.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/validation-results/html-dashboard-error-validation.png" alt="" width="550"/>

- **How I fixed it:**  
    - Closed open ul.
    - Closed div
    - removed stray p element
    - Changed capital P to lowercase p on element

- **Final result:** Passed  
<img src="../images/validation-results/html-dashboard-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>budget_form.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-budget-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>expense_form.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-expense-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>income_form.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-income-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>profile.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-profile-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>email.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-email-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>password_change.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/validation-results/html-password_change-error-validation.png" alt="" width="550"/>

- **How I fixed it:**  
    - id_password1_helptext ID missing a related element. Added if satement for password helper
    and added the missing ID.

- **Final result:** Passed  
<img src="../images/validation-results/html-password_change-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>password_reset.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/validation-results/html-password_reset-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>delete_user.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-delete_user-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>logout.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-logout-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>404.html</strong></summary>

- **Result:** Passed
<img src="../images/validation-results/html-404-validation.png" alt="" width="550"/>
</details>

---

### CSS 

<sub>All CSS files were validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).</sub>

<details>
<summary><strong>style.css</strong></summary>

- **Result:** Passed  
<img src="../images/validation-results/css-validation.png" alt="" width="550"/>

</details>



---

### JavaScript

<sub>All JavaScript files were checked using [JSHint](https://jshint.com/).</sub>

<details>
<summary><strong>main.js</strong></summary>

- **Result:** Passed with warning shown
<img src="../images/validation-results/js-validation.png" alt="" width="550"/>

- **Warning:**  
JS Hint presented a warning, however the warning is irrelevant, since 'new' is needed for chart.js, therefore ignored warning.
</details>



---

### Python

<sub>All Python files were checked using [Code Institute's Python Linter (PEP8CI)](https://pep8ci.herokuapp.com/).</sub>

 #### Finances App - Python Files
<details>
<summary><strong>finances/views.py</strong></summary>

- **Result:** Passed  
<img src="../images/validation-results/finances-views-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>finances/urls.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/finances-urls-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>finances/tests.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/finances-tests-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>finances/models.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/finances-models-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>finances/forms.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/finances-forms-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>finances/apps.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/finances-apps-validation.png" alt="" width="550"/>
</details>

<details>
<summary><strong>finances/admin.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/finances-admin-validation.png" alt="" width="550"/>
</details>

#### Let's Talk Money Project - Python Files

<details>
<summary><strong>letstalkmoney/urls.py</strong></summary>

- **Result:** Passed 
<img src="../images/validation-results/letstalkmoney-urls-validation.png" alt="" width="550"/>
</details>