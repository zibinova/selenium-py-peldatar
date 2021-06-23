from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://hu.glosbe.com/pl/hu")

driver.find_element_by_id("nemletezik")

if