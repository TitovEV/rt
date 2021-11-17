import os

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page.login_page import LoginPage
from page.yandex_page import YandexPage


@pytest.fixture(scope="class")
def browser(request):
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument("--start-maximized")
    options_chrome.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options_chrome)
    request.cls.driver = driver
    yield request.cls.driver
    request.cls.driver.close()
    request.cls.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='error',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture
def login_page(browser) -> LoginPage:
    return LoginPage(browser)


@pytest.fixture
def yandex_page(browser) -> YandexPage:
    return YandexPage(browser)
