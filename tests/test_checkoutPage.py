import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkOutPage import CheckOutPage
from pageObjects.homePage import HomePage
from pageObjects.shopPage import ShopPage
from pageObjects.summaryPage import SummaryPage


@pytest.mark.usefixtures("setupBrowser")
class TestCheckoutPage:

    @pytest.fixture()
    def checkOutPage(self):
        self.checkOutPage = CheckOutPage(self.driver)
        return self.checkOutPage

    @pytest.fixture()
    def homePage(self):
        self.homePage = HomePage(self.driver)
        return self.homePage

    @pytest.fixture()
    def shopPage(self):
        self.shopPage = ShopPage(self.driver)
        return self.shopPage

    @pytest.fixture()
    def summaryPage(self):
        self.summaryPage = SummaryPage(self.driver)
        return self.summaryPage

    def test_validateElementsOnScreen(self, checkOutPage, homePage, summaryPage, shopPage):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.checkOutBtnE().click()
        self.summaryPage.checkOutBtnE().click()
        assert self.checkOutPage.checkOutBtnE().is_displayed()
        assert self.checkOutPage.locationHeaderE().text == self.checkOutPage.locationHeaderTxt
        assert self.checkOutPage.inputCountryE().is_displayed()
        assert not self.checkOutPage.checkBoxE().is_selected()
        assert self.checkOutPage.checkBoxTxt in self.checkOutPage.checkBoxTextE().text
        assert self.checkOutPage.purchaseBtnE().is_displayed()
        self.checkOutPage.homeBtnE().click()

    def test_validateTermsAndConditionPopup(self, checkOutPage, homePage, summaryPage, shopPage):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.checkOutBtnE().click()
        self.summaryPage.checkOutBtnE().click()
        self.checkOutPage.checkBoxTermsE().click()
        assert self.checkOutPage.tACHeaderE().text == "Terms And Conditions"
        assert self.checkOutPage.tACTxtE().text == self.checkOutPage.termsAndConditionTxt
        assert self.checkOutPage.tACCloseBtnE().is_displayed()
        assert self.checkOutPage.tACXBtnE().is_displayed()
        self.checkOutPage.tACCloseBtnE().click()
        self.checkOutPage.homeBtnE().click()

    @pytest.mark.skip
    def test_validateCheckBoxEnable(self, checkOutPage, homePage, summaryPage, shopPage):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.checkOutBtnE().click()
        self.summaryPage.checkOutBtnE().click()
        assert not self.checkOutPage.checkBoxE().is_selected()
        actions = ActionChains(self.driver)
        actions.move_to_element(self.checkOutPage.checkBoxE()).click().perform()
        assert self.checkOutPage.checkBoxE().is_selected()

    def test_validateSearchCountry(self, checkOutPage, homePage, summaryPage, shopPage):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.checkOutBtnE().click()
        self.summaryPage.checkOutBtnE().click()
        self.checkOutPage.inputCountryE().send_keys("in")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.checkOutPage.countryResults))
        for i in self.checkOutPage.countryResultsE():
            assert "in" or "In" in i.text
        self.checkOutPage.homeBtnE().click()


