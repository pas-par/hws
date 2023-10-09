import time

from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("selector", ['item_4_img_link',
                                      'item_2_img_link',
                                      'item_1_img_link',
                                      'item_5_img_link'])
def test_img_click(login_by_standard_user, driver, selector):
    img_selector = selector
    print(img_selector)
    time.sleep(2)
    driver.find_element(By.ID, img_selector).click()
    time.sleep(2)
    assert driver.current_url != "https://www.saucedemo.com/inventory.html"