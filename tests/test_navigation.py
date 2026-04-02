import allure

from pages.home_page import HomePage
from urls import Urls


@allure.feature("Навигация")
class TestNavigation:
    @allure.story("Логотип Самоката")
    @allure.title("Переход на главную по клику на логотип Самоката")
    def test_scooter_logo_redirects_to_home(self, driver):
        home_page = HomePage(driver)

        with allure.step("Открыть страницу заказа"):
            home_page.click_order_button("top")

        with allure.step("Нажать на логотип Самоката"):
            home_page.click_scooter_logo()

        with allure.step("Проверить URL главной"):
            assert driver.current_url.startswith(Urls.BASE_URL)

    @allure.story("Логотип Яндекса")
    @allure.title("Переход на Дзен по клику на логотип Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        home_page = HomePage(driver)

        with allure.step("Нажать на логотип Яндекса"):
            home_page.click_yandex_logo()
            home_page.switch_to_new_tab()
            home_page.wait_url_contains("dzen.ru")

        with allure.step("Проверить URL Дзена"):
            assert "dzen.ru" in driver.current_url
