from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    #Нахождение и нажатие кнопки добавления товара в корзину
    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()
    
    #Проверка добавления товара в корзину
    def guest_can_add_product_to_basket(self):
        self.add_product_to_basket()
        #Вести промокод
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert presented")
        
        self.guest_can_see_message_product_add_to_basket()
        self.guest_can_see_message_price_basket()
        self.guest_can_see_same_product_name()
        self.guest_can_see_correct_price_basket()
        
        
    def guest_can_see_message_product_add_to_basket(self):
        message_product_add_to_basket = self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT)
        assert message_product_add_to_basket, "Product was not add to basket."
        
    def guest_can_see_message_price_basket(self):
        message_price_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_BASKET_PRICE)
        assert message_price_basket, "Cant see basket price."
        
    def guest_can_see_same_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert product_name.text == product_name_in_basket.text, "Product name is not the same"
        
    def guest_can_see_correct_price_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert product_price.text == product_price_in_basket.text, "Price is not correct"