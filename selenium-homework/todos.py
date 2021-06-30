from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/todo.html")

todos = driver.find_elements_by_class_name("done-false")
for todo in todos:
    print(todo.text)
