from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')  # кнопка "Личный кабинет"
    CONSTRUCTOR = (By.XPATH, '//a[@href="/"]')  # кнопка "Конструктор"
    BUILD_A_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')  # тест "Соберите бургер" на главной странице


class AuthPageLocators:
    # Локаторы страницы входа в аккаунт
    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода email на странице авторизации
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"
    REG_BUTTON_IN_ENTRY = (By.XPATH, '//a[@href="/register"]')  # текст-ссылка "Зарегистрироваться"
    RESTORE_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]')  # текст-ссылка "Восстановить пароль"


class RegPageLocators:
    # Локаторы страницы регистрации
    CREATE_NAME = (By.XPATH, '(//input[@name="name"])[1]')  # поле ввода имени
    CREATE_EMAIL = (By.XPATH, '(//input[@name="name"])[2]')  # поле ввода email
    CREATE_PASSWORD = (By.XPATH, '//input[@name="Пароль"]')  # поле ввода пароля
    REG_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    ERR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]')  # сообщение об ошибке, что введен некорректный пароль


class PersonalAccountPageLocators:
    # Локаторы страницы "Личный кабинет"
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  # кнопка выхода из Личного кабинета


class ConstructorPageLocators:
    # Локаторы на странице конструктора
    CONSTRUCTOR_BAGELS_BUTTON = (By.XPATH, '//span[text()="Булки"]')  # раздел "Булки"
    CONSTRUCTOR_SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]')  # раздел "Соусы"
    CONSTRUCTOR_FILLINGS_BUTTON = (By.XPATH, '//span[text()="Начинки"]')  # раздел " Начинки"
    CONSTRUCTOR_ACTIVE_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')  # активная кнопка в конструкторе
