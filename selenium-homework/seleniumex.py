from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("https://hu.glosbe.com/pl/hu")

try:
    driver.find_element_by_id("nemletezik")

except NoSuchElementException:

    print("Ilyen mező nem létezik")

finally:
    pass
driver.close()


# extra:


#def this_sucks():
