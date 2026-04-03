import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step("Нажать кнопку 'Заказать' в зоне: {place}")
    def click_order_button(self, place):
        if place == "bottom":
            self.scroll_to(HomePageLocators.BOTTOM_ORDER_BUTTON)
            self.click(HomePageLocators.BOTTOM_ORDER_BUTTON)
        else:
            self.click(HomePageLocators.TOP_ORDER_BUTTON)

    @allure.step("Открыть вопрос FAQ с индексом: {index}")
    def open_faq_question(self, index):
        self.scroll_to(HomePageLocators.FAQ_BLOCK)
        question = (HomePageLocators.FAQ_QUESTION[0], HomePageLocators.FAQ_QUESTION[1].format(index))
        self.click(question)

    @allure.step("Получить ответ FAQ с индексом: {index}")
    def get_faq_answer(self, index):
        answer = (HomePageLocators.FAQ_ANSWER[0], HomePageLocators.FAQ_ANSWER[1].format(index))
        return self.get_text(answer)

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(HomePageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(HomePageLocators.YANDEX_LOGO)

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.switch_to_last_tab()
