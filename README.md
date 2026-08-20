# Python Playwright QA Automation Demo

A QA automation project demonstrating UI test automation using **Python, Playwright, pytest, and GitHub Actions CI/CD**.

## Project Overview

This project automates testing of the SauceDemo web application using Playwright and Python.

The goal is to demonstrate practical QA automation skills including:

- UI automation
- Positive and negative testing
- Automated assertions
- Regression testing
- Test maintainability
- CI/CD test execution

## Technologies

- Python
- Playwright
- pytest
- GitHub Actions
- Git
- CI/CD

## Test Coverage

### Homepage Validation

Validates:

- Application loads successfully
- Username field is displayed
- Password field is displayed
- Login button is displayed
- Page title is correct

### Successful Login

Validates that a valid user can:

1. Open the application
2. Enter valid credentials
3. Submit the login form
4. Successfully reach the Products page

### Invalid Login

Validates that:

1. Invalid credentials are submitted
2. Login is rejected
3. An appropriate error message is displayed

## Project Structure

```text
python-playwright-qa-demo/
│
├── .github/
│   └── workflows/
│       └── playwright.yml
│
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   └── test_negative_login.py
│
└── README.md
