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


class NestedFramesPageLocators:

    PARENT_FRAME = ('xpath', '//iframe[@id="frame1"]')
    PARENT_TEXT = ('css selector', 'body')
    CHILD_FRAME = ('xpath', '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = ('xpath', '//p[text()="Child Iframe"]')


class ModalDialogPageLocators:

    SMALL_MODAL_BUTTON = ('xpath', '//button[@id="showSmallModal"]')
    SMALL_MODAL_CLOSE_BUTTON = ('xpath', '//button[@id="closeSmallModal"]')
    TITLE_SMALL_MODAL = ('xpath', '//div[@id="example-modal-sizes-title-sm"]')
    BODY_SMALL_MODAL = ('xpath', '//div[@class="modal-body"]')
    LARGE_MODAL_BUTTON = ('xpath', '//button[@id="showLargeModal"]')
    LARGE_MODAL_CLOSE_BUTTON = ('xpath', '//button[@id="closeLargeModal"]')
    TITLE_LARGE_MODAL = ('xpath', '//div[@id="example-modal-sizes-title-lg"]')
    BODY_LARGE_MODAL = ('xpath', '//div[@class="modal-body"]')