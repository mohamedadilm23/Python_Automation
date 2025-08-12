import time


from selenium.webdriver.common.by import By


def test_sorting(browserInstance):
    driver = browserInstance

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")


# empty list la data store agum
    listdata = []
# before
# original value[ wheat,tomato,strawberry,rice,potato]

# after
# 1.click on veg fruit sort icon
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# 2.collect all vegiee names->browsersortedlist(Almond,Apple,Banana,Beans,Brinjal)

    vegtableelements = driver.find_elements(By.XPATH, "//tr//td[1]")

# using for loop for itration
    for fruits in vegtableelements:
     listdata.append(fruits.text)

    originaldata = listdata.copy()

# Almond,Apple,Banana,Beans,Brinjal(list data stored in a variable original data)


# 3 sort the list=>new sortedlist
    listdata.sort()
# Almond,Apple,Banana,Beans,Brinjal(listdata)

    assert listdata == originaldata

time.sleep(10)
