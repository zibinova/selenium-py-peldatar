from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/editable-table.html")

add_button = driver.find_element_by_tag_name("button")
add_button.click()

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[7]/td[1]/input")))

added_row = driver.find_element_by_xpath("//table/tbody/tr[7]")

cell_name = driver.find_element_by_xpath("//table/tbody/tr[7]/td[1]/input")

cell_name.send_keys("Xiaomi")

cell_price = driver.find_element_by_xpath("//table/tbody/tr[7]/td[2]/input")

cell_price.send_keys("20.50")

cell_quantity = cell_price = driver.find_element_by_xpath("//table/tbody/tr[7]/td[3]/input")

cell_quantity.send_keys("20")

cell_category = driver.find_element_by_xpath("//table/tbody/tr[7]/td[4]/input")

cell_category.send_keys("Electronics")



