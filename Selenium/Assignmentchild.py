from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Create Firefox WebDriver
driver = webdriver.Chrome()

# Implicit wait
driver.implicitly_wait(3)

# Open the website
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
#click blink url
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
#handling parents and childwindows
windows_opened=driver.window_handles

#childwindows
driver.switch_to.window(windows_opened[1])
#Please email us at mentor@rahulshettyacademy.com
# with below template to receive response (grab the text)
message=driver.find_element(By.CSS_SELECTOR,".red").text
#spilt the text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
#goes to parent window
#opening parent windows
driver.switch_to.window(windows_opened[0])
driver.find_element(By.ID,"username").send_keys(var)
driver.find_element(By.ID,"password").send_keys(var)
driver.find_element(By.ID,"signInBtn").click()
wait=WebDriverWait(driver,10)
#signbutton loading use implicat wait
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

