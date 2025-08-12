# WAVE Accessibility Testing

Accessibility testing is an essential part of web development, helping to ensure that everyone—including people with disabilities—can use and navigate your site effectively. Using the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/), I checked each page for accessibility issues and made improvements where needed. This process helps to create a more inclusive and user-friendly experience for all visitors.

---

## Tests

### Points

- Whilst running accessibility tests, one alert persisted across all pages. This alert existed because both the dashboard nav link and the XpensoLog logo navigate users back to the dashboard. This is intentional: when the nav links collapse, the user can still click the logo to return to the dashboard.

<details>
<summary><strong>login.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/accessibility-results/wave-login-errors.png" alt="WAVE accessibility errors for login.html" width="400"/>

- **How I fixed it:**  
login.html: Added label elements with related IDs above username and password fields and changed heading level on Sign Up.  
base.html: Changed text to white by removing the 'text-muted' class.

- **Final result:** Passed  
<img src="../images/accessibility-results/wave-login-passed.png" alt="WAVE accessibility passed for login.html" width="400"/>
</details>

<details>
<summary><strong>signup.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/accessibility-results/wave-signup-errors.png" alt="WAVE accessibility errors for signup.html" width="400"/>

- **How I fixed it:**  
    - Added labels to HTML template.
    - Changed heading level.
    - The link is not redundant; it is needed for user flow, so the alert was not addressed.

- **Final result:** Passed  
<img src="../images/accessibility-results/wave-signup-passed.png" alt="WAVE accessibility passed for signup.html" width="400"/>
</details>

<details>
<summary><strong>password_reset.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-password_reset-passed.png" alt="WAVE accessibility passed for password_reset.html" width="400"/>
</details>

<details>
<summary><strong>password_reset_done.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-password_reset_done.png" alt="WAVE accessibility passed for password_reset_done.html" width="400"/>
</details>

<details>
<summary><strong>password_reset_from_key.html</strong></summary>

**Result:** Initial run failed
 

- **Result:** Passed  
<img src="../images/accessibility-results/wave-password_reset_key_done-pass.png" alt="WAVE accessibility passed for password_reset_from_key_done.html" width="400"/>
</details>

<details>
<summary><strong>password_reset_done.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-password_reset_done.png" alt="WAVE accessibility passed for password_reset_done.html" width="400"/>
</details>

<details>
<summary><strong>verify_email_required.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-verify_email-passed.png" alt="WAVE accessibility passed for verify_email_required.html" width="400"/>
</details>

<details>
<summary><strong>email_confirm.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-confirm_email-passed.png" alt="WAVE accessibility passed for email_confirm.html" width="400"/>
</details>

<details>
<summary><strong>dashboard.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-dashboard-pass.png" alt="WAVE accessibility passed for dashboard.html" width="400"/>

- **Alerts:**
    - During the accessibility test for the dashboard, an alert for a skipped heading was apparent. However, after investigation, the error was not visible on the page. Because there was no visual indication of the error and it also did not affect the page, this was not addressed.

- **Alert:** Unknown  
<img src="../images/accessibility-results/wave-dashboard-alerts.png" alt="WAVE accessibility passed for dashboard.html" width="400"/>
</details>

<details>
<summary><strong>budget_form.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-budget-pass.png" alt="WAVE accessibility passed for budget_form.html" width="400"/>
</details>

<details>
<summary><strong>expense_form.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-expenses-pass.png" alt="WAVE accessibility passed for expense_form.html" width="400"/>
</details>

<details>
<summary><strong>income_form.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-income-pass.png" alt="WAVE accessibility passed for income_form.html" width="400"/>
</details>

<details>
<summary><strong>profile.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-profile-pass.png" alt="WAVE accessibility passed for profile.html" width="400"/>
</details>

<details>
<summary><strong>email.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-email-pass.png" alt="WAVE accessibility passed for email.html" width="400"/>
</details>

<details>
<summary><strong>password_change.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-password_change-pass.png" alt="WAVE accessibility passed for password_change.html" width="400"/>
</details>

<details>
<summary><strong>delete_user.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-delete_user-pass.png" alt="WAVE accessibility passed for delete_user.html" width="400"/>
</details>

<details>
<summary><strong>logout.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-logout-pass.png" alt="WAVE accessibility passed for logout.html" width="400"/>
</details>

<details>
<summary><strong>404.html</strong></summary>

- **Result:** Passed  
<img src="../images/accessibility-results/wave-404-pass.png" alt="WAVE accessibility passed for 404.html" width="400"/>
</details>