from selenium.webdriver.common.by import By


class Locators:
    LOGIN_EMAIL = (By.XPATH, '//input[@name="name"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@name="Пароль"]')
    LOGIN_BUTTON_ON_THE_LOGIN_PAGE = (By.XPATH, "//button[text()='Войти']")
    BUILD_A_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')
    LOGIN_BUTTON_ON_THE_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')




    REG_BUTTON_IN_ENTRY = (By.XPATH, "//a[@href='/register']")
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REG_INPUT = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')

    CONSTRUCTOR = (By.XPATH, '//a[@href="/"]')
