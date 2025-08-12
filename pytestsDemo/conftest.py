# conftest.py
import os
import sys
from datetime import datetime
import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None  # Global for screenshot use


# --------- Pytest Options ---------
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser: chrome/firefox/edge/incognito"
    )


# --------- Browser Fixture ---------
@pytest.fixture(scope="function")
def browserInstance(request):
    """Launch browser before each test."""
    global driver
    browser_name = request.config.getoption("--browser_name").lower().strip()
    service_obj = Service()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
    elif browser_name in ["incognito", "incognito tab"]:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(service=service_obj, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    print(f"Launched browser: {driver.capabilities['browserName']}")
    yield driver
    driver.quit()


# --------- Screenshot on Failure ---------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure and embed in HTML report."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("browserInstance")
        if driver_instance and _is_driver_alive(driver_instance):

            screenshot_dir = os.path.join("pytestsDemo", "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"FAILED_{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver_instance.save_screenshot(file_path)

            # Log to console (emoji locally, plain text in Jenkins)
            if sys.stdout.encoding and sys.stdout.encoding.lower().startswith("utf"):
                print(f"\n📸 Screenshot saved to: {file_path}")
            else:
                print(f"\nScreenshot saved to: {file_path}")

            # Relative path for HTML report so Jenkins can show it
            html_report_path = getattr(item.config.option, "htmlpath", None)
            if html_report_path:
                rel_path = os.path.relpath(file_path, os.path.dirname(html_report_path))
            else:
                rel_path = file_path

            extra = getattr(report, 'extra', [])
            extra.append(extras.image(rel_path))
            report.extra = extra


def _is_driver_alive(driver_instance):
    """Check if Selenium session is still active."""
    try:
        _ = driver_instance.title
        return True
    except:
        return False
