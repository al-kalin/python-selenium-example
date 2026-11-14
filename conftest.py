import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Fixture for initializing and managing the Chrome WebDriver.

    Steps:
        1. Install and configure ChromeDriver using ChromeDriverManager.
        2. Initialize the Chrome WebDriver.
        3. Maximize the browser window.
        4. Yield the WebDriver instance for test execution.
        5. Close the browser after the test is completed.

    Expected result:
        A maximized Chrome browser is available during test execution
        and is automatically closed after the test finishes.
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
