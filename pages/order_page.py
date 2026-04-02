from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def fill_first_step(self, data):
        self.write(OrderPageLocators.NAME, data["name"])
        self.write(OrderPageLocators.SURNAME, data["surname"])
        self.write(OrderPageLocators.ADDRESS, data["address"])
        self.write(OrderPageLocators.METRO, data["metro"])

        metro_option = (By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{data['metro']}']")
        self.click(metro_option)

        self.write(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_step(self, data):
        self.write(OrderPageLocators.DATE, data["date"])
        self.close_date_picker()

        self.open_rent_period_dropdown()

        self.select_rent_period(data["rent_period"])

        self.click((By.ID, data["color"]))
        self.write(OrderPageLocators.COMMENT, data["comment"])

    def create_order(self):
        self.click(OrderPageLocators.CREATE_ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    def get_success_popup_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_POPUP)

    def select_rent_period(self, period_text):
        options_locator = (By.XPATH, "//div[contains(@class,'Dropdown-option')]")
        self.wait.until(EC.visibility_of_all_elements_located(options_locator))
        options = self.driver.find_elements(*options_locator)

        for option in options:
            option_text = option.text.strip().lower()
            if period_text.lower() in option_text:
                self.driver.execute_script("arguments[0].click();", option)
                return

        raise AssertionError(f"Не найдена опция периода: {period_text}")

    def close_date_picker(self):
        date_input = self.driver.find_element(*OrderPageLocators.DATE)
        date_input.send_keys(Keys.ENTER)
        date_input.send_keys(Keys.ESCAPE)
        self.driver.execute_script("arguments[0].blur();", date_input)
        self.driver.execute_script("document.body.click();")

        try:
            self.wait.until(EC.invisibility_of_element_located(OrderPageLocators.DATE_PICKER_POPUP))
        except Exception:
            pass

    def open_rent_period_dropdown(self):
        dropdown = self.wait.until(EC.presence_of_element_located(OrderPageLocators.RENT_PERIOD))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)

        try:
            self.click(OrderPageLocators.RENT_PERIOD)
        except Exception:
            self.driver.execute_script("arguments[0].click();", dropdown)

        options_locator = (By.XPATH, "//div[contains(@class,'Dropdown-option')]")
        if not self.driver.find_elements(*options_locator):
            dropdown_label = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder') and contains(., 'Срок аренды')]")
            try:
                self.click(dropdown_label)
            except Exception:
                pass
