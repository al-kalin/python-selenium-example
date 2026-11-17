import time

from pages.elements_page import CheckBoxPage, RadioButtonPage, TextBoxPage, WebTablePage

import random


class TestElements:
    """
    Test suite for the Elements module.

    Contains test cases for UI elements functionality.
    """

    class TestTextBox:
        """
        Test suite for the Text Box functionality.

        Covers form submission and validation of displayed data.
        """

        def test_text_box(self, driver):
            """
            Verify that the Text Box form accepts valid data
            and displays the submitted information correctly.

            Steps:
                1. Open the Text Box page.
                2. Fill in all form fields.
                3. Submit the form.
                4. Verify that the displayed data matches the input data.

            Expected result:
                All submitted values match the original input data.
            """
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = (
                text_box_page.fill_all_fields()
            )
            output_name, output_email, output_cur_addr, output_perm_addr = (
                text_box_page.check_filled_form()
            )
            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert (
                current_address == output_cur_addr
            ), "the current address does not match"
            assert (
                permanent_address == output_perm_addr
            ), "the permanent address does not match"

    class TestCheckBox:
        """
        Test suite for the Check Box functionality.

        Covers checkbox selection and validation of selected items.
        """

        def test_check_box(self, driver):
            """
            Verify that randomly selected checkboxes are correctly displayed
            in the output result.

            Steps:
                1. Open the Check Box page.
                2. Expand the entire checkbox tree.
                3. Select random checkboxes.
                4. Retrieve the names of the selected checkboxes.
                5. Retrieve the checkbox names displayed in the output result.
                6. Verify that the selected checkboxes match the output result.

            Expected result:
                All selected checkboxes are correctly displayed in the output result.
            """
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.clicl_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "checkboxes have not been selected"

    class TestRadioButton:
        """
        Test suite for the Radio Button functionality.

        Covers radio button selection and validation of selected options.
        """

        def test_radio_button(self, driver):
            """
            Verify that radio buttons can be selected and the correct
            selection results are displayed.

            Steps:
                1. Open the Radio Button page.
                2. Select the 'Yes' radio button and retrieve the output result.
                3. Select the 'Impressive' radio button and retrieve the output result.
                4. Select the 'No' radio button and retrieve the output result.
                5. Verify that each selection matches the expected output.

            Expected result:
                The selected radio button is correctly reflected in the output result:
                - 'Yes' displays 'Yes'.
                - 'Impressive' displays 'Impressive'.
                - 'No' displays 'No'.
            """
            radio_button_page = RadioButtonPage(
                driver, "https://demoqa.com/radio-button"
            )
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("no")
            output_no = radio_button_page.get_output_result()
            assert output_yes == "Yes", "'Yes' have not been selected"
            assert (
                output_impressive == "Impressive"
            ), "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"

    class TestWebTable:
        """
        Test suite for the Web Tables functionality.

        Covers adding new records, searching for existing records,
        and validating displayed table data.
        """

        def test_web_table_add_person(self, driver):
            """
            Verify that a new person can be successfully added to the web table.

            Steps:
                1. Open the Web Tables page.
                2. Add a new person with randomly generated data.
                3. Retrieve the list of people displayed in the table.
                4. Verify that the newly added person is present in the table.

            Expected result:
                The newly added person is correctly displayed in the web table.
            """
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.get_people_list()
            assert new_person in table_result, "The person was not added to the table."

        def test_web_table_search_person(self, driver):
            """
            Verify that the search functionality correctly filters table records.

            Steps:
                1. Open the Web Tables page.
                2. Add a new person with randomly generated data.
                3. Retrieve the list of people displayed in the table.
                4. Select a random keyword from the newly added person's data.
                5. Search for the selected keyword.
                6. Retrieve the filtered list of people.
                7. Verify that the number of displayed records has decreased.
                8. Verify that every displayed record contains the search keyword.

            Expected result:
                The table displays only records containing the search keyword,
                and the number of displayed records is smaller than before the search.
            """
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            people_list = web_table_page.get_people_list()
            time.sleep(3)
            key_word = new_person[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            search_people_list = web_table_page.get_people_list()
            assert len(people_list) > len(
                search_people_list
            ), "The number of displayed records did not decrease"
            for person in search_people_list:
                assert (
                    key_word in person
                ), f"Search word '{key_word}' not found in: {person.text}"
