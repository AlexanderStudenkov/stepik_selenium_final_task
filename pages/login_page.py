from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "В адресе страницы нет login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы для входа"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Нет формы для регистрации"
        
    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_USER).click()
        time.sleep(3)
        self.should_be_authorized_user()