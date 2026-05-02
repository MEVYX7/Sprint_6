import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить первый шаг заказа")
    def fill_first_step(self, data):
        self.write(OrderPageLocators.NAME, data["name"])
        self.write(OrderPageLocators.SURNAME, data["surname"])
        self.write(OrderPageLocators.ADDRESS, data["address"])
        self.write(OrderPageLocators.METRO, data["metro"])

        metro_option = (By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{data['metro']}']")
        self.click(metro_option)

        self.write(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить второй шаг заказа")
    def fill_second_step(self, data):
        self.write(OrderPageLocators.DATE, data["date"])
        self.close_date_picker()
        self.open_rent_period_dropdown()
        self.select_rent_period(data["rent_period"])
        self.click((By.ID, data["color"]))
        self.write(OrderPageLocators.COMMENT, data["comment"])

    @allure.step("Создать и подтвердить заказ")
    def create_order(self):
        self.click(OrderPageLocators.CREATE_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить текст попапа об успешном заказе")
    def get_success_popup_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_POPUP)

    @allure.step("Выбрать срок аренды: {period_text}")
    def select_rent_period(self, period_text):
        self.wait_visible_all(OrderPageLocators.RENT_PERIOD_OPTIONS)

        period_option = (By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space(text())='{period_text}']")
        self.click(period_option)

    @allure.step("Закрыть календарь выбора даты")
    def close_date_picker(self):
        self.send_keys(OrderPageLocators.DATE, Keys.ENTER, Keys.ESCAPE)
        self.blur(OrderPageLocators.DATE)
        self.click_body()
        self.wait_invisible(OrderPageLocators.DATE_PICKER_POPUP)

    @allure.step("Открыть выпадающий список срока аренды")
    def open_rent_period_dropdown(self):
        self.scroll_to_center(OrderPageLocators.RENT_PERIOD)
        self.click(OrderPageLocators.RENT_PERIOD)

        if not self.has_elements(OrderPageLocators.RENT_PERIOD_OPTIONS):
            self.click(OrderPageLocators.RENT_PERIOD_PLACEHOLDER)

        self.wait_visible_all(OrderPageLocators.RENT_PERIOD_OPTIONS)
