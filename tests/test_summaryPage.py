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
