
from selenium.webdriver.common.by import By
import pytest


# add item to cart from catalog
@pytest.mark.parametrize("selectors", [("add-to-cart-sauce-labs-backpack", 'remove-sauce-labs-backpack'),
                                       ("add-to-cart-sauce-labs-bike-light", 'remove-sauce-labs-bike-light')])
def test_add_to_cart(driver, login_by_standard_user, selectors):
    add_button, remove_button = selectors
    driver.implicitly_wait(2)

    button = driver.find_element(By.ID, add_button)
    add_to_cart_button_text = button.text
    button.click()

    remove_button_text = driver.find_element(By.ID, remove_button).text
    shopping_cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')

    assert shopping_cart_badge.is_displayed()
    assert add_to_cart_button_text != remove_button_text


# remove item from cart
@pytest.mark.parametrize("selectors", ["add-to-cart-sauce-labs-backpack",
                                       "add-to-cart-sauce-labs-bike-light"])
def test_remove_from_cart(driver, login_by_standard_user, selectors):
    driver.implicitly_wait(2)
    add_button = selectors
    # click on add to cart button
    driver.find_element(By.ID, add_button).click()
    # switch to cart
    driver.find_element(By.ID, 'shopping_cart_container').click()
    elements_before_delete = driver.find_elements(By.CLASS_NAME, 'cart_item')
    # delete element
    driver.find_element(By.CSS_SELECTOR, '.cart_button').click()
    elements_after_delete = driver.find_elements(By.CLASS_NAME, 'cart_item')

    assert len(elements_before_delete) > len(elements_after_delete)


# add item to cart from card
def test_add_to_cart_from_card(driver, login_by_standard_user):
    driver.implicitly_wait(2)
    # find button and click
    driver.find_element(By.CSS_SELECTOR, '.btn_inventory').click()
    # get button text after click
    button_text_after_click = driver.find_element(By.CSS_SELECTOR, '.btn_inventory').text

    shopping_cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')

    assert shopping_cart_badge.is_displayed()
    assert button_text_after_click == 'remove'


# remove item to cart from card
def test_remove_to_cart_from_card(driver, login_by_standard_user):
    driver.implicitly_wait(2)
    # find button add to cart anc click
    driver.find_element(By.CSS_SELECTOR, '.btn_inventory').click()
    # find button remove and click
    driver.find_element(By.CSS_SELECTOR, '.btn_inventory').click()
    # get button text
    button_text = driver.find_element(By.CSS_SELECTOR, '.btn_inventory').text

    assert button_text == 'Add to cart'

