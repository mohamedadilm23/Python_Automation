from selenium.webdriver.common.by import By

from pageobjects.checkout_confirmationpage import CheckoutConfirmationPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shoplink = (By.CSS_SELECTOR, "a[href*='shop']")
        self.productcards = (By.CSS_SELECTOR, "div.card.h-100")
        self.checkoutbutton = (By.XPATH, "//a[contains(@class,'nav-link btn')]")

    def add_product_by_name(self, product_name):
        # Click on the 'Shop' link
        self.driver.find_element(*self.shoplink).click()

        # Get all product cards
        products = self.driver.find_elements(*self.productcards)

        for product in products:
            # Get the product title
            product_title = product.find_element(By.CSS_SELECTOR, "h4.card-title").text

            if product_title == product_name:
                # Click the 'Add' button inside this product card
                product.find_element(By.XPATH, ".//button").click()

    def gotocart(self):
        # checkoutprodcut

        self.driver.find_element(*self.checkoutbutton).click()
        checkout_page = CheckoutConfirmationPage(self.driver)
        return checkout_page
