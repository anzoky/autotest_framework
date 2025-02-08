import time

from generator.generator import generated_person
from locators.alerts_frame_windows_locators import BrowserWindowPageLocators, AlertsPageLocators, FramesPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):

    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW_WINDOW).text
        return text_title


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_text = alert_window.text
        alert_window.accept()
        return alert_text

    def check_alert_appear_after_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_text = alert_window.text
        alert_window.accept()
        return alert_text

    def check_confirm_alert_accept(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_confirm_alert_dismiss(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.dismiss()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        person_data = next(generated_person())
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(person_data.full_name)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return person_data.full_name, text_result


class FramesPage(BasePage):

    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text_frame = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text_frame, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text_frame = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text_frame, width, height]


