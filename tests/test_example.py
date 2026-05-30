from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.google.com")

        page.fill('textarea[name="q"]', "Playwright Python")
        page.press('textarea[name="q"]', "Enter")

        page.wait_for_load_state("networkidle")

        assert "Playwright" in page.title()

        browser.close()