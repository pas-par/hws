import time

import pytest
from selenium.webdriver.common.by import By



@pytest.mark.parametrize("items", [('standard_user', 'secret_sauce'),
                                   ('problem_user', 'secret_sauce'),
                                   ('performance_glitch_user', 'secret_sauce')])
def test_auth_positive(driver, items):
    log, password = items
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "user-name").send_keys(f"{log}")
    driver.find_element(By.ID, "password").send_keys(f"{password}")
    driver.find_element(By.ID, "login-button").click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.failed_auth
@pytest.mark.parametrize("items", [('standard_users', 'secret'),
                                   ('problem_', 'sesauce'), ])
def test_auth_negative(driver, items):
    log, password = items
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(1)
    driver.find_element(By.ID, "user-name").send_keys(f"{log}")
    driver.find_element(By.ID, "password").send_keys(f"{password}")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container.error").text
    assert error_message == "Epic sadface: Username and password do not match any user in this service"
