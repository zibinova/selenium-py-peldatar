from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/editable-table.html")

add_button = driver.find_element_by_tag_name("button")
rows = driver.find_elements_by_xpath("//table/tbody/tr")

#new_row = driver.find_element_by_xpath("//table/tbody/tr[7]")


def add_and_fill_row(n, p, q, c):
    add_button.click()

    WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[last()]/td[1]/input")))

    cell_name = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[1]/input")

    cell_price = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[2]/input")

    cell_quantity = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[3]/input")
    cell_category = driver.find_element_by_xpath("//table/tbody/tr[last()]/td[4]/input")

    cell_name.send_keys(n)
    cell_price.send_keys(p)
    cell_quantity.clear()
    cell_quantity.send_keys(q)
    cell_category.send_keys(c)


add_and_fill_row("Xiaomi", "20.50", "20", "Electronics")
add_and_fill_row("Tesla", "30.50", "40", "Electronics")

