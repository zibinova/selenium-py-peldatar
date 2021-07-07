from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import csv

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/another_form.html")


def find_and_clear_by_id(ids):
    element = driver.find_element_by_id(ids)
    element.clear()
    return element


submit_button = driver.find_element_by_id("submit")

with open("table_in.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
        find_and_clear_by_id("fullname").send_keys(row[0])
        find_and_clear_by_id("email").send_keys(row[1])
        find_and_clear_by_id("dob").send_keys(row[2])
        find_and_clear_by_id("phone").send_keys(row[3])
        submit_button.click()


