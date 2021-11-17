import allure
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.DATA = 'autotest_123'
        self.LOGIN = (By.XPATH, '//input[@id = "promed-login"]')
        self.PASSWORD = (By.XPATH, '//input[@id = "promed-password"]')
        self.AUTH_SUBMIT = (By.XPATH, '//button[@id = "auth_submit"]')
        self.LOGIN_MESSAGE = (By.XPATH, '//span[@id = "login-message"]')

    def enter_login(self, value):
        with allure.step('Ввод логина'):
            self.find_element(self.LOGIN).send_keys(value)

    def enter_password(self, value):
        with allure.step('Ввод пароля'):
            self.find_element(self.PASSWORD).send_keys(value)

    def click_auth_submit(self):
        with allure.step('Нажатие на кнопку "Войти"'):
            self.find_element(self.AUTH_SUBMIT).click()

    def get_negative_login_message(self):
        with allure.step("Получение текста ошибки авторизации"):
            self.text_to_be_present_in_element(self.LOGIN_MESSAGE, 'Ошибка авторизации')
            return self.find_element(self.LOGIN_MESSAGE).text

    def authorization(self, value):
        self.enter_login(value)
        self.enter_password(value)
        self.click_auth_submit()

