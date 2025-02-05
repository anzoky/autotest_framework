import random


class FormPageLocators:

    #
    FIRST_NAME = ('xpath', '//input[@id="firstName"]')
    LAST_NAME = ('xpath', '//input[@id="lastName"]')
    EMAIL = ('xpath', '//input[@id="userEmail"]')
    GENDER = ('xpath', f'//label[@for="gender-radio-{random.randint(1, 3)}"]')
    MOBILE = ('xpath', '//input[@id="userNumber"]')
    DATE_OF_BIRTH = ('xpath', '//input[@id="dateOfBirthInput"]')
    SUBJECT = ('xpath', '//input[@id="subjectsInput"]')
    HOBBIES = ('xpath', f'//label[@for="hobbies-checkbox-{random.randint(1, 3)}"]')
    FILE_INPUT = ('xpath', '//input[@id="uploadPicture"]')
    CURRENT_ADDRESS = ('xpath', '//textarea[@id="currentAddress"]')
    SELECT_STATE = ('xpath', '//div[@id="state"]')
    STATE_INPUT = ('xpath', '//input[ @ id = "react-select-3-input"]')
    SELECT_CITY = ('xpath', '//div[@id="city"]')
    CITY_INPUT = ('xpath', '//input[ @ id = "react-select-4-input"]')
    SUBMIT = ('xpath', '//button[@id="submit"]')

    # table result
    RESULT_TABLE = ('xpath', '//div[@class="table-responsive"]//td[2]')