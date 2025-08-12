import time
from selenium import webdriver

# Launch Chrome browser
driver = webdriver.Chrome()


driver.get("https://jmc.edu/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# Close the browser
driver.quit()
