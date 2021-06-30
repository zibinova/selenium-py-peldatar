from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/trickyelements.html")

driver.find_element_by_id("element1")
driver.find_element_by_id("element2")
driver.find_element_by_id("element3")
driver.find_element_by_id("element4")
driver.find_element_by_id("element5")

driver.find_element_by_tag_name('button').click()
button_label = driver.find_element_by_tag_name('button').text
print(button_label)

assert driver.find_element_by_id('result').text == (button_label + ' was clicked')

driver.close()

