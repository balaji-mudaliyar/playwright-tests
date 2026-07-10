from playwright.sync_api import Page

def test_google_search(page: Page) -> None:
    page.goto("https://www.google.com")

    page.fill('textarea[name="q"]', "Playwright Python")
    page.press('textarea[name="q"]', "Enter")

    page.wait_for_load_state("networkidle")

    assert "Playwright" in page.title()