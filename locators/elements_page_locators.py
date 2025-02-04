

class TextBoxPageLocators:

    # form fields - форма для заполнения

    FULL_NAME = ('xpath', '//input[@id="userName"]')
    EMAIL = ('xpath', '//input[@id="userEmail"]')
    CURRENT_ADDRESS = ('xpath', '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = ('xpath', '//textarea[@id="permanentAddress"]')
    SUBMIT = ('xpath', '//button[@id="submit"]')

    # created form - заполненная форма

    CREATED_FULL_NAME = ('xpath', '//p[@id="name"]')
    CREATED_EMAIL = ('xpath', '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = ('xpath', '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = ('xpath', '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:

    # checkboxes - чекбоксы

    EXPAND_ALL_BUTTON = ('xpath', '//button[@class="rct-option rct-option-expand-all"]')
    ITEM_LIST = ('xpath', '//span[@class="rct-title"]')
    CHECKED_ITEMS = ('css selector', 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ('xpath', './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = ('xpath', '//span[@class="text-success"]')


class RadioButtonPageLocators:

    # radiobuttons - радиокнопки

    YES_RADIOBUTTON = ('xpath', '//label[@for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = ('xpath', '//label[@for="impressiveRadio"]')
    NO_RADIOBUTTON = ('xpath', '//label[@for="noRadio"]')
    OUTPUT_RADIOBUTTON_RESULT = ('xpath', '//span[@class="text-success"]')


class WebTablePageLocators:

    # add person form - форма для добавления людей
    ADD_BUTTON = ('xpath', '//button[@id="addNewRecordButton"]')
    FIRST_NAME_INPUT = ('xpath', '//input[@id="firstName"]')
    LASTNAME_INPUT = ('xpath', '//input[@id="lastName"]')
    EMAIL_INPUT = ('xpath', '//input[@id="userEmail"]')
    AGE_INPUT = ('xpath', '//input[@id="age"]')
    SALARY_INPUT = ('xpath', '//input[@id="salary"]')
    DEPARTMENT_INPUT = ('xpath', '//input[@id="department"]')
    SUBMIT_BUTTON = ('xpath', '//button[@id="submit"]')

    # table - таблица

    FULL_PEOPLE_LIST = ('xpath', '//div[@class="rt-tr-group"]')
    SEARCH_INPUT = ('xpath', '//input[@id="searchBox"]')
    DELETE_BUTTON = ('xpath', '//span[@title="Delete"]')
    ROW_PARENT = ('xpath', './/ancestor::div[@class="rt-tr-group"]')
    NO_ROWS_FOUND = ('xpath', '//div[@class="rt-noData"]')
    NUMBER_OF_ROWS = ('xpath', '//select[@aria-label="rows per page"]')

    # update - обновление

    UPDATE_BUTTON = ('xpath', '//span[@title="Edit"]')


class ButtonsPageLocators:

    DOUBLE_CLICK_BUTTON = ('xpath', '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = ('xpath', '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = ('xpath', '//button[text()="Click Me"]')

    # result

    SUCCESS_DOUBLE = ('xpath', '//p[@id="doubleClickMessage"]')
    SUCCESS_RIGHT = ('xpath', '//p[@id="rightClickMessage"]')
    SUCCESS_CLICK_ME = ('xpath', '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:

    SIMPLE_LINK = ('xpath', '//a[@id="simpleLink"]')


class UploadAndDownloadLocators:

    UPLOAD_FILE = ('xpath', '//input[@id="uploadFile"]')
    UPLOADED_RESULT = ('xpath', '//p[@id="uploadedFilePath"]')

    DOWNLOAD_FILE = ('xpath', '//a[@id="downloadButton"]')


class DynamicPropertiesLocators:

    ENABLE_AFTER_5_SECONDS_BUTTON = ('xpath', '//button[@id="enableAfter"]')
    COLOR_CHANGE_BUTTON = ('xpath', '//button[@id="colorChange"]')
    VISIBLE_AFTER_5_SECONDS_BUTTON = ('xpath', '//button[@id="visibleAfter"]')
