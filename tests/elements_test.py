import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
from conftest import driver


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, "name does not match"
            assert email == output_email, "email does not match"
            assert current_address == output_address, "current_address does not match"
            assert permanent_address == output_per_address, "permanent_address does not match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected - чекбоксы не были выбраны'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            yes_result = radio_button_page.get_output_result_radiobutton()
            radio_button_page.click_on_the_radio_button('impressive')
            impressive_result = radio_button_page.get_output_result_radiobutton()
            radio_button_page.click_on_the_radio_button('no')
            no_result = radio_button_page.get_output_result_radiobutton()
            assert yes_result == 'Yes', '"Yes" have not been selected'
            assert impressive_result == 'Impressive', '"Impressive" have not been selected'
            assert no_result == 'No', '"No" have not been selected'

