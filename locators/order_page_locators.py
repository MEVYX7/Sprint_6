from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_POPUP = (By.CLASS_NAME, "react-datepicker")
    RENT_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    CREATE_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    SUCCESS_POPUP = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
