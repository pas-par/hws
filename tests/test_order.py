from selenium.webdriver.common.by import By


def test_order(driver, login_by_standard_user):
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.ID, 'shopping_cart_container').click()

    driver.find_element(By.NAME, 'checkout').click()

    input1 = driver.find_element(By.ID, 'first-name').send_keys("Petr")
    input2 = driver.find_element(By.ID, 'last-name').send_keys("Med")
    input3 = driver.find_element(By.ID, 'postal-code').send_keys("123123")

    driver.find_element(By.ID, 'continue').click()
    driver.find_element(By.ID, 'finish').click()

    complete_order_massage = driver.find_element(By.CLASS_NAME, 'complete-header').text

    assert complete_order_massage == 'Thank you for your order!'