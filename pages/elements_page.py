import base64
import os
import time
import random

import allure
import requests
from selenium.common import TimeoutException

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadLocators, DynamicPropertiesLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('Fill out all fields')
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('Filling fields'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('Click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Check filled form')
    def check_filled_form(self):
        with allure.step('Get filled data'):
            full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
            email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
            current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
            permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    @allure.step('Open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random checkboxes')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 15
        with allure.step(f'Click random checkboxes {count} times'):
            while count != 0:
                item = item_list[random.randint(1, 15)]
                if count > 0:
                    self.go_to_element(item)
                    item.click()
                    count -= 1
                else:
                    break

    @allure.step('Get checked checkboxes')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        with allure.step('Get list of checked checkboxes'):
            for box in checked_list:
                title_item = box.find_element(*self.locators.TITLE_ITEM)
                data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    @allure.step('Get output result of checked checkboxes')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        with allure.step('Get result list of checked checkboxes'):
            for item in result_list:
                data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    @allure.step('Click on the radio buttons')
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                  'no': self.locators.NO_RADIOBUTTON}

        radio = self.element_is_visible(choices[choice]).click()

    @allure.step('Get output text result of radiobutton')
    def get_output_result_radiobutton(self):
        return self.element_is_present(self.locators.OUTPUT_RADIOBUTTON_RESULT).text


class WebTablePage(BasePage):

    locators = WebTablePageLocators()

    @allure.step('Add a new person to the WebTable')
    def add_new_person(self):
        count = 1
        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        with allure.step('Filling out the form to add a new person'):
            while count != 0:
                self.element_is_visible(self.locators.ADD_BUTTON).click()
                self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(firstname)
                self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
                self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
                self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
                self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
                self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
                count -= 1
        return [firstname, lastname, age, email, salary, department]

    @allure.step('Check added a new person')
    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data_person = []
        with allure.step('Get full people list from the table'):
            for item in person_list:
                data_person.append(item.text.splitlines())
        return data_person

    @allure.step('Search people in the table')
    def search_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check person in the table')
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person info in the table')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        with allure.step('Change person`s age'):
            self.element_is_visible(self.locators.UPDATE_BUTTON).click()
            self.element_is_visible(self.locators.AGE_INPUT).clear()
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        with allure.step('Click Submit button'):
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return age

    @allure.step('Delete person from the table')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Select rows in the table one by one')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            number_of_rows = self.element_is_visible(self.locators.NUMBER_OF_ROWS)
            self.go_to_element(number_of_rows)
            number_of_rows.click()
            self.element_is_visible(('css selector', f'option[value="{x}"]')).click()
            data.append(len(self.elements_are_present(self.locators.FULL_PEOPLE_LIST)))
        return data


class ButtonsPage(BasePage):

    locators = ButtonsPageLocators()

    @allure.step('Click on the double click button')
    def click_on_the_double_button(self):
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

    @allure.step('Click on the right click button')
    def click_on_the_right_button(self):
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

    @allure.step('Click on the "Me" button')
    def click_on_the_me_button(self):
        self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
        return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    @allure.step('Get text after clicking on the button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):

    locators = LinksPageLocators()

    @allure.step('Click on the simple link')
    def click_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_url = simple_link.get_attribute('href')

        response = requests.get(link_url)
        with allure.step('Move to the opened tab'):
            if response.status_code == 200:
                simple_link.click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                current_url = self.driver.current_url
                return link_url, current_url
        return link_url, response.status_code

    @allure.step('Get status code of broken link')
    def check_broken_link(self, url):
        request = requests.get(url)
        return request.status_code


class UploadAndDownloadPage(BasePage):

    locators = UploadAndDownloadLocators()

    @allure.step('Upload file')
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    @allure.step('Download file')
    def download_file(self):
        # Получаем `href` ссылку на файл
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')

        # Декодирование
        base64_data = link.split(',')[1]
        link_base = base64.b64decode(base64_data)

        # Генерация уникального имени файла
        path_name_file = rf'C:\autotest_framework\filetest_{random.randint(0, 999)}.jpeg'

        # Запись данных в файл
        with open(path_name_file, 'wb') as f:
            offset = link_base.find(b'\xff\xd8')  # Начало JPEG-файла
            f.write(link_base[offset:])

        # Проверка существования файла
        check_file = os.path.exists(path_name_file)

        # Удаление файла, если он существукт
        if check_file:
            os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesLocators()

    @allure.step('Check enable button')
    def check_enable_button(self):
        try:
            enable_button = self.element_is_clickable(self.locators.ENABLE_AFTER_5_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True

    @allure.step('Check changed color button')
    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('Check visible after 5 seconds button')
    def check_visible_after_5_sec_button(self):
        try:
            visible_after_5_sec_button = self.element_is_visible(self.locators.VISIBLE_AFTER_5_SECONDS_BUTTON)
        except TimeoutException:
            return False
        return True
