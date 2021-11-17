import allure
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class YandexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.MEASURE_BUTTON = (By.XPATH, '//button[span[text()="Измерить"]]')
        self.MEASURE_AGAIN_BUTTON = (By.XPATH, '//button[span[text()="Измерить ещё раз"]]')
        self.QUANTITY_MBIT = \
            (By.XPATH, '//div[contains(@class, "detailed")][preceding-sibling::h3[text()="Входящее соединение"]]')

    def get_speed(self):
        with allure.step("Получение актуально скорости входящего соединения"):
            self.wait_measure_again_button()
            text = self.find_element(self.QUANTITY_MBIT).text
        return float(text.split(" ")[0])

    def click_measure_button(self):
        with allure.step("Клик на кнопку 'Измерить'"):
            self.find_element(self.MEASURE_BUTTON).click()

    def wait_measure_again_button(self):
        with allure.step("Ожидание кнопки 'Измерить ещё раз'"):
            self.clickable_element(self.MEASURE_AGAIN_BUTTON)
