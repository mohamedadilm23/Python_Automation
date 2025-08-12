import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the website
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
#auto suggest dropdown
driver.find_element(By.ID,"autosuggest").send_keys("south")
time.sleep(3)
dynamiclist=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(dynamiclist))

for droplist in dynamiclist:
    #text is matching chhs.find_element(By.ID,"autosuggest").send_keys("south")
    if droplist.text=="South Africa":
      droplist.click()
      break

assert print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))=="South"



# Keep browser open for 10 seconds
time.sleep(20)