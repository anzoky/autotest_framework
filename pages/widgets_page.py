import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    @allure.step('Check accordians')
    def check_accordian(self, accordian_num):

        accordian = {'first': {'title': self.locators.SECTION_FIRST,
                               'content': self.locators.SECTION_CONTENT_FIRST},
                     'second': {'title': self.locators.SECTION_SECOND,
                                'content': self.locators.SECTION_CONTENT_SECOND},
                     'third': {'title': self.locators.SECTION_THIRD,
                               'content': self.locators.SECTION_CONTENT_THIRD}
                     }
        with allure.step('Select accordian'):
            section_title = self.element_is_visible(accordian[accordian_num]['title'])
            section_title.click()
        with allure.step('Get accordian text'):
            try:
                section_content = self.element_is_visible(accordian[accordian_num]['content']).text
            except TimeoutException:
                section_title.click()
                section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()

    @allure.step('Check multi input')
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        with allure.step('Send colors'):
            for color in colors:
                input_multi = self.element_is_visible(self.locators.MULTI_COMPLETE_INPUT)
                input_multi.send_keys(color)
                input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('Remove value from multi input')
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE)
        with allure.step('Remove value from multi input'):
            for value in remove_button_list:
                value.click()
                break
        with allure.step('Get number of values from input'):
            count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step('Remove all value from multi input')
    def remove_all_values_from_multi(self):
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE)
        with allure.step('Remove values'):
            for value in remove_button_list:
                value.click()
        with allure.step('Get number of values from input'):
            result_list = self.element_is_visible(self.locators.MULTI_COMPLETE_INPUT).get_attribute('value')
        return len(result_list)

    @allure.step('Check color in multi input')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        with allure.step('Get color names'):
            for color in color_list:
                colors.append(color.text)
        return colors

    @allure.step('Fill out single input')
    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        with allure.step('Send color to the single input'):
            input_single.send_keys(color)
            input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('Check color in single input')
    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DataPickerPage(BasePage):

    locators = DataPickerPageLocators()

    @allure.step('Select date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        with allure.step('Set date, month and year in the select date field'):
            self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
            self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
            self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('Select date and time')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.INPUT_DATE_AND_TIME)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        with allure.step('Fill out date and time in the input'):
            self.element_is_clickable(self.locators.MONTH_DATE_AND_TIME).click()
            self.set_date_item_from_list(self.locators.MONTH_DATE_AND_TIME_LIST, date.month)
            self.element_is_visible(self.locators.YEAR_DATE_AND_TIME).click()
            self.set_date_item_from_list(self.locators.YEAR_DATE_AND_TIME_LIST, '2023')
            self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
            self.set_date_item_from_list(self.locators.TIME_DATE_AND_TIME_LIST, date.time)
        input_date_after = self.element_is_visible(self.locators.INPUT_DATE_AND_TIME)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('Set date by text')
    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    @allure.step('Set date from list')
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):

    locators = SliderPageLocators()

    @allure.step('Change the value of the slider')
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.VALUE_SLIDER).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.VALUE_SLIDER).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):

    locators = ProgressBarPageLocators()

    @allure.step('Change the value of the progres bar')
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        self.go_to_element(self.element_is_present(self.locators.PROGRESS_BAR_VALUE))
        progress_bar_button = self.element_is_present(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 7))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):

    locators = TabsPageLocators()

    @allure.step('Check tabs page and get title and content')
    def check_tabs(self, tab):
        tabs = {'what': {'title': self.locators.TABS_WHAT,
                         'content': self.locators.TABS_WHAT_CONTENT},
                'origin': {'title': self.locators.TABS_ORIGIN,
                           'content': self.locators.TABS_ORIGIN_CONTENT},
                'use': {'title': self.locators.TABS_USE,
                        'content': self.locators.TABS_USE_CONTENT},
                'more': {'title': self.locators.TABS_MORE,
                         'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[tab]['title'])
        button.click()
        content = self.element_is_visible(tabs[tab]['content']).text
        return button.text, len(content)


class ToolTipsPage(BasePage):

    locators = ToolTipsPageLocators()

    @allure.step('Get text from tool tips')
    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        with allure.step('Move mouse to element'):
            self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        with allure.step('Get appear text'):
            tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
            text = tool_tip_text.text
        return text

    @allure.step('Check tool tips')
    def check_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.go_to_element(element)
        return self.get_text_from_tool_tips(hover_elem, wait_elem)


class MenuPage(BasePage):

    locators = MenuPageLocators()

    @allure.step('Check menu and get items from menu')
    def check_menu(self):
        menu_item = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):

    locators = SelectMenuPageLocators()

    @allure.step('"Select value" and get value from input')
    def select_value(self):
        select_option = self.element_is_visible(self.locators.SELECT_VALUE_INPUT)
        select_option.click()
        values = self.elements_are_visible(self.locators.SELECT_VALUE_OPTIONS)
        send_value = random.choice(values)
        text = send_value.text
        send_value.click()
        return text

    @allure.step('Get values from "select value" input')
    def check_select_value(self):
        selected_option = self.element_is_visible(self.locators.SELECT_VALUE_RESULT)
        return selected_option.text

    @allure.step('"Select one" and get one from input')
    def select_one(self):
        select_title = self.element_is_visible(self.locators.SELECT_ONE_INPUT)
        select_title.click()
        title = self.elements_are_visible(self.locators.SELECT_ONE_OPTIONS)
        send_value = random.choice(title)
        text = send_value.text
        send_value.click()
        return text

    @allure.step('Get values from "select one" input')
    def check_select_one(self):
        selected_title = self.element_is_visible(self.locators.SELECT_ONE_RESULT)
        return selected_title.text

    @allure.step('Select and input menu color')
    def input_color(self):
        color = self.element_is_visible(self.locators.SELECT_MENU_COLOR)
        color.click()
        choose_color = self.element_is_visible(self.locators.COLOR)
        choose_color.click()
        return choose_color.text

    @allure.step('Check color')
    def check_color(self):
        color = self.element_is_visible(self.locators.SELECT_MENU_COLOR)
        selected_color = Select(color)
        return selected_color.first_selected_option.text

    @allure.step('Choose a car in menu')
    def choose_car(self):
        car = self.element_is_present(self.locators.CHOOSE_CAR)
        car.click()
        return car.text

    @allure.step('Check a car')
    def check_car(self):
        car = self.element_is_visible(self.locators.STANDARD_MULTI_SELECT_FOR_CARS)
        selected_car = Select(car)
        return selected_car.first_selected_option.text