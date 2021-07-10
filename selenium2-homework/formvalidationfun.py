from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/simplevalidation.html")

    element_to_hover_over = driver.find_element_by_id("test-button")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()

    msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='test-button']"))).get_attribute("validationMessage")

    print(msg)
    assert msg is not None
    assert msg == 'Please complete all fields'


finally:
    pass


