import random
import time

import pytest

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, \
    LinksPage, UploadAndDownloadPage, DynamicPropertiesPage
from conftest import driver


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, 'Name does not match'
            assert email == output_email, 'Email does not match'
            assert current_address == output_address, 'Current_address does not match'
            assert permanent_address == output_per_address, 'Permanent_address does not match'

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Checkboxes have not been selected - чекбоксы не были выбраны'

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

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            check_person = web_table_page.check_new_added_person()
            assert new_person in check_person, 'The added person is not in the table'

        def test_web_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'The person was not found in the table'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'Information about the person has not been changed'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            firstname = web_table_page.add_new_person()[0]
            time.sleep(1)
            web_table_page.search_person(firstname)
            web_table_page.delete_person()
            row_info = web_table_page.check_deleted()
            assert row_info == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], 'The number of rows does not match'

    class TestButtonPage:
        def test_different_click_on_the_button(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_on_the_double_button()
            right = buttons_page.click_on_the_right_button()
            me_click = buttons_page.click_on_the_me_button()
            assert double == 'You have done a double click', 'The button has not done a double click'
            assert right == 'You have done a right click', 'The button has not done a right click'
            assert me_click == 'You have done a dynamic click', 'The button has not done a dynamic click'

    class TestLinksPage:
        def test_check_simple_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.click_new_tab_simple_link()
            assert href_link == current_url, f"Expected URL: {href_link}, but got {current_url}"

        @pytest.mark.parametrize("url, expected_status", [
            ('https://demoqa.com/created', 201),
            ('https://demoqa.com/no-content', 204),
            ('https://demoqa.com/moved', 301),
            ('https://demoqa.com/bad-request', 400),
            ('https://demoqa.com/unauthorized', 401),
            ('https://demoqa.com/forbidden', 403),
            ('https://demoqa.com/invalid-url', 404),
        ])
        def test_check_links(self, driver, url, expected_status):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link(url)
            assert response_code == expected_status, f'Status code for {url} is not {expected_status}'

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, 'The file has not been uploaded'

        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, 'The file has not been downloaded'

    class TestDynamicProperties:

        def test_enable_after_5_sec_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'Button did not enable after 5 seconds'

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_before != color_after, 'Color has not been changed'

        def test_visible_after_5_sec_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_visible_after_5_sec_button()
            assert appear is True, 'Button did not appear after 5 seconds'

