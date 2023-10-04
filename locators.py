from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REG_BUTTON_IN_ENTRY = (By.XPATH, "//a[@href='/register']")
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REG_INPUT = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    # NAME = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')[0]
    EMAIL_ENTRY = (By.XPATH, '//input[@name="name"]')
    PASSWORD_ENTRY = (By.XPATH, '//input[@name="Пароль"]')
    ENTRY_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
