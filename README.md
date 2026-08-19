# Python Playwright QA Automation Demo

A personal QA automation project demonstrating UI test automation using Python, Playwright, and pytest.

## Project Overview

This project demonstrates automated testing of the SauceDemo web application using Playwright.

The tests cover:

- Positive login testing
- Negative login testing
- UI element validation
- End-to-end user workflows
- Automated assertions

## Technologies

- Python
- Playwright
- pytest
- GitHub
- GitHub Actions / CI
- HTML test reporting

## Test Coverage

### Homepage Validation

Verifies that:

- The application loads successfully
- Username field is displayed
- Password field is displayed
- Login button is displayed
- Page title is correct

### Successful Login

Verifies that a valid user can:

1. Open the application
2. Enter valid credentials
3. Submit the login form
4. Successfully reach the Products page

### Invalid Login

Verifies that:

1. Invalid credentials are submitted
2. Login is rejected
3. An appropriate error message is displayed

## Project Structure

```text
python-playwright-qa-demo/
│
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   └── test_negative_login.py
│
└── README.md
