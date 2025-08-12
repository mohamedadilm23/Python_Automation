import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#globally timeout 5 seconds wait loading webelements

driver.implicitly_wait(2)
# Open the website
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("po")
time.sleep(2)
#implict wait list of webelements not working
veg=driver.find_elements(By.XPATH,"//div[@class='products']/div")
result=len(veg)
assert result > 0

#chaining concept parents to child easy tricks
for pack in veg:
  pack.find_element(By.XPATH,"div/button").click()

#add cart
driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
#checkoutpage
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
#total count vegtables
prices=driver.find_elements(By.XPATH,"//tr//td [5]/p")
sum=0
for rate in prices:
    #string convert int
    sum = sum + int (rate.text) #0+48 has calculate with us
    print(sum)

totalcount = int (driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalcount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#explictwait for prmocodeapplying
wait= WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

# Keep browser open for 10 seconds
time.sleep(10)

