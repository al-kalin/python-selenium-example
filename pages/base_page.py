"""
Module providing the BasePage class for Selenium WebDriver automation.

Contains reusable methods for browser navigation, locating web elements,
handling explicit waits, scrolling, and performing mouse actions.

Serves as a base class for Page Object classes across the application.
"""

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base class providing common functionality for Page Object classes.

    Stores the Selenium WebDriver instance and page URL,
    and provides reusable methods for interacting with web pages.
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visiblle(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def element_are_visiblle(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def elements_are_present_or_empty(self, locator, timeout=5):
        """
        Find all elements matching the specified locator.

        Args:
            locator (tuple): Locator used to find elements on the page.
            timeout (int): Maximum time to wait for elements to appear.

        Returns:
            list: A list of matching WebElements or an empty list
            if no elements are found within the specified timeout.
        """
        try:
            return wait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            return []

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Scroll the page until the specified web element comes into view.

        Steps:
            1. Execute a JavaScript command using WebDriver.
            2. Scroll the page to bring the specified element into view.

        Args:
            element (WebElement): The web element to scroll into view.

        Expected result:
            The specified web element is brought into the visible area of the page.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        """
        Perform a double-click action on the specified web element.

        Steps:
            1. Initialize an ActionChains instance.
            2. Move the mouse pointer to the specified element.
            3. Perform a double-click on the element.

        Expected result:
            The specified web element is successfully double-clicked.

        Args:
            element (WebElement): The web element to double-click.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.double_click(element)
        actions.perform()

    def action_right_click(self, element):
        """
        Perform a right-click action on the specified web element.

        Steps:
            1. Initialize an ActionChains instance.
            2. Move the mouse pointer to the specified element.
            3. Perform a right-click on the element.

        Expected result:
            The context menu is triggered by right-clicking the specified element.

        Args:
            element (WebElement): The web element to right-click.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.context_click(element)
        actions.perform()

    def switch_to_new_tab(self, index):
        """
        Switch to a browser tab or window by its index.

        Steps:
            1. Retrieve the list of currently open browser windows.
            2. Switch WebDriver focus to the window at the specified index.

        Args:
            index (int): The index of the browser window to switch to.

        Expected result:
            WebDriver successfully switches focus to the specified browser window.
        """
        self.driver.switch_to.window(self.driver.window_handles[index])
