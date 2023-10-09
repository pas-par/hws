import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com/')

browser.find_element(By.ID, "user-name").send_keys(f"standard_user")
browser.find_element(By.ID, "password").send_keys(f"secret_sauce")
browser.find_element(By.ID, "login-button").click()


items = browser.find_elements(By.CSS_SELECTOR, '.inventory_item')

for item in items:
    link_img = item.find_element(By.CSS_SELECTOR, '.inventory_item_img a').click()
    time.sleep(1)
    assert browser.current_url != 'https://www.saucedemo.com/inventory.html'
    button_back = browser.find_element(By.ID, 'back-to-products').click()
    time.sleep(3)
    items = browser.find_elements(By.CSS_SELECTOR, '.inventory_item')
# links_lst = browser.find_elements(By.CSS_SELECTOR, '.inventory_item a')
#
# for link in links_lst:
#     link_id = link.get_attribute("id").split("_")
#     print(f'id={link_id}')

#как параметр передать массив элементов??? передать как параметры селекторы




