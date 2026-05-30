from .base_page import BasePage


class CheckoutPage(BasePage):
    def complete_purchase(self) -> None:
        self.page.click('button.checkout')
        self.page.wait_for_selector('text=Thank you for your order')
