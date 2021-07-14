from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:

    driver.get("http://localhost:9999/windowgame.html")
    time.sleep(3)

    main_window = driver.window_handles[0]
    buttons = driver.find_elements_by_tag_name("button")
    random.shuffle(buttons)

    for button in buttons:
        ref_text = driver.find_element_by_id("target_color").text
        button.click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        color = driver.find_element_by_tag_name("h1").text
        if color == ref_text:
            driver.close()
            driver.switch_to.window(main_window)
            strikes = driver.find_element_by_id("numberOfGuesses").text
            print(f"Eltaláltad a színt, találatok száma: " + strikes)
            break
        else:
            driver.close()
            driver.switch_to.window(main_window)

finally:
    driver.close()
