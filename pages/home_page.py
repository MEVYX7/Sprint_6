from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def click_order_button(self, place):
        if place == "bottom":
            self.scroll_to(HomePageLocators.BOTTOM_ORDER_BUTTON)
            self.click(HomePageLocators.BOTTOM_ORDER_BUTTON)
        else:
            self.click(HomePageLocators.TOP_ORDER_BUTTON)

    def open_faq_question(self, index):
        self.scroll_to(HomePageLocators.FAQ_BLOCK)
        question = (HomePageLocators.FAQ_QUESTION[0], HomePageLocators.FAQ_QUESTION[1].format(index))
        self.click(question)

    def get_faq_answer(self, index):
        answer = (HomePageLocators.FAQ_ANSWER[0], HomePageLocators.FAQ_ANSWER[1].format(index))
        return self.get_text(answer)

    def click_scooter_logo(self):
        self.click(HomePageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(HomePageLocators.YANDEX_LOGO)

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
