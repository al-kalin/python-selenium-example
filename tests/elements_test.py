from pages.elements_page import CheckBoxPage, RadioButtonPage, TextBoxPage


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
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"
