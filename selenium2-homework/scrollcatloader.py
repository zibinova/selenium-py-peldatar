from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

URL = "http://localhost:9999/scrolltoload.html"

driver.get(URL)
time.sleep(3)

for _ in range(2):
    time.sleep(3)
    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)
cats = driver.find_elements_by_tag_name("img")
print(cats)


for index, cat in enumerate(cats):
    url_str = cat.get_attribute("src")
    cat_id = cat.find_element_by_xpath("../p").text.replace("Cat id: ", "")
    cat_file_name = f"cats/{index}_{cat_id}"

    r = requests.get(url_str)
    if r.status_code == 200:
        with open(cat_file_name, 'wb') as f:
            f.write(r.content)
print()
print(len(cats))






# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
#
# # In order for ChromeDriverManager to work you must pip install it in your own environment.
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# try:
#     driver.get("http://localhost:9999/scrolltoload.html")
#     for i in range(4):
#         time.sleep(3)
#         images = driver.find_elements_by_xpath("//div[@class='image']")
#         for j in images[-5:]:
#             print(j.find_element_by_tag_name("img").get_attribute("src"))
#             print(j.find_element_by_tag_name("p").text)
#         js = "window.scrollTo(0, document.body.scrollHeight);"
#         driver.execute_script(js)
#
#
# finally:
#     pass












