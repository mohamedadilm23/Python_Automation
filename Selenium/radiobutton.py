import time
from wsgiref.validate import assert_

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

buttons=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(buttons))

for radio in buttons:
   if radio.get_attribute("value")=="radio2":
    radio.click()
    assert radio.is_selected()
    break

#method 2 easy way based on index
radio1=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radio1[1].click()
assert radio1[1].is_selected()

#element dislayed example

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
#assert not means false statements allow true

# Keep browser open for 10 seconds
time.sleep(10)