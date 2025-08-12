from selenium.webdriver.common.by import By
from pageobjects.shoppage import ShopPage
from utilis.browserutils import browserutils


class LoginPage(browserutils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")

    def login(self, email, password):
        self.driver.find_element(*self.username).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin_button).click()

        # After login, return the shop page object
        return ShopPage(self.driver)


#| Line                       | Meaning                                                                 |
#| -------------------------- | ----------------------------------------------------------------------- |
#| `super()`                  | Parent class-ah refer pannudhu                                          |
#| `super().__init__(driver)` | Parent class-oda constructor-ah koopudhu and driver value pass panradhu |
#| Purpose                    | Inheritance use panni, duplicate code avoid panradhu                    |
