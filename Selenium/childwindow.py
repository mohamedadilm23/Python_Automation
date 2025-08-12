from selenium import webdriver
from selenium.webdriver.common.by import By

# Create Firefox WebDriver
driver = webdriver.Firefox()

# Implicit wait
driver.implicitly_wait(3)

# Open the website
driver.get("https://letcode.in/test")
driver.maximize_window()

# Click on "Tabs"
driver.find_element(By.LINK_TEXT, "Tabs").click()

# Click on "home" button to open new tab
driver.find_element(By.ID, "home").click()

# Get all window handles
windows_opened = driver.window_handles

# Switch to the newly opened tab (2nd one)
driver.switch_to.window(windows_opened[0])

# Example: print the page title
print(driver.title)

# Close the new tab
driver.close()

# Switch back to original window
driver.switch_to.window(windows_opened[1])
