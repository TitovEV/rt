import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.url_rtmis = "https://demo.rtmis.ru"
        self.url_yandex = "https://yandex.ru/internet"

    def open_yandex(self):
        with allure.step(f"Переход на {self.url_yandex}"):
            self.driver.get(self.url_yandex)

    def open_rtmis(self):
        with allure.step(f"Переход на {self.url_rtmis}"):
            self.driver.get(self.url_rtmis)

    def find_element(self, locator, times=15):
        return WebDriverWait(self.driver, times).until(ec.presence_of_element_located(locator),
                                                       message=f"Не нашел элемент по {locator}")

    def find_elements(self, locator, times=15):
        return WebDriverWait(self.driver, times).until(ec.presence_of_all_elements_located(locator),
                                                       message=f"Не нашел элементы по {locator}")

    def clickable_element(self, locator):
        WebDriverWait(self.driver, 30) \
            .until(ec.element_to_be_clickable(locator), message=f"{locator} не доступен для клика!")

    def text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 4) \
            .until(ec.text_to_be_present_in_element(locator, text), message=f"{locator} не доступен для клика!")
