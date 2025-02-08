class BrowserWindowPageLocators:

    NEW_TAB_BUTTON = ('xpath', '//button[@id="tabButton"]')
    NEW_WINDOW_BUTTON = ('xpath', '//button[@id="windowButton"]')

    TITLE_NEW_TAB = ('xpath', '//h1[@id="sampleHeading"]')
    TITLE_NEW_WINDOW = ('xpath', '//h1[@id="sampleHeading"]')


class AlertsPageLocators:

    SEE_ALERT_BUTTON = ('xpath', '//button[@id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = ('xpath', '//button[@id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = ('xpath', '//button[@id="confirmButton"]')
    PROMPT_BOX_ALERT_BUTTON = ('xpath', '//button[@id="promtButton"]')

    CONFIRM_RESULT = ('xpath', '//span[@id="confirmResult"]')
    PROMPT_RESULT = ('xpath', '//span[@id="promptResult"]')


class FramesPageLocators:

    FIRST_FRAME = ('xpath', '//iframe[@id="frame1"]')
    SECOND_FRAME = ('xpath', '//iframe[@id="frame2"]')
    TITLE_FRAME = ('xpath', '//h1[@id="sampleHeading"]')