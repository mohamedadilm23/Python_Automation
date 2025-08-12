from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilis.browserutils import browserutils


class CheckoutConfirmationPage(browserutils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.terms_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase_button = (By.XPATH, "//input[@type='submit']")
        self.sucessmessage=(By.CLASS_NAME, "alert-success")

    def checkout_order(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, country_name="India"):
        # Start typing the country
        self.driver.find_element(*self.country_input).send_keys(country_name[:4])  # e.g., 'Indi'

        # Wait for the suggestion to appear
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(self.country_option))

        # Click on the country option
        self.driver.find_element(*self.country_option).click()

        # Click on the checkbox
        self.driver.find_element(*self.terms_checkbox).click()

        # Click on the purchase button
        self.driver.find_element(*self.purchase_button).click()

    def validate_order(self):
        # Add logic here, e.g., verify confirmation message
        success_message = self.driver.find_element(*self.sucessmessage).text
        return "Success" in success_message
