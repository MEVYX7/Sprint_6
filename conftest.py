import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
