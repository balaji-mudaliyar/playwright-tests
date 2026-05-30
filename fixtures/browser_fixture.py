from playwright.sync_api import sync_playwright


def browser_fixture():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
