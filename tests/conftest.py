import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'https://www.saucedemo.com/'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def login_by_standard_user(driver):#request попробовать делать через
    driver.get("https://www.saucedemo.com/")
    # log, password = request.param
    driver.find_element(By.ID, "user-name").send_keys(f"standard_user")
    driver.find_element(By.ID, "password").send_keys(f"secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver