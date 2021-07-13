from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from os import getcwd

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("http://localhost:9999/dragndrop2.html")

time.sleep(2)

cwd = getcwd()
JS_DRAG_DROP = open(cwd + '\\dnd.js', 'r').read()
print(JS_DRAG_DROP)
# drag and drop an element on another one

sources = driver.find_elements_by_xpath("//ul[@id='Todo']/li")
target = driver.find_element_by_id("Done")


for source in sources:
    driver.execute_script(JS_DRAG_DROP, source, target)


driver.implicitly_wait(5)



