import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    @allure.step("Инициализировать базовую страницу")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст в поле: {locator}")
    def write(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Отправить клавиши в элемент: {locator}")
    def send_keys(self, locator, *keys):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(*keys)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Прокрутить к центру элемента: {locator}")
    def scroll_to_center(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Снять фокус с элемента: {locator}")
    def blur(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].blur();", element)

    @allure.step("Кликнуть по body")
    def click_body(self):
        self.click((By.TAG_NAME, "body"))

    @allure.step("Дождаться, что URL содержит: {text}")
    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на последнюю вкладку браузера")
    def switch_to_last_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться видимости всех элементов: {locator}")
    def wait_visible_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Найти все элементы: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Проверить наличие элементов: {locator}")
    def has_elements(self, locator):
        return len(self.find_elements(locator)) > 0

    @allure.step("Дождаться, что элемент станет невидимым: {locator}")
    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
