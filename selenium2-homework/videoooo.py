from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/videos.html")
    html5video_builtin = driver.find_element_by_id("html5video")
    html5video_builtin.click()

    video1 = driver.find_element_by_xpath("/html/body/div/button[1]")
    video1.click()

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()


finally:
    pass
