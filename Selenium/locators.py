from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Correct import for Chrome
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Provide the correct path to chromedriver
service_obj = Service("C:\\Users\\Adil\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")

# Initialize Chrome with service
driver = webdriver.Chrome(service=service_obj)

# Open the website
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

print(driver.find_element(By.NAME,"name").send_keys("mohamed adil"))
print(driver.find_element(By.NAME,"email").send_keys("adil.m@vdartin.com"))
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.find_element(By.XPATH,"//label[@for='inlineRadio2']").click()

#static dropdown
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)

message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

#assert validation
assert "success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Adil")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


#Select the agree
driver.find_element(By.CSS_SELECTOR,".chkAgree").is_selected()

# Keep browser open for 10 seconds
time.sleep(20)

#xpath= //tagname[@attribute='value']
#css= tagname[attribute='value'],#id,.classname


