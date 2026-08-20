from playwright.sync_api import Page, expect


def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Username and password do not match"
    )
