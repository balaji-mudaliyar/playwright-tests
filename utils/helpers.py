from playwright.sync_api import Page


def take_screenshot(page: Page, path: str) -> None:
    page.screenshot(path=path)
