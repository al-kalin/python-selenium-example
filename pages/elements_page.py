"""
Module containing Page Object classes for the Elements section
of the DemoQA application.

Provides methods for interacting with page elements, filling out forms,
selecting options, managing table records, and validating page content.
"""

import random

import requests

from generator.generator import generated_person
from locators.elements_page_locators import (
    ButtonsPageLocators,
    CheckBoxPageLocators,
    LinksPageLocators,
    RadioButtonPageLocators,
    TextBoxPageLocators,
    WebTablePageLocators,
)
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """
    Page Object class for the Text Box page.

    Provides methods for interacting with the text boxes.
    """

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """
        Fill in all fields of the Text Box form using randomly generated data.

        Steps:
            1. Generate a person with randomly generated data.
            2. Retrieve the person's full name, email, current address,
            and permanent address.
            3. Fill in all form fields with the generated data.
            4. Submit the form.
            5. Return the submitted data, replacing newline characters
            in the addresses with spaces.

        Returns:
            tuple: A tuple containing the full name, email, current address,
            and permanent address.
        """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visiblle(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visiblle(self.locators.EMAIL).send_keys(email)
        self.element_is_visiblle(self.locators.CURRENT_ADDRESS).send_keys(
            current_address
        )
        self.element_is_visiblle(self.locators.PERMANENT_ADDRESS).send_keys(
            permanent_address
        )
        self.element_is_visiblle(self.locators.SUBMIT).click()
        return (
            full_name,
            email,
            current_address.replace("\n", " "),
            permanent_address.replace("\n", " "),
        )

    def check_filled_form(self):
        """
        Retrieve the submitted data displayed after filling out the Text Box form.

        Steps:
            1. Locate the displayed full name and extract its value.
            2. Locate the displayed email and extract its value.
            3. Locate the displayed current address and extract its value.
            4. Locate the displayed permanent address and extract its value.
            5. Return all extracted values as a tuple.

        Returns:
            tuple: A tuple containing the full name, email, current address,
            and permanent address displayed on the page.
        """
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(
            ":"
        )[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS
        ).text.split(":")[1]
        permanent_address = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS
        ).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """
    Page Object class for the Check Box page.

    Provides methods for interacting with the check boxes.
    """

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        """
        Expand all checkbox tree elements.
        """

        while True:
            tree_switcher = self.driver.find_elements(*self.locators.TREE_SWITCHER_LIST)

            if not tree_switcher:
                break

            tree_switcher[0].click()

    def clicl_random_checkbox(self):
        """
        Click random checkboxes.
        """

        checkbox_item_list = self.element_are_visiblle(self.locators.CHECK_BOX_LIST)
        count = 21
        while count != 0:
            item = checkbox_item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        """
        Get title from checked checkboxes.
        """

        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return (
            str(sorted(data))
            .replace(" ", "")
            .replace("doc", "")
            .replace(".", "")
            .lower()
        )

    def get_output_result(self):
        """
        Get the output result after checking the checkboxes.
        """

        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(sorted(data)).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    """
    Page Object class for the Radio Button page.

    Provides methods for interacting with the radio buttons.
    """

    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        """
        Click on the radio button.
        """

        choices = {
            "yes": self.locators.YES_RADIOBUTTON,
            "no": self.locators.NO_RADIOBUTTON,
            "impressive": self.locators.IMPRESSIVE_RADIOBUTTON,
        }
        self.element_is_visiblle(choices[choice]).click()

    def get_output_result(self):
        """
        Get the output result after selecting the radio button.
        """

        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    """
    Page Object class for the Web Tables page.

    Provides methods for interacting with the web table.
    """

    locators = WebTablePageLocators()

    def add_new_person(self):
        """
        Add a new person to the web table using randomly generated data.

        Steps:
            1. Generate random personal and employment information.
            2. Extract the person's first name, last name, email, age,
            salary, and department.
            3. Click the Add button to open the registration form.
            4. Fill in all form fields with the generated data.
            5. Submit the form.
            6. Return the data of the newly added person.

        Returns:
            list: A list containing the person's first name, last name,
            age, email, salary, and department.
        """
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visiblle(self.locators.ADD_BUTTON).click()
            self.element_is_visiblle(self.locators.FIRST_NAME_INPUT).send_keys(
                firstname
            )
            self.element_is_visiblle(self.locators.LAST_NAME_INPUT).send_keys(lastname)
            self.element_is_visiblle(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visiblle(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visiblle(self.locators.SALARY_INPYT).send_keys(salary)
            self.element_is_visiblle(self.locators.DEPARTMENT_INPUT).send_keys(
                department
            )
            self.element_is_visiblle(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def get_people_list(self):
        """
        Retrieve and organize all displayed records from the web table.

        Steps:
            1. Find all elements containing the table records.
            2. Extract the text content from each element.
            3. Group the extracted data into lists of six values per person,
            excluding the seventh element (action buttons).
            4. Return the list of people with their corresponding data.

        Returns:
            list: A list of people, where each person is represented by
            a list containing first name, last name, age, email, salary,
            and department.
        """
        people_list = self.elements_are_present_or_empty(self.locators.FULL_PEOPLE_LIST)
        if not people_list:
            return None
        data = []
        for item in people_list:
            person_data = item.text
            data.append(person_data)
        data = [data[i : i + 6] for i in range(0, len(data), 7)]
        return data

    def search_some_person(self, key_word):
        """
        Search for a person in the web table using a specified keyword.

        Steps:
            1. Locate the search input field.
            2. Enter the specified keyword into the search field.

        Args:
            key_word (str): The keyword used to search for a person
            in the web table.
        """
        self.element_is_visiblle(self.locators.SEARCH_INPUT).send_keys(key_word)

    def update_person_info(self):
        """
        Update a person's age in the web table using randomly generated data.

        Steps:
            1. Generate a person with randomly generated data.
            2. Retrieve the generated person's age.
            3. Click the Edit button for the person's record.
            4. Clear the existing age value.
            5. Enter the newly generated age.
            6. Submit the updated information.
            7. Return the updated age.

        Expected result:
            The person's age is successfully updated,
            and the new age is returned as a string.
        """

        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visiblle(self.locators.EDIT_BUTTON).click()
        age_input = self.element_is_visiblle(self.locators.AGE_INPUT)
        age_input.clear()
        age_input.send_keys(age)
        self.element_is_visiblle(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        """
        Delete a person's record from the web table.

        Steps:
            1. Locate the Delete button for the person's record.
            2. Click the Delete button.

        Expected result:
            The person's record is successfully deleted from the web table.
        """
        self.element_is_visiblle(self.locators.DELETE_BUTTON).click()


class ButtonsPage(BasePage):
    """
    Page Object class for the Buttons page.

    Provides methods for interacting with the buttons.
    """

    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        """
        Perform the specified click action on a button and verify the result.

        Steps:
            1. Check the specified click type.
            2. Perform a double-click, right-click, or regular click
            on the corresponding button.
            3. Retrieve the success message displayed after the interaction.
            4. Return the success message.

        Args:
            type_click (str): The type of click action to perform.
                Accepted values are "double", "right", and "click".

        Returns:
            str: The success message displayed after the button interaction.
        """
        if type_click == "double":
            self.action_double_click(
                self.element_is_visiblle(self.locators.DOUBLE_CLICK_BUTTON)
            )
            return self.check_clicked_on_the_button(self.locators.SUCCCESS_DOUBLE)

        if type_click == "right":
            self.action_right_click(
                self.element_is_visiblle(self.locators.RIGHT_CLICK_BUTTON)
            )
            return self.check_clicked_on_the_button(self.locators.SUCCCESS_RIGHT)

        if type_click == "click":
            self.element_is_visiblle(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        """
        Retrieve the success message displayed after a button interaction.

        Steps:
            1. Locate the success message element.
            2. Extract and return its text content.

        Args:
            element (tuple): Locator used to find the success message element.

        Returns:
            str: The text of the success message.
        """
        return self.element_is_present(element).text


class LinksPage(BasePage):
    """
    Page Object class for the Links page.

    Provides methods for interacting with the links.
    """

    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        """Verify that the Simple Link opens successfully in a new tab.

        Checks the link's HTTP response status, clicks the link if the
        response is successful, switches to the newly opened tab, and
        returns the expected and actual URLs.

        Returns:
            tuple: The link URL and either the opened tab URL or
            the HTTP response status code.
        """
        simple_link = self.element_is_visiblle(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute("href")
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_new_tab(1)
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url, locator_link):
        """Check the HTTP response status of a link and click it if accessible.

        Sends a GET request to the provided URL. If the response status
        code is 200, retrieves the specified locator and clicks the element.
        Otherwise, returns the HTTP response status code.

        Args:
            url (str): The URL to check.
            locator_link (str): The name of the locator attribute.

        Returns:
            int or None: The HTTP response status code if the link is
            inaccessible; otherwise, None.
        """
        request = requests.get(url)
        if request.status_code == 200:
            locator = getattr(self.locators, locator_link)
            self.element_is_present(locator).click()
        else:
            return request.status_code
