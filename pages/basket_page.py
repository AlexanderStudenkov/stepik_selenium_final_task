from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def guest_can_see_message_basket_is_empty(self):
        message = "Your basket is empty."
        message_basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert message in message_basket_empty.text, "Basket not empty."

    def guest_cant_see_product_in_basket(self):
        presence_product_in_basket = self.is_not_element_present(*BasketPageLocators.PRESENCE_PRODUCT_IN_BASKET)
        assert presence_product_in_basket, "Product in the basket"
