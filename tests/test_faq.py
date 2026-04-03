import allure
import pytest

from pages.home_page import HomePage
from data import FAQ_CASES


@pytest.mark.parametrize("index, answer_text", FAQ_CASES)
@allure.feature("Главная страница")
@allure.story("Блок FAQ")
class TestFaq:
    @allure.title("Открывается ответ на вопрос FAQ #{index}")
    def test_faq_answers(self, driver, index, answer_text):
        home_page = HomePage(driver)

        with allure.step("Открыть вопрос FAQ"):
            home_page.open_faq_question(index)

        with allure.step("Проверить текст ответа"):
            assert answer_text in home_page.get_faq_answer(index)
