from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from locators import Locators


class TestConstructor:
    # переход к разделу «Булки»
    def test_go_to_the_bagels_sectione(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER))
        driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()
        driver.find_element(By.XPATH, '//span[text()="Булки"]').click()
        assert driver.find_element(By.XPATH,
                                   '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'
                                   '/span[text()="Булки"]')

    # переход к разделу «Соусы»
    def test_go_to_the_sauces_sectione(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER))
        driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()
        assert driver.find_element(By.XPATH,
                                   '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'
                                   '/span[text()="Соусы"]')

    # переход к разделу «Начинки»
    def test_go_to_the_fillings_sectione(self, driver, login):
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUILD_A_BURGER))
        driver.find_element(By.XPATH, '//span[text()="Начинки"]').click()
        assert driver.find_element(By.XPATH,
                                   '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'
                                   '/span[text()="Начинки"]')
