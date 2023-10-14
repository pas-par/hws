import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'https://www.saucedemo.com/'


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login_by_standard_user(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(f"standard_user")
    driver.find_element(By.ID, "password").send_keys(f"secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield


