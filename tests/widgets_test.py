import time

from conftest import driver
from pages.widgets_page import AccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage, TabsPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'The title or content is incorrect in the first accordian.'
            assert second_title == 'Where does it come from?' and second_content > 0, 'The title or content is incorrect in the second accordian.'
            assert third_title == 'Why do we use it?' and third_content > 0, 'The title or content is incorrect in the third accordian.'

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

        def test_what_tab(self, driver):
            tab = TabsPage(driver, 'https://demoqa.com/tabs')
            tab.open()
            what_button, what_content = tab.check_tabs('what')
            assert what_button == 'What' and what_content != 0, 'The tab "What" was not pressed or the text is missing'

        def test_origin_tab(self, driver):
            tab = TabsPage(driver, 'https://demoqa.com/tabs')
            tab.open()
            origin_button, origin_content = tab.check_tabs('origin')
            assert origin_button == 'Origin' and origin_content != 0, 'The tab "Orgin" was not pressed or the text is missing'

        def test_use_tab(self, driver):
            tab = TabsPage(driver, 'https://demoqa.com/tabs')
            tab.open()
            use_button, use_content = tab.check_tabs('use')
            assert use_button == 'Use' and use_content != 0, 'The tab "Use" was not pressed or the text is missing'

        def test_more_tab(self, driver):
            tab = TabsPage(driver, 'https://demoqa.com/tabs')
            tab.open()
            more_button, more_content = tab.check_tabs('more')
            assert more_button == 'More' and more_content != 0, 'The tab "More" was not pressed or the text is missing'