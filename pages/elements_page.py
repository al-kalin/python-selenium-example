from generator.generator import generated_person
from locators.elements_page_locators import (
    CheckBoxPageLocators,
    RadioButtonPageLocators,
    TextBoxPageLocators,
    WebTablePageLocators,
)
from pages.base_page import BasePage

import random


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_adress
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
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
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
