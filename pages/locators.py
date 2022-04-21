from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span.btn-group a.btn.btn-default")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages div:first-child")
    SUCCESS_MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner > p")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    
class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    PRESENCE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    