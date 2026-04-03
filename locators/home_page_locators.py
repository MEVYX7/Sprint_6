from selenium.webdriver.common.by import By


class HomePageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    FAQ_BLOCK = (By.CLASS_NAME, "Home_FourPart__1uthg")
    FAQ_QUESTION = (By.ID, "accordion__heading-{}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{}")

    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
