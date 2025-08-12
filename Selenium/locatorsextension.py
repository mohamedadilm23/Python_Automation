import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the website
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
#linktext
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#xpath parent to child
driver.find_element(By.XPATH,"//form//div[1]//input").send_keys("demo@gmail.com")
#css parent to child
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("123456")

#css parent to child
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("123456")

#text based xpath
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
# Keep browser open for 10 seconds
time.sleep(20)