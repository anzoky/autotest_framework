import time

from pages.alerts_frame_windows_page import BrowserWindowPage, AlertsPage
from conftest import driver


class TestAlertsFrameWindow:

    class TestBrowserWindows:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'The new tab has not opened or an incorrect tab has opened'

        def test_new_window(self, driver):
            new_window_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', 'The new window has not opened or an incorrect window has opened'

    class TestAlertsPage:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        def test_alert_appear_after_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        def test_confirm_alert_accept(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert_accept()
            assert alert_text == 'You selected Ok', 'Alert did not show up'

        def test_confirm_alert_dismiss(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert_dismiss()
            assert alert_text == 'You selected Cancel', 'Alert did not show up'

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            person_data, prompt_result = alert_page.check_prompt_alert()
            assert person_data in prompt_result, 'Alert did not show up'
