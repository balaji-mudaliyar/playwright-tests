from .base_page import BasePage


class HomePage(BasePage):
    def is_loaded(self) -> bool:
        return self.page.locator('header').is_visible()
