# MP_3_XpensoLog

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
- [Design Choices](#design-choices)
    - [Fonts](#fonts)
    - [Colour Scheme](#colour-scheme)
    - [Images](#images)
- [Security Measures](#security-measures)

## Project Introduction
XpensoLog is a user-friendly finance budgeting web application that enables users to input their monthly income or budget and track their expenses by category. The app is designed to help users gain better control over their spending habits through clear, interactive features and data visualisation.

This project is being developed as part of Milestone Project 3 and aims to demonstrate my ability to implement full-stack web development concepts — with a strong focus on backend functionality — using Python and the Django framework.

## Agile Methodology
### Overview
For this project, I plan to utilise the Agile methodology to promote flexibility and ensure steady progress towards a clear objective. Agile development is particularly effective in environments where requirements and ideas evolve throughout the development process. It enables teams to break down large tasks into manageable, iterative steps, fostering continuous improvement and adaptability. This approach allows for quick adjustments in response to changing needs, making it ideal for dynamic project environments.

### MoSCoW Prioritisation Technique
As part of the project planning process, I will apply the MoSCoW prioritisation technique to help determine the relative importance of features and tasks. This method categorises requirements into four distinct groups: Must Have, Should Have, Could Have, and Won’t Have (at this time). By clearly identifying what is essential versus what is optional or deferrable, this approach supports effective time and resource management, ensuring that critical elements are addressed early in the development cycle.

### GitHub Project Board
In line with Agile development methodology, I have made extensive use of GitHub’s project board by organising the development process into Epics, which are further broken down into user stories and manageable tasks. I have also utilised the Milestones feature, allowing me to group tasks into Sprint sections, each with a defined due date. By following this structured approach, I aim to maintain effective time management throughout the development of the web application, while also remaining adaptable to any necessary changes.

[INSERT IMAGE OF PROJECT BOARD]

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
### User Stories
Through the implementation of Agile methodology, I created the user stories with the website’s goals and objectives in mind. The result is a well-organised structure of user stories, divided between developer-focused and visitor-focused perspectives. A full list of these is provided below.

#### Developer Stories
- [#9](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/9) As a Developer I want to implement an Agile work method so that I can develop a high quality we application that meets the needs of the user.
- [#10](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/10) As a Developer I want to design my database ERD to efficiently store and manage my web application content, ensuring optimal performance and flexibility.
- [#11](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/11) As a developer I want to ensure the web app is visually engaging and follows a mobile first responsive design so that Users can navigate the website and access relevant information with ease.
- [#12](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/12) As a developer I will create Wireframes so that I can Visually display my web application's design and structure.
- [#13](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/13) As a developer I will set up and configure the Django project so that I can create a secure working environment.
- [#18](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/18) As a developer, I want to define the requirements and create the initial Budget and Income models so that the data structure is ready for further development.
- [#19](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/19) As a developer, I want to migrate the new models to the database and register them with the Django admin so that they can be managed through the admin interface.
- [#20](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/20) As a developer, I want to test the admin panel functionality and write unit tests for the models so that data management is reliable and robust.
- [#21](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/21) As a developer, I want to document the models and admin setup so I can document the developing process and future developers can easily understand and maintain the code.
- [#22](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/22) As a developer, I want to define the requirements and create the initial Expense and Category models so that the data structure for expense tracking is ready for further development.
- [#23](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/23) As a developer, I want to migrate the new Expense and Category models to the database and register them with the Django admin so that they can be managed through the admin interface.
- [#24](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/24) As a developer, I want to test the admin panel functionality and write unit tests for the Expense and Category models so that data management is reliable and robust.
- [#25](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/25) As a developer, I want to document the models and admin setup for Expense and Category so that future developers can easily understand and maintain the code.
- [#38](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/38) As a developer I can run automated tests for core features so that I am confident the application works as intended.
- [#39](github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/39) As a tester I can manually test all user flows so that any bugs or usability issues are identified and fixed before release.
- [#40](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/40) As a developer I can read clear and up-to-date README documentation so that I can understand, set up, and contribute to the project easily.

#### Visitor Stories
- [#14](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/14) As a site user I want to register for an account so I Can create an account for when I revisit this site.
- [#15](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/15) As a Visitor I want to Log in and out of my account each time I visit so my financial data is stored and saved after each visit.
- [#16](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/16) As a User I want to be able to reset my password so If I forget my password I can still recover my account.
- [#17](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/17) As a User I want to have access to a profile management page so that I can edit my information and delete my account if I desire to.
- [#26](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/26) As a user, I want to register for an account or log in so that my data is secure and personalised.
- [#27](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/27) As a user, I can view a dashboard with my financial summary so that I can quickly understand my budget, income, and expenses at a glance.
- [#28](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/28) As a user, I can set and view my budget so that I can plan my finances effectively.
- [#29](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/29) As a user, I can add and view income sources so that I can track all my earnings.
- [#30](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/30) As a user, I can add, view, and delete expenses and assign categories so that I can analyse my spending habits.
- [#31](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/31) As a user I can use the dashboard and login/registration pages comfortably on any device so that I have a good experience whether on mobile, tablet, or desktop.
- [#32](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/32) As a user I can use well-styled, accessible forms on any device so that I can enter data easily and accurately.
- [#33](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/33) As a user I can navigate the site easily and use assistive technology so that the site is accessible to everyone.
- [#34](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/34) As a developer I can test and polish the site on various devices and browsers so that all users have a smooth experience.
- [#35](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/35) As a user I can see clear success messages after completing actions so that I know when my actions have been successful.
- [#36](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/36) As a user I can see clear error messages when something goes wrong or input is invalid so that I understand what needs to be fixed.
- [#37](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/37) As a user I can only submit valid data in forms so that the site works reliably and prevents mistakes.

#### Epics 
The user stories above have been grouped into Epics to align with the Agile methodology. The Epics are as follows:
- [EPIC 1: Project Setup & Planning](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/1)
- [EPIC 2: User Authentication & Access Control](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/2)
- [EPIC 3: Budget and Income Management](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/3)
- [EPIC 4: Expense Tracking & categorisation](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/4)
- [EPIC 5: Dashboard](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/5)
- [EPIC 6: User interface & Responsive Design](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/6)
- [EPIC 7: User Experiance Optimisation](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/7)
- [EPIC 8: Quality Assurance & Documentation](https://github.com/CoalTrain1618/MP_3_Lets-Talk-Money/issues/8)

[Back to top](#contents)

## WireFrames Design
The wireframe designs serve as an initial blueprint for the website’s layout and user interface. While these designs provide a clear starting point for the placement of key elements across each page, they are intended to be flexible and may evolve throughout development as requirements and user needs become clearer. Creating wireframes has been instrumental in visualising the site’s structure and user flow, as well as aiding the development of the underlying database schema.

[Wireframes doc link here]

## Database Design
This database ERD visualises the structure and relationships between the database tables for this web application.

This ERD was designed using [dbdiagram.io](https://dbdiagram.io)

[ERD Design Here]

#### Chnages
While creating the finances models, I made some adjustments to the database schema and the relationships between tables. Initially, the tables did not include any month or year fields. However, I soon realised that adding these fields was necessary to allow users to view financial data specific to a selected month and year. I also decided to link Budget as a Foreign Key to both Expenses and Incomes, making it much easier to group and filter data by month and date.


## Design Choices

#### Fonts 
The font choice for this web application is [Inter](https://fonts.google.com/specimen/Inter?query=Inter), which offers a professional, modern look that fits well with fintech applications. Inter is easy to read and accessible to all users. For headings, I have chosen [Montserrat](https://fonts.google.com/specimen/Montserrat?sort=popularity), providing a clear visual distinction between sections of text while remaining in line with the fintech style.

#### Colour Scheme
[Colour Scheme information here]

#### Images

All images were produced using [Adobe Firefly](https://www.adobe.com/products/firefly.html) with custom prompts. I chose this option to avoid any copyright issues with images.

[Back to top](#contents)

## Security Measures

#### User Authentication

- Django’s `LoginRequiredMixin` is implemented to ensure that users must be logged in to access protected pages. Any unauthenticated requests are redirected to the login screen.
- The `UserPassesTestMixin` is used to restrict certain actions, such as editing or deleting content, so that only the original author has permission. If a user does not meet the required conditions, a 403 Forbidden error is displayed.

#### Password Management

- Django’s built-in password management system is used to securely hash and store user passwords.
- Strong password requirements are enforced to improve the security of user accounts.

#### Form Validation

- Forms are validated both client-side and server-side. If a user submits incomplete or incorrect information, the form will not be processed and a clear warning message will indicate which field needs attention.

#### Database Security

- Sensitive information such as the database URL and secret key are stored in an `env.py` file, keeping them out of version control and reducing the risk of unauthorised access. This was set up prior to the initial commit to GitHub.
- CSRF (Cross-Site Request Forgery) protection is enabled on all forms to further safeguard user data.## Security Measures

[Back to top](#contents)

## Webapp Features

[Features listed here]

#### Custom error page

[custom error page herer]

## Admin Portal

[Admin portal section]

## Testing

[Link testing documentation here]

## Deployment

### Deployment process for Heroku

[Fill in step process of deployment here]


## Technologies

#### Languages

#### Framework

#### Libraries

#### Tools
