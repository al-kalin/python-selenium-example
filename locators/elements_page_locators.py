from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:

    TREE_SWITCHER_LIST = (By.CSS_SELECTOR, "span.rc-tree-switcher_close")
    CHECK_BOX_LIST = (By.CSS_SELECTOR, "span.rc-tree-checkbox")
    CHECK_BOX_TITLE_LIST = (By.CSS_SELECTOR, "span[class='rc-tree-title']")
    CHECKED_ITEMS = (
        By.CSS_SELECTOR,
        "div[role='treeitem'].rc-tree-treenode-checkbox-checked",
    )
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rc-tree-title']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    """
    Locators for the Radio Button page elements.

    """

    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='form-check'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (
        By.CSS_SELECTOR,
        "label[class^='form-check'][for='impressiveRadio']",
    )
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='form-check'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:

    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPYT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "tbody tr td")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
