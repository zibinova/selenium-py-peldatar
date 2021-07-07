from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    base_url = "http://localhost:9999"
    driver.get(base_url)
    links = driver.find_elements_by_xpath('//a')
    print(len(links))
    string_links = "".join([str(i) for i in links])
    print(string_links)

    for i in links:
        with open("egyfajl.txt", "w") as f:
            f.write(string_links)

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()

