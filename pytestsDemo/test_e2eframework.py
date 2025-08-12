import json
import pytest

from pageobjects.loginpage import LoginPage
from pageobjects.shoppage import ShopPage

# Load JSON test data
# "pageobjects/e2e.json" this is file name

test_datapath = "C:\\Users\\Adil\\PycharmProjects\\Python Testing\\pageobjects\\e2e.json"
with open(test_datapath) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


# ✅ FIXED: use @pytest.mark.parametrize (not @pytest.Mark.paramatrize)
@pytest.mark.parametrize("test_item", test_list)
def test_case_e2e_ecommerce(browserInstance, test_item):
    driver = browserInstance

    # Login
    login_page = LoginPage(driver)
    print(login_page.get_title())
    login_page.login(test_item['UserEmail'], test_item['UserPassword'])

    # Shop page
    shop_page = ShopPage(driver)
    shop_page.add_product_by_name(test_item['productName'])

    # Proceed to checkout
    checkout_page = shop_page.gotocart()
    print(checkout_page.get_title())

    # Confirm checkout
    checkout_page.checkout_order()
    checkout_page.enter_delivery_address("India")

    # Validate the order
    assert checkout_page.validate_order() is True

def test_dummy():
    assert 1 == 2

##pytest -m smoke // Tagging
#pytest 10 //pytest-xdist plugin you need to run in parallel