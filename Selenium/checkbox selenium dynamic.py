import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkbox))

for checkcount in checkbox:
    #if get attribute not showing like id ,xpath,css
    if checkcount.get_attribute("value")=="option3":
        checkcount.click()
        assert checkcount.is_selected()
        break

# Keep browser open for 10 seconds
time.sleep(20)