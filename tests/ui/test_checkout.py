from playwright.sync_api import Page


def test_checkout_process(page: Page) -> None:
    page.goto('https://example.com')
    assert page.locator('h1').text_content() == 'Example Domain'
