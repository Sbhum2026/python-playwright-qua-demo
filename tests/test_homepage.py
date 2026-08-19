from playwright.sync_api import Page, expect


def test_homepage(page: Page):
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()
