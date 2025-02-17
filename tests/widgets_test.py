import time

import pytest

from conftest import driver
from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


class TestWidgets:

    class TestAccordianPage:

        @pytest.mark.parametrize('accordian_type, expected_title', [
            ('first', 'What is Lorem Ipsum?'),
            ('second', 'Where does it come from?'),
            ('third', 'Why do we use it?')
        ])
        def test_accordian(self, driver, accordian_type, expected_title):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            title, content_length = accordian_page.check_accordian(accordian_type)
            assert title == expected_title, f'Incorrect title for {accordian_type} accordian.'
            assert content_length > 0, f"Content is missing for {accordian_type} accordian."

    class TestAutoCompletePage:

        def test_fill_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, 'Added colors were missing in the input'

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'Value was not deleted'

        def test_remove_all_values_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            remove_result = auto_complete_page.remove_all_values_from_multi()
            assert remove_result == 0, 'Values were not deleted'

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, 'Added colors were missing in the input'

    class TestDataPickerPage:

        def test_change_date(self, driver):
            date_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'The date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, 'The date and time have not been changed'

    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            slider_before, slider_after = slider.change_slider_value()
            assert slider_before != slider_after, 'The slider value has not been changed'

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            progress_bar_before, progress_bar_after = progress_bar.change_progress_bar_value()
            assert progress_bar_before != progress_bar_after,  'The progress bar value has not been changed'

    class TestTabsPage:

        @pytest.mark.parametrize('tab_button, expected_title', [
            ('what', 'What'),
            ('origin', 'Origin'),
            ('use', 'Use'),
            ('more', 'More')
        ])
        def test_tabs(self, driver, tab_button, expected_title):
            tab = TabsPage(driver, 'https://demoqa.com/tabs')
            tab.open()
            tab_title, content_title = tab.check_tabs(tab_button)
            assert tab_title == expected_title, f'Incorrect title for {tab_title} tab.'
            assert content_title > 0, f'Content is missing for {tab_title} tab.'

    class TestToolTipsPage:

        @pytest.mark.parametrize('hover_elem, wait_elem, expected_text', [
            (ToolTipsPage.locators.HOVER_BUTTON, ToolTipsPage.locators.HOVER_BUTTON_TOOL_TIP, 'You hovered over the Button'),
            (ToolTipsPage.locators.HOVER_INPUT, ToolTipsPage.locators.HOVER_INPUT_TOOL_TIP, 'You hovered over the text field'),
            (ToolTipsPage.locators.LINK_CONTRARY, ToolTipsPage.locators.LINK_CONTRARY_TOOL_TIP, 'You hovered over the Contrary'),
            (ToolTipsPage.locators.LINK_FIGURES, ToolTipsPage.locators.LINK_FIGURES_TOOL_TIP, 'You hovered over the 1.10.32')
        ])
        def test_tool_tips(self, driver, hover_elem, wait_elem, expected_text):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            actual_text = tool_tips_page.check_tool_tips(hover_elem, wait_elem)
            assert actual_text == expected_text, f'Expected "{expected_text}", but got "{actual_text}"'

    class TestMenuPage:

        def test_menu_page(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            expected_result = ['Main Item 1', 'Main Item 2', 'Sub Item',
                               'Sub Item', 'SUB SUB LIST »',
                               'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']
            assert data == expected_result, 'The expected result does not match the actual result'

    class TestSelectMenuPage:

        def test_select_value(self, driver):
            select_menu = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu.open()
            selected_option = select_menu.select_value()
            selected_result = select_menu.check_select_value()
            assert selected_option == selected_result, 'Selected option does not match with selected result'

        def test_select_one(self, driver):
            select_menu = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu.open()
            selected_title = select_menu.select_one()
            selected_result = select_menu.check_select_one()
            assert selected_title == selected_result, 'Selected title does not match with selected result'

        def test_input_color(self, driver):
            select_menu = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu.open()
            input_color = select_menu.input_color()
            color_result = select_menu.check_color()
            assert input_color == color_result, 'The colors does not match'

        def test_choose_car(self, driver):
            select_menu = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu.open()
            car_input = select_menu.choose_car()
            car_result = select_menu.check_car()
            assert car_input == car_result, 'The cars does not match'