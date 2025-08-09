# WAVE Accessibility Testing

Accessibility testing is an essential part of web development, helping to ensure that everyone—including people with disabilities—can use and navigate your site effectively. Using the [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/), I checked each page for accessibility issues and made improvements where needed. This process helps to create a more inclusive and user-friendly experience for all visitors.

---

<details>
<summary><strong>login.html</strong></summary>

- **Result:** Initial run failed  
<img src="../images/accessibility-results/wave-login-errors.png" alt="WAVE accessibility errors for login.html" width="550"/>

- **How I fixed it:**  
login.html: Added label elements with related id's above username and password field and changed heading level on sign up.
base.html: changed text to white by removing text muted class.

- **Final result:** Passed  
<img src="../images/accessibility-results/wave-login-passed.png" alt="WAVE accessibility passed for login.html" width="550"/>
</details>