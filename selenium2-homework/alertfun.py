from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time


# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/alert_playground.html")
    driver.find_element_by_name("alert").click()
    time.sleep(1)
    ref_text = "I am alert"
    alert = driver.switch_to.alert
    assert(alert.text == ref_text)
    print(alert.text)
    alert.accept()

    driver.find_element_by_name("confirmation").click()
    time.sleep(1)
    ref_text = "I am confirm"
    alert = driver.switch_to.alert
    assert (alert.text == ref_text)
    print(alert.text)
    time.sleep(2)
    alert.accept()
    time.sleep(1)

    driver.find_element_by_name("prompt").click()
    time.sleep(1)
    ref_text = "I am prompt"
    alert = driver.switch_to.alert
    assert (alert.text == ref_text)
    print(alert.text)
    time.sleep(2)
    alert.send_keys("I love this")
    alert.accept()
    time.sleep(1)
    ref_text = "You entered: I love this"
    assert (driver.find_element_by_tag_name("p").text == ref_text)

    # identifying the source element
    source = driver.find_element_by_id("double-click")
    # action chain object creation
    action = ActionChains(driver)
    # double click operation and perform
    action.double_click(source).perform()
    time.sleep(1)
    ref_text = "You double clicked me!!!, You got to be kidding me"
    alert = driver.switch_to.alert
    assert (alert.text == ref_text)
    print(alert.text)
    time.sleep(2)
    alert.accept()

finally:
    pass
    driver.close()

