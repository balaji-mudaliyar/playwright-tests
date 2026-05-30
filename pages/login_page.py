from .base_page import BasePage


class LoginPage(BasePage):
    def load(self, url: str) -> None:
        self.goto(url)

    def is_loaded(self) -> bool:
        return 'Example Domain' in self.page.title()

    def login(self, username: str, password: str) -> None:
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')
