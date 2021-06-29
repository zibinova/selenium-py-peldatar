from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/kitchensink.html")

# elem ID alapján:/BMW radio button:

radiobutton = driver.find_element_by_id("bmwradio")
print(radiobutton.text)
#ennek van text vagy barmilyen attributum erteke?
# #úgy tűnik számomra, hogy van name, value, type attributuma mégse bírom kiiratni,

select_class = driver.find_element_by_id("carselect")
print(select_class.text)

multiple_select = driver.find_element_by_name("multiple-select-example")
print(multiple_select.text)

checkbox_example = driver.find_element_by_xpath('//*[@id="checkbox-example"]/fieldset/legend')
print(checkbox_example.text)
driver.close()

