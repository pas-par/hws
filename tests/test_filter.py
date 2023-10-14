

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



def test_filter_by_a_to_z(driver, login_by_standard_user):
    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    heading_text_list = [element.text for element in item_list]
    sorted_heading_text_list = sorted(heading_text_list)

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('az')

    after_filter_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    filtered_heading_text_list = [element.text for element in after_filter_list]

    assert sorted_heading_text_list == filtered_heading_text_list


def test_filter_by_z_to_a(driver, login_by_standard_user):
    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    heading_text_list = [element.text for element in item_list]
    sorted_heading_text_list = sorted(heading_text_list, reverse=True)

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('za')

    after_filter_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    filtered_heading_text_list = [element.text for element in after_filter_list]

    assert heading_text_list != filtered_heading_text_list
    assert sorted_heading_text_list == filtered_heading_text_list


def test_filter_by_low_to_high(driver, login_by_standard_user):
    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    price_list = [element.text for element in item_list]
    convert_to_float_price_list = [float(element.replace("$", "")) for element in price_list]
    sorted_price_list = sorted(convert_to_float_price_list)

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('lohi')

    after_filter_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    filtered_price_list = [element.text for element in after_filter_list]
    convert_to_float_filtered_price_list = [float(element.replace("$", "")) for element in filtered_price_list]

    assert price_list != filtered_price_list
    assert sorted_price_list == convert_to_float_filtered_price_list


def test_filter_by_high_to_low(driver, login_by_standard_user):
    item_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    price_list = [element.text for element in item_list]
    convert_to_float_price_list = [float(element.replace("$", "")) for element in price_list]
    sorted_price_list = sorted(convert_to_float_price_list, reverse=True)

    select = Select(driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_value('hilo')

    after_filter_list = driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    filtered_price_list = [element.text for element in after_filter_list]
    convert_to_float_filtered_price_list = [float(element.replace("$", "")) for element in filtered_price_list]

    assert price_list != filtered_price_list
    assert sorted_price_list == convert_to_float_filtered_price_list