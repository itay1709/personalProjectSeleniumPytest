import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkOutPage import CheckOutPage
from pageObjects.homePage import HomePage
from pageObjects.shopPage import ShopPage
from pageObjects.summaryPage import SummaryPage


@pytest.mark.usefixtures("setupBrowser")
class TestE2E:

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

    def test_purchaseOneDevice(self, checkOutPage, homePage, shopPage, summaryPage):
        self.homePage.shopBtnLinkE().click()
        for j in range(1, 2):
            self.shopPage.cardDevicesAddBtnE()[j].click()
        for j in range(1, 2):
            deviceNameA = self.shopPage.cardDevicesNameE()[j].text
        checkOutBtnSP = self.shopPage.checkOutBtnE().text
        self.shopPage.checkOutBtnE().click()
        assert deviceNameA == self.summaryPage.tableDeviceNameE()[0].text
        assert self.summaryPage.tableQuantityE()[0].get_attribute("value") == "1"
        self.summaryPage.checkOutBtnE().click()
        assert checkOutBtnSP == self.checkOutPage.checkOutBtnE().text
        self.checkOutPage.inputCountryE().send_keys("in")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.checkOutPage.countryResults))
        for i in self.checkOutPage.countryResultsE():
            if i.text == "Finland":
                i.click()
                break
        self.checkOutPage.purchaseBtnE().click()
        assert self.checkOutPage.successMsgTxt in self.checkOutPage.successMsgE().text
        self.checkOutPage.homeBtnE().click()

    def test_purchaseTwoDevices(self, checkOutPage, homePage, shopPage, summaryPage):
        self.homePage.shopBtnLinkE().click()
        deviceNameA = []
        for j in range(1, 3):
            self.shopPage.cardDevicesAddBtnE()[j].click()
        for j in range(1, 3):
            deviceNameA.append(self.shopPage.cardDevicesNameE()[j].text)
        checkOutBtnSP = self.shopPage.checkOutBtnE().text
        self.shopPage.checkOutBtnE().click()
        deviceNameListSUP = []  # SUP = Summary Page
        for i in self.summaryPage.tableDeviceNameE():
            deviceNameListSUP.append(i.text)
        assert deviceNameA == deviceNameListSUP
        for i in self.summaryPage.tableQuantityE():
            assert i.get_attribute("value") == "1"
        self.summaryPage.checkOutBtnE().click()
        self.checkOutPage.inputCountryE().send_keys("in")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.checkOutPage.countryResults))
        for i in self.checkOutPage.countryResultsE():
            if i.text == "Finland":
                i.click()
                break
        self.checkOutPage.purchaseBtnE().click()
        assert self.checkOutPage.successMsgTxt in self.checkOutPage.successMsgE().text
        self.checkOutPage.homeBtnE().click()
