from selenium.webdriver.common.by import By
import pytest

def test_logout_button(driver, login_by_standard_user):
    driver.implicitly_wait(2)
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    driver.find_element(By.ID, 'logout_sidebar_link').click()

    assert driver.current_url == 'https://www.saucedemo.com/'


def test_about_button(driver, login_by_standard_user):
    driver.implicitly_wait(2)
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    driver.find_element(By.ID, 'about_sidebar_link').click()

    assert driver.current_url == 'https://saucelabs.com/'


def test_resset_state_button(driver, login_by_standard_user):
    driver.implicitly_wait(2)
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    driver.find_element(By.ID, 'shopping_cart_container').click()

    elements_in_cart_before_resset = len(driver.find_elements(By.CLASS_NAME, 'cart_item'))
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    driver.find_element(By.ID, 'reset_sidebar_link').click()
    driver.refresh()
    elements_in_cart_after_resset = len(driver.find_elements(By.CLASS_NAME, 'cart_item'))

    assert elements_in_cart_before_resset != elements_in_cart_after_resset
    assert elements_in_cart_after_resset == 0