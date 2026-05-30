import pytest
from playwright.sync_api import sync_playwright

from config.settings import get_config


@pytest.fixture(scope='session')
def config() -> dict:
    return get_config()


@pytest.fixture(scope='session')
def playwright_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def browser_context(playwright_browser):
    context = playwright_browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope='function')
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture()
def auth_data() -> dict:
    return {
        'username': 'test_user',
        'password': 'secret123'
    }
