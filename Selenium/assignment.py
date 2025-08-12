import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#globally timeout 5 seconds wait loading webelements

#list of the values
Expectedlist=['Potato - 1 Kg','Pomegranate - 1 Kg']
actuallist=[]

driver.implicitly_wait(2)

# Open the website
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

#search the elements
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("po")
time.sleep(2)
#implict wait list of webelements not working

#list of vegtables count
veg=driver.find_elements(By.XPATH,"//div[@class='products']/div")
result=len(veg)
assert result > 0

#chaining concept parents to child easy tricks
for pack in veg:
  actuallist.append(pack.find_element(By.XPATH,"h4").text)
  pack.find_element(By.XPATH,"div/button").click()

assert Expectedlist==actuallist
print(actuallist)
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

totalamount = int (driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalamount #117


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#explictwait for prmocodeapplying
wait= WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

totaldiscounted= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert  totalamount > totaldiscounted


#placeorder
driver.find_element(By.XPATH,"(//div[@class='products']//button)[2]").click()

#dropdown
#static dropdown
dropdown= Select(driver.find_element(By.TAG_NAME,"Select"))
dropdown.select_by_visible_text("Albania")
dropdown.select_by_index(1)



#Select the agree
driver.find_element(By.CSS_SELECTOR,".chkAgree").click()

#Select proceed
driver.find_element(By.XPATH,"//button[normalize-space(text())='Proceed']").click()
# Keep browser open for 10 seconds
time.sleep(10)

