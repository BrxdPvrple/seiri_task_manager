# Seiri Task Manager

Seiri is a task manager app created using the flask framework and written in python.

## Contents:

- [Project Brief](#Project-Brief)
- [Product Requirements](#Product-Requirements)
- [App Design](#Appl-Design)
- [Application](#Application)
- [Tech Stack](#Tech-Stack)
- [Testing](#Testing)
- [Risk Assessment](#Risk-Assessment)
- [Latest Updates](#Updates)
- [Known Issues](#Known-Issues)
- [Future Development](#Future-Development)

## Project Brief

The aim of this project was to create a CRUD web application written in python and using the Flask web microframework. The web application also requires a database with at least two tables showing a one-to-many relationship. This application then needed to be deployed to a cloud server and continuous integration is needed to display knowledge of core DevOps principles and agile methodologies.

## Product Requirements

During the pre-planning stages of my project I wrote up a very brief software requirements specification before any actual development began.

![SRS](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/SRS%20Screenshot.png)

I later expanded upon this SRS by creating a more in depth product requirements document using the project pages feature on Jira.
![STM1](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/STM-2021-11-08Productrequirements-131121-1451-1.jpg)
![STM2](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/STM-2021-11-08Productrequirements-131121-1451-2.jpg)
![STM3](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/STM-2021-11-08Productrequirements-131121-1451-3.jpg)

The product requirements can be viewed in full here.
[Product Requitements PDF](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/STM-2021-11-08Productrequirements-131121-1451.pdf)

## Application Design

For my project I decided to create a task manager app that allows users to input new tasks, edit and delete them (CRUD functionality). The app utilises a SQL database with two tables that share a one-to-many relationship as illustrated in the entity relashionship diagram below.

![ERD](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Entity%20Relationship%20Diagram.png)

Upon connecting to the site the home page provides you with a button to sign up, at this stage all other links will redirect you to the login page and the Logo redirects you back to the homepage. Upon creating an account you will then be able to login and the apps features now become accesible to the user. The website navigation structure is illustrated below.

![Webpages](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Webpage%20Flow%20Chart.png)

## Application

#### Landing Page

![Landing](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Landing.png)

#### Sign Up Form

![Signup](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Signup_Final.png)

#### Login Form

![Login](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Login_Final.png)

#### Dashboard

![Dashboard](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Dashboard_Final.png)

#### Task Management Hub

![Tasks](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Tasks_Final.png)

#### Adding a Task

![Add](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Add_Task.png)

#### Updating a Task

![Edit](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Update_Task.png)

#### Account Management Hub

![Accounts](https://github.com/BrxdPvrple/seiri_task_manager/blob/feature/documents/Account.png)

## Tech Stack

## Testing

## Risk Assessment

## Latest Updates

- 10/11/2021:

  - Navbar links all redirect to the login page when user not signed in.

  - Changed users table properties for username and email to both be unique.

- 11/11/2021:

  - Login button switches to logout when user signed in.

- 12/11/2021:

  - Logo href used to always redired to landing page, now redirected to dashboard when logged in.

  - Changed background and improved styling.
    ![before](https://github.com/BrxdPvrple/seiri_task_manager/blob/main/documents/Task%20Management%20Hub.png)
    ![after](https://github.com/BrxdPvrple/seiri_task_manager/blob/main/documents/Tasks_Final.png)

## Known Issues

- Able to edit and delete tasks from other accounts if task id is known by manipulating the url.
- Passwords currently unsafe via HTTP and require HTTPS for end to end encryption.
- Edit tasks function doesn't prefill text with current task name and description.
- Not yet optimized for mobile browsers.
- Stack trace error is thrown when tyring to enter duplicate details; needs try/except statements to catch erros and prompt users to input a new username or email.

## Future Development

- Include an SSL Certificate for HTTPS.
- Add a footer to layout.html.
- Improve the dashboard.
- Implement a dark mode feature.
- Flash messaging for login/logout and tasks deleted.
- Add completion dates and check boxes to tasks.
- New table for completed tasks.
- Add account management to allow users to change username/email/password and delete account.
