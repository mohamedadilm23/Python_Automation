import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()
driver.get("https://letcode.in/frame")
driver.maximize_window()

# Step 1: Switch to the first frame
driver.switch_to.frame("firstFr")

# Step 2: Enter name and email in the first frame
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter name']").send_keys("Mohamed")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']").send_keys("Adil")

# Step 3: Switch to the nested iframe inside firstFr
nested_frame = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(nested_frame)

# Step 4: Enter nested email
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("adilfc007@gmail.com")

# Step 5: Switch back to the main page content
driver.switch_to.default_content()

# Step 6: Grab and print heading text from the main page
heading = driver.find_element(By.TAG_NAME, "h1").text
print("Page Heading:", heading)

# Step 7: Wait to see results before closing
time.sleep(10)
driver.quit()
