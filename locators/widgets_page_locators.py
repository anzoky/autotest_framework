import random


class AccordianPageLocators:

    SECTION_FIRST = ('xpath', '//div[@id="section1Heading"]')
    SECTION_CONTENT_FIRST = ('xpath', '//div[@id="section1Content"]')
    SECTION_SECOND = ('xpath', '//div[@id="section2Heading"]')
    SECTION_CONTENT_SECOND = ('xpath', '//div[@id="section2Content"]')
    SECTION_THIRD = ('xpath', '//div[@id="section3Heading"]')
    SECTION_CONTENT_THIRD = ('xpath', '//div[@id="section3Content"]')


class AutoCompletePageLocators:

    MULTI_COMPLETE_INPUT = ('xpath', '//input[@id="autoCompleteMultipleInput"]')
    MULTI_VALUE = ('xpath', '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_REMOVE = ('xpath', '//div[@class="css-xb97g8 auto-complete__multi-value__remove"]')
    SINGLE_INPUT = ('xpath', '//input[@id="autoCompleteSingleInput"]')
    SINGLE_VALUE = ('xpath', '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')


class DataPickerPageLocators:

    # select date locators
    DATE_INPUT = ('xpath', '//input[@id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = ('xpath', '//select[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = ('xpath', '//select[@class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = ('css selector', 'div[class^="react-datepicker__day react-datepicker__day"]')

    # date and time locators
    INPUT_DATE_AND_TIME = ('xpath', '//input[@id="dateAndTimePickerInput"]')
    MONTH_DATE_AND_TIME = ('xpath', '//div[@class="react-datepicker__month-read-view"]')
    YEAR_DATE_AND_TIME = ('xpath', '//div[@class="react-datepicker__year-read-view"]')
    TIME_DATE_AND_TIME_LIST = ('xpath', '//li[@class="react-datepicker__time-list-item "]')
    MONTH_DATE_AND_TIME_LIST = ('xpath', '//div[@class="react-datepicker__month-option"]')
    YEAR_DATE_AND_TIME_LIST = ('xpath', '//div[@class="react-datepicker__year-option"]')


class SliderPageLocators:

    INPUT_SLIDER = ('xpath', '//input[@class="range-slider range-slider--primary"]')
    VALUE_SLIDER = ('xpath', '//input[@id="sliderValue"]')


class ProgressBarPageLocators:

    PROGRESS_BAR_BUTTON = ('xpath', '//button[@id="startStopButton"]')
    PROGRESS_BAR_VALUE = ('xpath', '//div[@class="progress-bar bg-info"]')


class TabsPageLocators:

    TABS_WHAT = ('xpath', '//a[@id="demo-tab-what"]')
    TABS_WHAT_CONTENT = ('xpath', '//div[@id="demo-tabpane-what"]')
    TABS_ORIGIN = ('xpath', '//a[@id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = ('xpath', '//div[@id="demo-tabpane-origin"]')
    TABS_USE = ('xpath', '//a[@id="demo-tab-use"]')
    TABS_USE_CONTENT = ('xpath', '//div[@id="demo-tabpane-use"]')
    TABS_MORE = ('xpath', '//a[@id="demo-tab-more"]')
    TABS_MORE_CONTENT = ('xpath', '//div[@id="demo-tabpane-more"]')


class ToolTipsPageLocators:

    HOVER_BUTTON = ('xpath', '//button[@id="toolTipButton"]')
    HOVER_BUTTON_TOOL_TIP = ('xpath', '//div[@id="buttonToolTip"]')

    HOVER_INPUT = ('xpath', '//input[@id="toolTipTextField"]')
    HOVER_INPUT_TOOL_TIP = ('xpath', '//div[@id="textFieldToolTip"]')

    LINK_CONTRARY = ('xpath', '//a[text()="Contrary"]')
    LINK_CONTRARY_TOOL_TIP = ('xpath', '//div[@id="contraryTexToolTip"]')

    LINK_FIGURES = ('xpath', '//a[text()="1.10.32"]')
    LINK_FIGURES_TOOL_TIP = ('xpath', '//div[@id="sectionToolTip"]')

    TOOL_TIPS_INNERS = ('xpath', '//div[@class="tooltip-inner"]')


class MenuPageLocators:

    MENU_ITEM_LIST = ('css selector', 'ul[id="nav"] li a')


class SelectMenuPageLocators:

    #list for cars
    cars = ['Volvo', 'Saab', 'Opel', 'Audi']

    SELECT_VALUE_INPUT = ('xpath', '//div[@id="withOptGroup"]')
    SELECT_VALUE_OPTIONS = ('xpath', '//div[contains(@id, "react-select-2-option-")]')
    SELECT_VALUE_RESULT = ('xpath', '//div[@class=" css-1uccc91-singleValue"]')

    SELECT_ONE_INPUT = ('xpath', '//div[@id="selectOne"]')
    SELECT_ONE_OPTIONS = ('xpath', '//div[contains(@id, "react-select-3-option-")]')
    SELECT_ONE_RESULT = ('xpath', '//div[@class=" css-1uccc91-singleValue"]')

    SELECT_MENU_COLOR = ('xpath', '//select[@id="oldSelectMenu"]')
    COLOR = ('xpath', f'//option[@value="{random.randint(1, 10)}"]')

    STANDARD_MULTI_SELECT_FOR_CARS = ('xpath', '//select[@id="cars"]')
    CHOOSE_CAR = ('xpath', f'//option[text()="{cars[random.randint(0, 3)]}"]')