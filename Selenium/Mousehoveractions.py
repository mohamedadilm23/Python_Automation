import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
action=ActionChains(driver)
#mousehover panathuku
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#RIGHTCLICK Mouse hover
#action.context_click(chhs.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
# Keep browser open for 10 seconds
time.sleep(10)