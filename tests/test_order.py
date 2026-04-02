import pytest
import allure

from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils import Utils


@pytest.mark.parametrize(
    "entry_point, metro, date, rent_period, color",
    [
        ("top", "Сокольники", "15.04.2026", "сутки", "black"),
        ("bottom", "Черкизовская", "16.04.2026", "двое суток", "grey"),
    ],
)
@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий")
class TestOrder:
    @allure.title("Успешный заказ через кнопку: {entry_point}")
    def test_successful_order(self, driver, entry_point, metro, date, rent_period, color):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        order_data = {
            "name": Utils.generate_name(),
            "surname": Utils.generate_last_name(),
            "address": Utils.generate_address(),
            "metro": metro,
            "phone": Utils.generate_phone_number(),
            "date": date,
            "rent_period": rent_period,
            "color": color,
            "comment": "тест",
        }

        with allure.step("Открыть форму заказа"):
            home_page.click_order_button(entry_point)

        with allure.step("Заполнить форму заказа"):
            order_page.fill_first_step(order_data)
            order_page.fill_second_step(order_data)

        with allure.step("Подтвердить заказ"):
            order_page.create_order()

        with allure.step("Проверить успешное оформление"):
            assert "Заказ оформлен" in order_page.get_success_popup_text()
