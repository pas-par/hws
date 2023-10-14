import time
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("selector", ['item_4_img_link',
                                      'item_2_img_link',
                                      'item_1_img_link'])
def test_click_on_img(login_by_standard_user, driver, selector):
    img_selector = selector
    driver.find_element(By.ID, img_selector).click()
    assert driver.current_url != "https://www.saucedemo.com/inventory.html"


@pytest.mark.parametrize("selector", ['item_0_title_link',
                                      'item_1_title_link',
                                      'item_2_title_link'])
def test_click_on_title(login_by_standard_user, driver, selector):
    title_selector = selector
    driver.find_element(By.ID, title_selector).click()
    assert driver.current_url != "https://www.saucedemo.com/inventory.html"