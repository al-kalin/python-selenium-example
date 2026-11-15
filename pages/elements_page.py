from generator.generator import generated_person
from locators.elements_page_locators import (
    CheckBoxPageLocators,
    RadioButtonPageLocators,
    TextBoxPageLocators,
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
