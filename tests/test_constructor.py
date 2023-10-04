from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from locators import Locators


class TestConstructor:
    # переход к разделу «Булки»
    def test_go_to_the_bagels_sectione(self, driver, login):
        text = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER)).text
        assert text == "Соберите бургер"
