import time

from selenium import webdriver



driver=webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
#scroll the footer of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#screenshot
driver.get_screenshot_as_file("letcode.png")

#ssl certificate error
#chrome_options.addarguments("__    ignore__certificate_error")
time.sleep(5)