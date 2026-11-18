from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
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
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
