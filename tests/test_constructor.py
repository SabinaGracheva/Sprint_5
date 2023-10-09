from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import ConstructorPageLocators


class TestConstructor:
    # переход к разделу «Булки»
    def test_go_to_the_bagels_section(self, driver):
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_SAUCES_BUTTON)).click()
        driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_BAGELS_BUTTON).click()
        assert driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_ACTIVE_BUTTON).text == 'Булки'

    # переход к разделу «Соусы»
    def test_go_to_the_sauces_section(self, driver):
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_SAUCES_BUTTON)).click()
        assert driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_ACTIVE_BUTTON).text == 'Соусы'

    # переход к разделу «Начинки»
    def test_go_to_the_fillings_section(self, driver):
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_FILLINGS_BUTTON)).click()
        assert driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_FILLINGS_BUTTON).text == 'Начинки'
