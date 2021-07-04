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

# extra próbálkozás függvénnyel
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# driver = webdriver.Chrome()
# driver.get("https://hu.glosbe.com/pl/hu")
#
# def find(elem):
#
#      try:
#      except NoSuchElementException:
#      print("Ilyen mező nem létezik")
#
# finally:
#         pass
#
#
# find(nincs)
# find("ájdi")


# tanár:
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException
#
# # In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# try:
#     driver.get("https://google.com")
#     links = driver.find_elements_by_id("no_such_element")
# except NoSuchElementException as e:
#     print('Element not found: ', e)
# finally:
#     driver.close()
