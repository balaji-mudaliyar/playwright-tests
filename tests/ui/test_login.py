from pages.login_page import LoginPage
from playwright.sync_api import Page


def test_login_page_object(page: Page, auth_data) -> None:
    login_page = LoginPage(page)
    login_page.load('https://example.com')

    assert login_page.is_loaded()
    assert auth_data['username'] == 'test_user'
