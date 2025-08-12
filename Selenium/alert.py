import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Mohamedadil"
driver = webdriver.Chrome()

# Open the website
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Enter name and click the alert button
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# Switch to alert and grab text
alert = driver.switch_to.alert  # ✅ correct method
copyalert = alert.text
print(copyalert)

# Accept the alert (click OK)
alert.accept()

# Assert that the name is in the alert text
assert name in copyalert, "Alert text does not contain the name!"

# Optional: handle confirm alert as well
# chhs.find_element(By.ID, "confirmbtn").click()
# confirm_alert = chhs.switch_to.alert
# print(confirm_alert.text)
# confirm_alert.accept()  # or .dismiss()

# Keep browser open for 10 seconds
time.sleep(10)

# Optional: close the browser
driver.quit()
