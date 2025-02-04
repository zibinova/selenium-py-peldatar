from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import csv
from datetime import datetime, timezone

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/forms.html")

nowutc = datetime.now(timezone.utc)

print(nowutc)

# dob = row[2]
# print(dob)
# dobnew = datetime.strptime(dob, "%Y-%m-%d").strftime("%m/%d/%Y")


driver.find_element_by_id("example-input-date").send_keys("6/5/2021")

driver.find_element_by_id("example-input-date-time").send_keys("2012.05.05 05:05:05:555")


frmt = "%m/%d/%Y %H:%M %p"
date_string = "05/12/2000 12:01 PM"
date = datetime.strptime("05/12/2000 12:01 PM", frmt).strftime("%m/%d/%Y %H:%M %p")

driver.find_element_by_id("example-input-date-time-local").send_keys(date)

driver.find_element_by_id("example-input-month").send_keys("December 1995")

driver.find_element_by_id("example-input-week").send_keys("52",  "2015")

driver.find_element_by_id("example-input-time").send_keys("12:25, AM")
