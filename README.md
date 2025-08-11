# MP_3_XpensoLog

## Project Introduction
XpensoLog is a user-friendly, budgeting Django application, designed to make budgeting free and accessible for everyone. The application offers secure account creation and management, ensuring users’ financial data remains private and protected. XpensoLog users can create budgets, track expenses and incomes, and visualize their financial data through a comprehensive dashboard that displays clear insights for each month. XpensoLog is designed with a sleek, modern Fintech style, making it visually appealing and easy to navigate.

Built with user-centric principles, XpensoLog's **C.R.U.D** based design enables users to easily **Create**, **Read**, **Update**, and **Delete** their financial data, providing full control over their experience. The app is developed with a mobile-first approach and is fully responsive across all devices.

## Contents

- [Project Introduction](#project-introduction)
- [Agile Methodology](#agile-methodology)
    - [Overview](#overview)
    - [MoSCoW Prioritisation Technique](#moscow-prioritisation-technique)
    - [GitHub Project Board](#github-project-board)
- [Website Goals & Objectives](#website-goals--objectives)
- [User Stories](#user-stories)
    - [Developer Stories](#developer-stories)
    - [Visitor Stories](#visitor-stories)
- [Epics](#epics)
- [Wireframes Design](#wireframes-design)
- [Database Design](#database-design)
    - [Data Model Description](#data-model-description)
    - [Rationale and Design Decisions](#rationale-and-design-decisions)
- [Design Choices](#design-choices)
    - [Fonts](#fonts)
    - [Colour Scheme](#colour-scheme)
- [Security Measures](#security-measures)
- [XpensoLog Pages](#xpensolog-pages)
    - [Pages Overview](#pages-overview)
- [Admin Portal](#admin-portal)
    - [Admin Panel Design](#admin-panel-design)
- [Automated Email Handling](#automated-email-handling)
    - [Setting Up Email with Gmail for Xpenso](#setting-up-email-with-gmail-for-xpenso)
    - [Steps for Gmail Integration](#steps-for-gmail-integration)
- [Deployment](#deployment)
    - [Deployment process for Heroku](#deployment-process-for-heroku)
- [Testing](#testing)
    - [Automated Testing](#automated-testing)
    - [Manual Testing](#manual-testing)
    - [Code Accessibility Tests](#code-accessibility-tests)
    - [Lighthouse Tests](#lighthouse-tests)
    - [Code Validation](#code-validation)
- [Technologies](#technologies)
    - [Languages](#languages)
    - [Framework](#framework)
    - [Libraries](#libraries)
    - [Tools](#tools)

---




## Agile Methodology
### Overview
- For this project, I plan to utilise the Agile methodology to promote flexibility and ensure steady progress towards a clear objective. Agile development is particularly effective in environments where requirements and ideas evolve throughout the development process. It enables teams to break down large tasks into manageable, iterative steps, fostering continuous improvement and adaptability. This approach allows for quick adjustments in response to changing needs, making it ideal for dynamic project environments.

### MoSCoW Prioritisation Technique
- As part of the project planning process, I will apply the MoSCoW prioritisation technique to help determine the relative importance of features and tasks. This method categorises requirements into four distinct groups: Must Have, Should Have, Could Have, and Won’t Have (at this time). By clearly identifying what is essential versus what is optional or deferrable, this approach supports effective time and resource management, ensuring that critical elements are addressed early in the development cycle.

### GitHub Project Board
- In line with Agile development methodology, I have made extensive use of GitHub’s project board by organising the development process into Epics, which are further broken down into user stories and manageable tasks. I have also utilised the Milestones feature, allowing me to group tasks into Sprint sections, each with a defined due date. By following this structured approach, I aim to maintain effective time management throughout the development of the web application, while also remaining adaptable to any necessary changes.

![Project](./documentation/images/app-pages/projectboard.png)

[Back to top](#contents)

## Website Goals & Objectives
- Empower Users to Manage Personal Finances:
    - Provide tools to help users set monthly budgets and track expenses effectively.
    - Enable categorisation of expenses for better insight into spending habits.

- Promote Financial Awareness and Accountability:
    - Offer clear visual summaries of income, outgoings, and remaining budget.
    - Help users identify areas where they can reduce costs or improve saving.

- Ensure an Intuitive and Accessible Experience:
    - Design a user-friendly interface that is simple, responsive, and accessible on all devices.
    - Minimise friction when inputting data and navigating between budgeting tools.

- Support Ongoing Improvement and Scalability:
    - Follow Agile development practices to iterate based on user feedback.
    - Build a scalable infrastructure capable of handling user growth and feature expansion.

- Prioritise Data Security and User Privacy:
    - Implement secure authentication to protect personal financial information.
    - Comply with data protection standards to ensure users’ privacy and trust.

- Encourage Continued Use and Habit Formation:
    - Provide reminders, insights, and positive feedback to help users stay engaged.
    - Allow users to view progress over time and set personal financial goals.

[Back to top](#contents)

--------------------------------------------------------------------------------------------
## User Stories
Through the implementation of Agile methodology, I created the user stories with the website’s goals and objectives in mind. The result is a well-organised structure of user stories, divided between developer-focused and visitor-focused perspectives. A full list of these is provided below.

### Developer Stories
- [#9](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/9) As a **developer** I want to implement an Agile work method so that I can develop a high quality web application that meets the needs of the user.
- [#10](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/10) As a **developer** I want to design my database ERD to efficiently store and manage my web application content, ensuring optimal performance and flexibility.
- [#11](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/11) As a **developer** I want to ensure the web app is visually engaging and follows a mobile first responsive design so that Users can navigate the website and access relevant information with ease.
- [#12](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/12) As a **developer** I will create Wireframes so that I can visually display my web application's design and structure.
- [#13](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/13) As a **developer** I will set up and configure the Django project so that I can create a secure working environment.
- [#14](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/14) As a **developer** I will implement Django's built in authentication system so that users can securely log in and manage their accounts.
- [#18](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/18) As a **developer**, I want to define the requirements and create the initial Budget and Income models so that the data structure is ready for further development.
- [#19](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/19) As a **developer**, I want to migrate the new models to the database and register them with the Django admin so that they can be managed through the admin interface.
- [#20](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/20) As a **developer**, I want to test the admin panel functionality and write unit tests for the models so that data management is reliable and robust.
- [#21](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/21) As a **developer**, I want to document the models and admin setup so I can document the developing process and future developers can easily understand and maintain the code.
- [#22](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/22) As a **developer**, I want to define the requirements and create the initial Expense and Category models so that the data structure for expense tracking is ready for further development.
- [#23](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/23) As a **developer**, I want to migrate the new Expense and Category models to the database and register them with the Django admin so that they can be managed through the admin interface.
- [#24](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/24) As a **developer**, I want to test the admin panel functionality and write unit tests for the Expense and Category models so that data management is reliable and robust.
- [#25](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/25) As a **developer**, I want to document the models and admin setup for Expense and Category so that future developers can easily understand and maintain the code.
- [#34](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/34) As a **developer**, I can test and polish the site on various devices and browsers so that all users have a smooth experience.
- [#38](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/38) As a **developer**, I can run automated tests for core features so that I am confident the application works as intended.
- [#39](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/39) As a **tester**, I can manually test all user flows so that any bugs or usability issues are identified and fixed before release.
- [#40](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/40) As a **developer**, I can read clear and up-to-date README documentation so that I can understand, set up, and contribute to the project easily.

### Visitor Stories
- [#15](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/15) As a **site user** I want to log in and out of my account each time I visit so my financial data is stored and saved after each visit.
- [#16](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/16) As a **site user** I want to be able to reset my password so if I forget my password I can still recover my account.
- [#17](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/17) As a **site user** I want to have access to a profile management page so that I can edit my information and delete my account if I desire to.
- [#26](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/26) As a **site user** I want to register for an account or log in so that my data is secure and personalised.
- [#27](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/27) As a **site user** I can view a dashboard with my financial summary so that I can quickly understand my budget, income, and expenses at a glance.
- [#28](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/28) As a **site user** I can set and view my budget so that I can plan my finances effectively.
- [#29](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/29) As a **site user** I can add and view income sources so that I can track all my earnings.
- [#30](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/30) As a **site user** I can add, view, and delete expenses and assign categories so that I can analyse my spending habits.
- [#31](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/31) As a **site user** I can use the dashboard and login/registration pages comfortably on any device so that I have a good experience whether on mobile, tablet, or desktop.
- [#32](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/32) As a **site user** I can use well-styled, accessible forms on any device so that I can enter data easily and accurately.
- [#33](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/33) As a **site user** I can navigate the site easily and use assistive technology so that the site is accessible to everyone.
- [#35](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/35) As a **site user** I can see clear success messages after completing actions so that I know when my actions have been successful.
- [#36](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/36) As a **site user** I can see clear error messages when something goes wrong or input is invalid so that I understand what needs to be fixed.
- [#37](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/37) As a **site user** I can only submit valid data in forms so that the site works reliably and prevents mistakes.

## Epics 
The user stories above have been grouped into Epics to align with the Agile methodology. The Epics are as follows:
- [EPIC 1: Project Setup & Planning](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/1)
- [EPIC 2: User Authentication & Access Control](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/2)
- [EPIC 3: Budget and Income Management](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/3)
- [EPIC 4: Expense Tracking & categorisation](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/4)
- [EPIC 5: Dashboard](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/5)
- [EPIC 6: User interface & Responsive Design](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/6)
- [EPIC 7: User Experience Optimisation](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/7)
- [EPIC 8: Quality Assurance & Documentation](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/8)

[Back to top](#contents)

## Wireframes Design
- The wireframe designs serve as an initial blueprint for the website’s layout and user interface. While these designs provide a clear starting point for the placement of key elements across each page, they are intended to be flexible and may evolve throughout development as requirements and user needs become clearer. Creating wireframes has been instrumental in visualising the site’s structure and user flow, as well as aiding the development of the underlying database schema.

**[Wireframes](./documentation/wireframes.md)**

[Back to top](#contents)

## Database Design

- A clear and purposeful data model underpins XpensoLog’s ability to help users organise and track their finances effectively. The Entity Relationship Diagram (ERD) below provides a visual overview of the application’s database structure, showing how different tables interact to support core features such as budgeting, expense logging, and income tracking.

![dbdiagram](./documentation/images/dbdiagram/dbdiagram.png)

This ERD was designed using [dbdiagram.io](https://dbdiagram.io).

### Data Model Description

Here is a technical description of the data model used in XpensoLog:

- **User** 
    - I have used Django's built in User model for user authentication and management. This will be represented as User in the database. It includes fields for username, email, password, and other user-related information. User is a **one-to-many** relationship with Budget, Expenses, and Income, meaning each user can have multiple budgets, expenses, and incomes.

---

#### Budget Model

|  Field Name | Data Type    | Field Arguments |
|-------------|--------------|------------------|
| user_id     | ForeignKey   | User, on_delete=models.CASCADE |
| amount      | DecimalField | max_digits=6, decimal_places=2 |
| date_set    | DateField    | auto_now_add=True |
| month       | IntegerField | choices=MONTH_CHOICES, default=datetime.date.today().month |
| year        | IntegerField | choices=YEAR_CHOICES, default=datetime.date.today().year |

- The **Budget** table stores user-defined budgets, including the amount, date set, month, and year. It has a **many-to-one** relationship with User, meaning each budget belongs to one user, but a user can have multiple budgets.

---

#### Income Model

|  Field Name |   Data Type  | Field Arguments |
|-------------|--------------|------------------|
| user_id     | ForeignKey   | User, on_delete=models.CASCADE |
| amount      | DecimalField | max_digits=6, decimal_places=2 |
| source      | CharField    | max_length=60 |
| date_set    | DateField    | auto_now_add=True |
| budget      | ForeignKey   | Budget, on_delete=models.CASCADE |

- The **Income** table stores user income entries, including the amount, source, date set, and a foreign key linking to the Budget table. It has a **many-to-one** relationship with both the User and Budget tables, meaning each income entry belongs to one user and is associated with one budget, but a user or budget can have multiple income entries.

---

#### Expenses Model

|  Field Name | Data Type    | Field Arguments |
|-------------|--------------|------------------|
| user_id     | ForeignKey   | User, on_delete=models.CASCADE |
| amount      | DecimalField | max_digits=6, decimal_places=2 |
| expense_date| DateField    | default=datetime.date.today |
| description | CharField    | max_length=50, null=True, blank=True |
| date_set    | DateField    | auto_now_add=True |
| category    | ForeignKey   | Category, on_delete=models.CASCADE |
| budget      | ForeignKey   | Budget, on_delete=models.CASCADE |

- The **Expenses** table stores user expenses, including the amount, date of expense, description, date set, and foreign keys linking to the Category and Budget tables. It has a **many-to-one** relationship with the User, Category, and Budget tables—meaning each expense is linked to one user, one category, and one budget, but a user, category, or budget can each have multiple associated expenses.

---

#### Category Model

|  Field Name | Data Type    | Field Arguments |
|-------------|--------------|-----------------|
| name        | CharField    | max_length=60   |

- The **Category** table stores expense categories, including the category name. It is used to classify expenses and does not have a direct relationship with the User or Budget tables—each category can be associated with multiple expenses, but each expense is linked to only one category.

--- 

### Rationale and Design Decisions

- During development, I identified the need to include `month` and `year` fields in the Budget table. This change ensures users can view and analyse their financial data on a monthly or yearly basis. Additionally, linking both Expenses and Incomes to their respective Budget entries (via foreign keys) enables efficient grouping, filtering, and reporting of financial data by time period. These changes were made to make the application more intuitive and to better support typical budgeting workflows.

**The final schema supports:**
- User-specific data segregation and security
- Flexible categorisation of transactions
- Accurate, time-based reporting and data visualisation

This approach to the data model ensures that XpensoLog is robust, scalable, and aligned with the practical needs of personal finance management.

[Back to top](#contents)

## Design Choices

### Fonts
- This application uses [Inter](https://fonts.google.com/specimen/Inter?query=Inter) for most text, giving it a modern and professional appearance that suits financial tools. Inter is chosen for its clarity and ease of reading, helping to make the site accessible for all users. For headings, [Montserrat](https://fonts.google.com/specimen/Montserrat?sort=popularity) is used, creating a clear difference between sections whilst keeping with the fintech style.

### Colour Scheme
![Colour Palette](./documentation/images/app-pages/colours.png)

- The colour scheme for XpensoLog was chosen to create a modern and fintech feel. 

### Categories
- I decided to only include four categories for users to select from when creating an expense. I believe that for the purpose of this project to showcase my skills, including more categories would not add significant value and would only clutter the interface. More categories could be added in the future using the admin panel. So the expansion of this feature is totally possible and ready if necessary.

### Application Name
- When first creating this project, I chose the name **Let’s Talk Money** because it felt approachable for discussing personal finance. However, as the project evolved, I realized that **XpensoLog** better reflects the application's purpose: expense tracking and financial logging. This name also fits much better with the design and branding. Due to the name change, the Django project remains as **Lets-Talk-Money** to avoid complications with the database and migrations, but the application name is now **XpensoLog**.

[Back to top](#contents)

## Security Measures

#### User Authentication

- Django’s `LoginRequiredMixin` is implemented to ensure that users must be logged in to access protected pages. Any unauthenticated requests are redirected to the login screen.

#### Password Management

- Django’s built-in password management system is used to securely hash and store user passwords.
- Strong password requirements are enforced to improve the security of user accounts.

#### Form Validation

- Forms are validated both client-side and server-side. If a user submits incomplete or incorrect information, the form will not be processed and a clear warning message will indicate which field needs attention.

#### Database Security

- Sensitive information such as the database URL and secret key are stored in an `env.py` file, keeping them out of version control and reducing the risk of unauthorised access. This was set up prior to the initial commit to GitHub.
- CSRF (Cross-Site Request Forgery) protection is enabled on all forms to further safeguard user data.

[Back to top](#contents)

## XpensoLog Pages

### Pages Overview

- XpensoLog uses a combination of custom templates and Django Allauth templates to render HTML pages for users. The addition of Allauth provided a robust foundation for authentication, registration, and account management, which made development faster and allowed easy customisation to match the app’s style and workflow. The sections below present the main pages of XpensoLog in the typical order a user would encounter them while navigating through the website.

<details>
<summary><strong>Login Page</strong></summary>
The Sign In page lets users log in securely with their username or email and password. There are links to reset your password or sign up if you’re new. The layout is clean and accessible.
<br>
<img src="./documentation/images/app-pages/sign-in.png" alt="signin" width="375"/>
</details>

<details>
<summary><strong>Sign Up Page</strong></summary>
The Sign Up page lets new users create an account by entering a username, email, and password. Password guidance is shown, and there’s a button to complete registration. Users can also switch easily to the sign in page.
<br>
<img src="./documentation/images/app-pages/sign-up.png" alt="signup" width="375"/>
</details>

<details>
<summary><strong>Forgot Password Page</strong></summary>
The Password Reset page lets users request a password reset by entering their email address. After submitting, a confirmation email is sent. There’s also a link to return to the sign in page.
<br>
<img src="./documentation/images/app-pages/forgot-password.png" alt="password reset" width="350"/>
</details>

<details>
<summary><strong>Email Verification Page</strong></summary>
The Email Verification page asks users to confirm their email address. A verification email is sent with a link to click, and you can change your email if needed.
<br>
<img src="./documentation/images/app-pages/verify-email.png" alt="email verification" width="350"/>
</details>

<details>
<summary><strong>Confirmation Email</strong></summary>
Users receive this email to confirm their address after signing up. Click the link in the email to finish registration and verify your account.
<br>
<img src="./documentation/images/app-pages/custom-email.png" alt="custom email" width="700"/>
</details>

<details>
<summary><strong>Confirm Email Address Page</strong></summary>
The Confirm Email Address page asks users to verify their email address. Click the “Confirm” button if the address is correct. This helps keep accounts secure and avoids mistakes.
<br>
<img src="./documentation/images/app-pages/confirm-email.png" alt="confirm email" width="350"/>
</details>

<details>
<summary><strong>Dashboard</strong></summary>
The Dashboard gives a quick overview of your budgets, incomes, and expenses. Select a budget to view analytics, then press Calculate for details. All totals and a chart by category are displayed for easy tracking.
<br>
<img src="./documentation/images/app-pages/dashboard.png" alt="dashboard" width="350"/>
</details>

<details>
<summary><strong>Navigation Menu</strong></summary>
The Navigation menu provides quick access to Dashboard, Budget, Expenses, Income, Profile, and Logout. It’s easy to find what you need from any page.
<br>
<img src="./documentation/images/app-pages/navigation.png" alt="navigation menu" width="350"/>
</details>

<details>
<summary><strong>Quick Start Guide Modal</strong></summary>
The Quick Start Guide modal greets users and gives a simple overview of how to get started. It explains how to create a budget, track expenses and incomes, and begin managing finances right away.
<br>
<img src="./documentation/images/app-pages/quickstart-modal.png" alt="quick start guide" width="350"/>
</details>

<details>
<summary><strong>Create Budget Page</strong></summary>
The Create Budget page lets users set a budget by entering an amount, month, and year. Budgets can be saved, edited, or deleted easily in the table below the form.
<br>
<img src="./documentation/images/app-pages/budget-create.png" alt="create budget" width="350"/>
</details>

<details>
<summary><strong>Create Expense Page</strong></summary>
The Create Expense page lets users add expenses by entering the date, amount, category, description, and budget. You can save each entry or add more. Existing expenses are listed in a table below, with options to edit or delete.
<br>
<img src="./documentation/images/app-pages/create-expense.png" alt="create expense" width="350"/>
</details>

<details>
<summary><strong>Create Income Page</strong></summary>
The Create Income page lets users add income by entering the amount, source, and budget. Entries appear in a table below, where you can edit or delete each item.
<br>
<img src="./documentation/images/app-pages/create-income.png" alt="create income" width="350"/>
</details>

<details>
<summary><strong>Profile Page</strong></summary>
The Profile page lets users update their username, email, and password. There’s also an option to delete the account under Account Removal.
<br>
<img src="./documentation/images/app-pages/profile.png" alt="profile page" width="350"/>
</details>

<details>
<summary><strong>Manage Email Addresses Page</strong></summary>
The Manage Email Addresses page lets users view, verify, set as primary, or remove email addresses on their account. You can also add a new email address at the bottom.
<br>
<img src="./documentation/images/app-pages/manage-email.png" alt="manage email" width="350"/>
</details>

<details>
<summary><strong>Change Password Page</strong></summary>
The Change Password page allows users to update their password by entering their current password and new password twice. There’s also a link for forgotten passwords.
<br>
<img src="./documentation/images/app-pages/change-password.png" alt="change password" width="350"/>
</details>

<details>
<summary><strong>Delete Account Confirmation Page</strong></summary>
The Delete Account Confirmation page warns users that their account and all data will be permanently deleted if they proceed. It offers options to confirm deletion or cancel.
<br>
<img src="./documentation/images/app-pages/delete-account.png" alt="delete account confirmation" width="350"/>
</details>

<details>
<summary><strong>Sign Out Page</strong></summary>
The Sign Out page asks users to confirm if they want to sign out, with a clear button to complete the action.
<br>
<img src="./documentation/images/app-pages/signout.png" alt="sign out" width="350"/>
</details>

<details>
<summary><strong>Custom 404 Page</strong></summary>
The Custom 404 page ensures continuity of style across the website even when a user is faced with a page not found. This helps the user have a seamless experience, allowing them to easily navigate back into desired pages.
<br>
<img src="./documentation/images/app-pages/404.png" alt="404 page" width="350"/>
</details>

[Back to top](#contents)

## Future Features

- Budget calculations on the dashboard which would take away the total expense amount from the overall budget amount, giving the user a clear view of how much they have left to spend.

- Implementing a dark mode for better user experience during night-time usage.

- Adding a feature to set financial goals and track progress towards them.

- Integrate a feature to export financial data to CSV or PDF for easy sharing and record-keeping.

- Adding in financial tips and resources to better help users manage their finances.

## Admin Portal

### Admin Panel Design
- The admin panel is simple in design, allowing the superuser to navigate easily. All objects are displayed with __str__ which allows the model objects to be easily identifiable. Unlike projects such as blogs, this site doesn't require extensive admin panel use. It still allows the superuser to create, edit and delete data.

<details>
<summary><strong>Admin Panel Overview</strong></summary>

<br>
<img src="./documentation/images/app-pages/admin-overview.png" alt="Admin Panel Overview" width="350"/>
</details>


- The __str__ method is used to display objects in the admin panel, here's an example.

<details>
<summary><strong>Admin Panel Example</strong></summary>

<br>
<img src="./documentation/images/app-pages/admin-layout-example.png" alt="Admin Panel Example" width="350"/>
</details>


[Back to top](#contents)

## Automated Email Handling

### Setting Up Email with Gmail for Xpenso

Xpenso uses Gmail to send important account emails, such as:
- Email verification links (when you sign up or change your email)
- Notifications about password changes

All emails sent by Xpenso include a link for the user to confirm their email address. This helps keep accounts secure and makes sure only the intended user can access their account.

### Steps for Gmail Integration

1. **Make Sure You Have a Gmail Account**  
   You’ll need an active Gmail (Google) account for Xpenso to send emails. Log in or create a new one if needed.

2. **Enable Two-Step Verification on Gmail**  
   - Go to your Google Account (click your profile picture, then **Manage your Google Account**).
   - Open the **Security** tab.
   - In **Signing in to Google**, enable 2-Step Verification and follow the steps.

3. **Create an App Password for Xpenso**  
   - Once 2-Step Verification is set up, stay on the Security page and click **App passwords**.
   - If asked, log in again.
   - Select **Mail** as the app type and **Other (Custom name)** for device (e.g., **Xpenso App**).
   - Click **Generate** to get a 16-character app password. Write this down somewhere safe, as you will not be able to see it again.

4. **Configure Xpenso’s Email Settings**  
   In your project’s environment variables (not in the code), add:
   - `EMAIL_HOST_USER: your Gmail address (e.g., youremail@gmail.com)`
   - `EMAIL_HOST_PASSWORD: the 16-character app password you just generated`

5. **Keep Credentials Safe**  
   Never put your Gmail address or app password directly in your code. Use environment variables or a secrets manager to keep them secure.

With this setup, Xpenso will send account-related emails to your users, helping them verify their email address and manage their account securely.

[Back to top](#contents)

## Deployment

### Deployment process for Heroku

To get this project live on Heroku, follow these steps:

1. Go to the [Heroku website](https://heroku.com) and sign in, or set up a new account if you haven’t got one already.
2. Navigate to your **dashboard**, click the **New** button in the top-right corner and select **Create new app**.
3. Choose a unique name for your app in the **App name** box. Heroku will show a green tick if it’s available.
4. Pick your region (**United States** or **Europe**) to match where most of your users are based.
5. Click **Create app** to continue.
6. Once your app is made, open the **Settings** tab along the top.
7. Find the **Config Vars** section and click **Reveal Config Vars** to access your environment variable settings.
8. Add all required environment variables here (these are usually in your local `env.py`). For this project, set at least:

        - **DATABASE_URL**: xxxx  
        - **SECRET_KEY**: xxxx  
        - **EMAIL_HOST_PASS**: xxxx  
        - **EMAIL_HOST_USER**: xxxx  

    Enter each variable name under **KEY** and its value under **VALUE**.

9. Go to the **Deploy** tab at the top of the page.
10. Under **Deployment method**, select **GitHub**.
11. Use the **Search** box to find your repository, then click **Connect**.
12. Scroll down and hit **Deploy Branch** to start deployment.
13. If you want, you can enable automatic deploys so Heroku will redeploy every time you push to GitHub.
14. Watch the build log at the bottom of the page. Once it’s done, you’ll get a link to your live app.

**Important:**  
- Make sure your Heroku app’s URL is included in the `ALLOWED_HOSTS` list in your `settings.py`.
- Set  `DEBUG = False` for your live site. This is automatically handled via env.
- Double-check that your `requirements.txt` and `Procfile` are both up to date and committed to GitHub before deploying.

[Back to top](#contents)

### To fork the project

Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.


- Log in to **GitHub**.

- Locate the repository.

- Click to open it.

- The fork button is located on the right side of the repository menu.

- To copy the repository to your **GitHub** account, click the button.

  
### To clone the project

- Log in to **GitHub**.

- Navigate to the main page of the repository and click **Code**.

- Copy the **URL** for the repository.

- Open your local **IDE**.

- Change the current working directory to the location where you want the cloned directory.

- Type git clone, and then paste the **URL** you copied earlier.

- Press **Enter** to create your local clone.
  

_Any changes required to the website, they can be made, committed and pushed to GitHub._

[Back to top](#contents)

## Testing

### Automated Testing
- My aim in this project was to implement Test Driven Development. By making use of automated testing, I was able to create robust views and methods to support my app’s functionality. Automated tests also allowed me to put my project under pressure throughout its development, including testing edge cases and ensuring user data isolation. This made sure that users couldn’t access each other’s information, and helped to prevent malicious users from breaking the website.

- Tests can be run with the following command: `python3 manage.py test finances`

#### [Automated Testing Document](./documentation/testing/automated_tests.md)

[Back to top](#contents)

### Manual Testing
- Manual testing was also an important part of this project. I created a CSV file to track and record all my manual tests, as this let me design the layout to suit my needs. Once all the tests were complete, I converted them into a .md file using [tabletomarkdown.com](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/). This produced tables for each test section.

- #### [Manual Testing Document](./documentation/testing/manual_tests.md)

[Back to top](#contents)

### Code Accessibility Tests
- Accessibility testing is a crucial part of the development process, ensuring that XpensoLog can be used by everyone, regardless of ability. By running thorough accessibility checks, I’ve been able to identify and address potential barriers to usability. You can view the full details of these tests and outcomes in the accessibility testing document. Including this section highlights a commitment to creating an inclusive and user-friendly experience.

- #### [Accessibility Testing Document](./documentation/testing/accessibility_testing.md)

[Back to top](#contents)

### Lighthouse Tests
- Lighthouse testing helps to assess the overall quality of a web application, covering key areas such as performance, accessibility, best practices, and SEO. Running Lighthouse audits on XpensoLog’s main pages has enabled me to spot and resolve issues early on, leading to a more robust and efficient site. The results and improvements are documented in the Lighthouse testing section. Including these tests shows a commitment to delivering a high standard of web development.

- #### [Lighthouse Testing Document](./documentation/testing/lighthouse_tests.md)

[Back to top](#contents)

### Code Validation

- Code validation is an important step in maintaining the quality and reliability of XpensoLog. By validating the HTML, CSS, Python, and JavaScript files, I made sure that the code follows best practices and standards, reducing the likelihood of errors and improving overall site performance. Including this section shows a commitment to robust, standards-compliant development.

- #### [Code Validation Document](./documentation/testing/validation_testing.md)

[Back to top](#contents)

## Technologies

### Languages

 - **[Python](https://www.python.org/)**: The primary language used for backend development.
 - **[JavaScript](https://www.javascript.com/)**: Used for frontend interactivity and dynamic content.
 - **[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)**: The standard markup language for creating web pages.
 - **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Used for styling the visual presentation of web pages.

### Framework

- **[Django](https://www.djangoproject.com/)**: The web framework used for building the backend of the application, providing a robust structure for development.

### Libraries

- **[Bootstrap](https://getbootstrap.com/)**: A CSS framework used for responsive design and styling, ensuring the application looks good on all devices.
- **[Chart.js](https://www.chartjs.org/)**: A JavaScript library used for creating interactive charts and graphs to visualise financial data.

[Back to top](#contents)

### Tools

#### Development & Collaboration
- **[GitHub](https://github.com/)**: A platform for version control and collaboration, allowing developers to work together on projects.  
- **[stackoverflow](https://stackoverflow.com/)**: A community-driven Q&A platform used for troubleshooting and finding solutions to coding problems encountered during development.  
- **[gpt-4.1](https://openai.com/research/gpt-4)**: A state-of-the-art language model used for spell checking and grammar correction in the README documentation.  

#### Frontend & User Interface
- **[jQuery](https://jquery.com/)**: A JavaScript library used for simplifying DOM manipulation and event handling.  
- **[crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)**: A Django app that helps to create beautiful forms with minimal effort, improving the user experience.  
- **[crispy-bootstrap5](https://django-crispy-forms.readthedocs.io/en/latest/)**: A Django app that provides Bootstrap 5 support for crispy-forms, making it easy to create responsive and stylish forms.  

#### Design Tools
- **[Google Fonts](https://fonts.google.com/)**: A library of free fonts used to enhance the typography of the application.  
- **[Favicon Generator](https://www.favicon-generator.org/)**: A tool for creating favicons from images, ensuring the app has a recognisable icon.  
- **[coolors](https://coolors.co/)**: A colour scheme generator that helps in creating and exploring colour palettes for the application.  

#### Database & Data Modelling
- **[dbdiagram.io](https://dbdiagram.io/)**: A tool for designing and visualising the database schema, helping to create a clear data model for the application.  
- **[psycopg2-binary](https://www.psycopg.org/)**: A PostgreSQL adapter for Python, used to connect the Django application to a PostgreSQL database.  
- **[dj-database-url](https://github.com/adamchainz/dj-database-url)**: A Django utility for parsing database URLs, making it easier to configure database connections.  
- **[sqlparse](https://github.com/andialbrecht/sqlparse)**: A non-validating SQL parser for Python, used to format and analyse SQL queries.  

#### Deployment & Hosting
- **[Heroku](https://www.heroku.com/)**: A cloud platform used for deploying the web application, providing a scalable environment for hosting.  
- **[gunicorn](https://gunicorn.org/)**: A Python WSGI HTTP server for UNIX, used to serve the Django application in production.  
- **[whitenoise](http://whitenoise.evans.io/en/stable/)**: A Django middleware that serves static files directly from the application, improving performance and simplifying deployment.  

#### Authentication & Security
- **[Django Allauth](https://django-allauth.readthedocs.io/en/latest/)**: A Django app that provides user authentication, registration, and account management features.  


## Acknowledgements

- Special thanks to my mentor, [Eventyret](https://github.com/Eventyret). Who gave me guidance and support throughout the development of this project, helping me to improve my coding skills and becoming a better developer.

- Special thanks to my cohort facilitator, Marko and my fellow students for their support and feedback during the development of this project.



- Special thanks to the contributors of the open-source libraries and tools used in this project.
- Gratitude to the Django community for their extensive documentation and support.
- Appreciation for the developers of Bootstrap and Chart.js for their excellent frameworks that enhanced the UI/UX of the application.

## Contributions
- Both contributors listed for this project are actually myself. I use two systems for development: a Linux desktop and a Linux laptop. When I first committed code from my laptop, I accidentally used the wrong git account because of its global git config. This is why two contributor accounts appear on the project.

[Back to top](#contents)