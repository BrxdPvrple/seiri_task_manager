# Seiri Task Manager

Seiri is a task manager app created using the flask framework and written in python.

## Contents:

- [Project Brief](#Project-Brief)
- [Application Design](#Application-Design)
- [Application](#Application)
- [Risk Assessment](#Risk-Assessment)
- [Testing](#Testing)
- [The App](#The-App)
- [Latest Updates](#Updates)
- [Known Issues](#Known-Issues)
- [Future Development](#Future-Development)

## Project Brief

## Product Requirements

## Application Design

## Application

## Tech Stack

## Risk Assessment

## Testing

## Latest Updates

- 10/11/2021:

  - Navbar links all redirect to the login page when user not signed in.

  - Changed users table properties for username and email to both be unique.

- 11/11/2021:

  - Login button switches to logout when user signed in.

- 12/11/2021:

  - Logo href used to always redired to landing page, now redirected to dashboard when logged in.

- 13/11/2021:
  - Changed background and improved styling.
    ![before](https://github.com/BrxdPvrple/seiri_task_manager/blob/main/documents/Task%20Management%20Hub.png)
    ![after](https://github.com/BrxdPvrple/seiri_task_manager/blob/main/documents/Tasks_Final.png)

## Known Issues

- Able to edit and delete tasks from other accounts if task id is known by manipulating the url.
- Edit tasks function doesn't prefill text with current task name and description.
- Not yet optimized for mobile browsers.
- Stack trace error is thrown when tyring to enter duplicate details; needs try/except statements to catch erros and prompt users to input a new username or email.

## Future Development

- Add a footer to layout.html.
- Improve the dashboard.
- Implement a dark mode feature
- Flash messaging for login/logout and tasks deleted
- Add completion dates and check boxes to tasks
- New table for completed tasks
- Add account management to allow users to change username/email/password and delete account
