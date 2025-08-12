import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Open the website
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Maximize the browser window
driver.maximize_window()
driver.implicitly_wait(7)

# Click on the 'Shop' link
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# Get all product cards
products = driver.find_elements(By.CSS_SELECTOR, "div.card.h-100")

for product in products:
    # Get the product title (inside h4 tag with class 'card-title')
    product_name = product.find_element(By.CSS_SELECTOR, "h4.card-title").text

    if product_name == "Blackberry":
        # Click the 'Add' button inside this product card
        product.find_element(By.XPATH, ".//button").click()  # Relative XPath

#checkoutprodcut
driver.find_element(By.XPATH,"//a[contains(@class,'nav-link btn')]").click()
#checkout process the page
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("Indi")

#search india via dropdown
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

#click on checkbox
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
#Click on purchase
driver.find_element(By.XPATH,"//input[@type='submit']").click()

alert=driver.find_element(By.XPATH,"//div[contains(@class,'alert alert-success')]").text
print(alert)
assert ("Success! Thank you!") in alert
time.sleep(5)