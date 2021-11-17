import pytest

from tests.base_test import BaseTest


@pytest.mark.test_task
class TestTask(BaseTest):
    """
    Шаги Allure внутри методов
    """

    def test_yandex_measure(self, yandex_page):
        yandex_page.open_yandex()
        yandex_page.click_measure_button()
        assert yandex_page.get_speed() >= 54.23

    def test_login(self, login_page):
        login_page.open_rtmis()
        login_page.authorization(login_page.DATA)
        assert login_page.get_negative_login_message() == 'Успешный вход'
