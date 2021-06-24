from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("https://hu.glosbe.com/pl/hu")

try:
    element = driver.find_element_by_id("nemletezik")

except NoSuchElementException:

    print("Field not found")
