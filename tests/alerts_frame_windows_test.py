import time

from pages.alerts_frame_windows_page import BrowserWindowPage
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
