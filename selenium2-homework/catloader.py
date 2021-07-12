from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#from PIL import Image
#import PIL

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/loadmore.html")
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    for i in range(4):
        time.sleep(3)
        images = driver.find_elements_by_xpath("//div[@class='image']")
        for j in images[-5:]:
            print(j.find_element_by_tag_name("img").get_attribute("src"))
            print(j.find_element_by_tag_name("p").text)
        load_more.click()

        #picture = Image.open(r'Downloads\3.jpg')
        #picture = picture.save("dolls.jpg")

finally:
    pass
