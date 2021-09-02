import pytest

from pageObjects.homePage import HomePage
from pageObjects.shopPage import ShopPage
from pageObjects.summaryPage import SummaryPage


@pytest.mark.usefixtures("setupBrowser")
class TestSummaryPage:

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

    def test_validateEmptyTable(self, homePage, shopPage, summaryPage):
        tableHeadA = []
        self.homePage.shopBtnLinkE().click()
        self.shopPage.checkOutBtnE().click()
        for i in self.summaryPage.tableHeadE():
            tableHeadA.append(i.text)
        assert tableHeadA == SummaryPage.tableHeadTxt
        assert self.summaryPage.continueShoppingBtnE().is_enabled()
        assert self.summaryPage.checkOutBtnE().is_enabled()
        assert self.summaryPage.tableTotalE().text == "Total"
        assert "0" in self.summaryPage.tableAmountE().text
        self.homePage.homeBtnLinkE().click()

    def test_validateAddOneDevice(self, homePage, shopPage, summaryPage):
        self.homePage.shopBtnLinkE().click()
        deviceNameA = self.shopPage.cardDevicesNameE()[1].text
        self.shopPage.cardDevicesAddBtnE()[1].click()
        assert "1" in self.shopPage.checkOutBtnE().text
        self.shopPage.checkOutBtnE().click()
        assert self.summaryPage.tableDeviceNameE()[0].text == deviceNameA
        assert self.summaryPage.tableQuantityE()[0].get_attribute("value") == "1"
        assert self.summaryPage.tablePriceE()[0].text == self.summaryPage.tablePriceTotE()[0].text == self.summaryPage.tableAmountE().text
        self.homePage.homeBtnLinkE().click()

    def test_validateAddTwoOfTheSameDevice(self, homePage, shopPage, summaryPage):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.cardDevicesAddBtnE()[1].click()
        self.shopPage.checkOutBtnE().click()
        self.summaryPage.tableQuantityE()[0].clear()
        self.summaryPage.tableQuantityE()[0].send_keys("2")
        priceTxt = self.summaryPage.tablePriceE()[0].text[3:]        # substring price string element
        priceInt = int(priceTxt)                                     # convert stirng to int
        priceTotTxt = self.summaryPage.tablePriceTotE()[0].text[3:]  # substring price total string element
        priceTotInt = int(priceTotTxt)                               # convert stirng to int
        assert priceInt * 2 == priceTotInt
        self.homePage.homeBtnLinkE().click()

    def test_validateRemoveLastDevice(self, homePage, shopPage, summaryPage):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.cardDevicesAddBtnE()[1].click()
        self.shopPage.checkOutBtnE().click()
        assert self.summaryPage.tableQuantityE()[0].is_enabled
        self.summaryPage.tableRemoveBtnE()[0].click()
        assert not self.summaryPage.tableQuantityE()
        tableTotPriceTxt = self.summaryPage.tableAmountE().text[3:]
        tableTotPriceInt = int(tableTotPriceTxt)
        assert tableTotPriceInt == 0

    def test_validateAddAllDevice(self, homePage, shopPage, summaryPage ):
        self.homePage.shopBtnLinkE().click()
        deviceNameListSP = []                                    # SP = Shop Page
        for i in self.shopPage.cardDevicesNameE():
            deviceNameListSP.append(i.text)
        for i in self.shopPage.cardDevicesAddBtnE():
            i.click()
        self.shopPage.checkOutBtnE().click()
        deviceNameListSUP = []                                       # SUP = Summary Page
        for i in self.summaryPage.tableDeviceNameE():
            deviceNameListSUP.append(i.text)
        assert deviceNameListSUP == deviceNameListSP
        priceTxt = []
        #breakpoint()
        for i in self.summaryPage.tablePriceE():
            priceTxt.append(i.text[3:])
        priceInt = []
        for i in priceTxt:
            priceInt.append(int(i))
        SumPrice = sum(priceInt)
        tableTotPriceTxt = self.summaryPage.tableAmountE().text[3:]
        tableTotPriceInt = int(tableTotPriceTxt)
        assert SumPrice == tableTotPriceInt

