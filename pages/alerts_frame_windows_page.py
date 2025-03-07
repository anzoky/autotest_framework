import time

import allure

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import BrowserWindowPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):

    locators = BrowserWindowPageLocators()

    @allure.step('Check opened new tab and switch to it')
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        with allure.step('Switch to the open tab'):
            self.driver.switch_to.window(self.driver.window_handles[1])
        with allure.step('Get text from the open tab'):
            text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return text_title

    @allure.step('Check opened new window and switch to it')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        with allure.step('Switch to the open window'):
            self.driver.switch_to.window(self.driver.window_handles[1])
        with allure.step('Get text from the open window'):
            text_title = self.element_is_present(self.locators.TITLE_NEW_WINDOW).text
        return text_title


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    @allure.step('Check "see alert"')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        with allure.step('Switch to the alert'):
            alert_window = self.switch_to_alert()
        with allure.step('Get alert text'):
            alert_text = alert_window.text
        with allure.step('Accept alert'):
            alert_window.accept()
        return alert_text

    @allure.step('Check "alert will appear after 5 seconds"')
    def check_alert_appear_after_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        with allure.step('Switch to the alert'):
            alert_window = self.switch_to_alert()
        with allure.step('Get alert text'):
            alert_text = alert_window.text
        with allure.step('Accept alert'):
            alert_window.accept()
        return alert_text

    @allure.step('Check "confirm alert" and accept it')
    def check_confirm_alert_accept(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        with allure.step('Switch to the alert'):
            alert_window = self.switch_to_alert()
        with allure.step('Accept alert'):
            alert_window.accept()
        with allure.step('Get confirm result text'):
            text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('Check "confirm alert" and dismiss it')
    def check_confirm_alert_dismiss(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        with allure.step('Switch to the alert'):
            alert_window = self.switch_to_alert()
        with allure.step('Dismiss alert'):
            alert_window.dismiss()
        with allure.step('Get confirm result text'):
            text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('Check "prompt alert"')
    def check_prompt_alert(self):
        person_data = next(generated_person())
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        with allure.step('Switch to the alert'):
            alert_window = self.switch_to_alert()
        with allure.step('Send to alert random full name'):
            alert_window.send_keys(person_data.full_name)
        with allure.step('Accept alert'):
            alert_window.accept()
        with allure.step('Get prompt result text'):
            text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return person_data.full_name, text_result


class FramesPage(BasePage):

    locators = FramesPageLocators()

    @allure.step('Check frames')
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            with allure.step('Get frame width and height'):
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
            with allure.step('Switch to the frame'):
                self.driver.switch_to.frame(frame)
            with allure.step('Get frame text'):
                text_frame = self.element_is_present(self.locators.TITLE_FRAME).text
            with allure.step('Switch to default content'):
                self.driver.switch_to.default_content()
            return [text_frame, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            with allure.step('Get frame width and height'):
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
            with allure.step('Switch to the frame'):
                self.driver.switch_to.frame(frame)
            with allure.step('Get frame text'):
                text_frame = self.element_is_present(self.locators.TITLE_FRAME).text
            with allure.step('Switch to default content'):
                self.driver.switch_to.default_content()
            return [text_frame, width, height]


class NestedFramesPage(BasePage):

    locators = NestedFramesPageLocators()

    @allure.step('Check nested frames')
    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        with allure.step('Switch to the parent frame'):
            self.driver.switch_to.frame(parent_frame)
        with allure.step('Get text from the parent frame'):
            parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        with allure.step('Switch to the child frame'):
            self.driver.switch_to.frame(child_frame)
        with allure.step('Get text from the child frame'):
            child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):

    locators = ModalDialogPageLocators()

    @allure.step('Check small modal dialog')
    def check_small_modal_dialog(self):
        with allure.step('Click on the Small modal button'):
            self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        with allure.step('Get title text from the small modal dialog'):
            title_text = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        with allure.step('Get body text from small modal dialog'):
            body_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        with allure.step('Click on the close button'):
            self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return title_text, len(body_text)

    @allure.step('Check large modal dialog')
    def check_large_modal_dialog(self):
        with allure.step('Click on the Large modal button'):
            self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        with allure.step('Get title text from the large modal dialog'):
            title_text = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        with allure.step('Get body text from large modal dialog'):
            body_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        with allure.step('Click on the close button'):
            self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return title_text, len(body_text)

