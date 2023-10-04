from selenium.webdriver.common.by import By


class Locators:
    LOGIN_EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода email на странице авторизации
    LOGIN_PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля на странице авторизации
    LOGIN_BUTTON_ON_THE_LOGIN_PAGE = (By.XPATH, "//button[text()='Войти']")  # кнопка "Вход" на странице авторизации
    BUILD_A_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')  # тест "Соберите бургер" на главной странице
    LOGIN_BUTTON_ON_THE_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"
