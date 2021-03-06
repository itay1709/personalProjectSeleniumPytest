import pytest

from pageObjects.homePage import HomePage
from pageObjects.shopPage import ShopPage


@pytest.mark.usefixtures("setupBrowser")
class TestShopPage:

    @pytest.fixture()
    def homePage(self):
        self.homePage = HomePage(self.driver)
        return self.homePage

    @pytest.fixture()
    def shopPage(self):
        self.shopPage = ShopPage(self.driver)
        return self.shopPage

    def test_validateSideMenu(self, homePage, shopPage ):
        self.categorySideMenuA = []
        self.homePage.shopBtnLinkE().click()
        assert self.shopPage.shopHeadlineE().text == "Shop Name"
        for i in self.shopPage.categoriesE():
            self.categorySideMenuA.append(i.text)
        assert self.categorySideMenuA == self.shopPage.categoriesSideMenu
        self.homePage.homeBtnLinkE().click()

    def test_validateDevicesList(self, homePage, shopPage ):
        self.devicesListA = []
        self.homePage.shopBtnLinkE().click()
        for i in self.shopPage.cardDevicesNameE():
            self.devicesListA.append(i.text)
        assert self.devicesListA == self.shopPage.devices
        self.homePage.homeBtnLinkE().click()

    def test_validateCategoryNavigation(self, homePage, shopPage ):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.categoriesE()[0].click()
        assert self.homePage.nameFieldE().is_enabled()
        self.homePage.homeBtnLinkE().click()

    def test_validateCategoryNavigation1(self, homePage, shopPage ):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.categoriesE()[1].click()
        assert self.homePage.nameFieldE().is_enabled()
        self.homePage.homeBtnLinkE().click()

    def test_validateCategoryNavigation2(self, homePage, shopPage ):
        self.homePage.shopBtnLinkE().click()
        self.shopPage.categoriesE()[2].click()
        assert self.homePage.nameFieldE().is_enabled()
        self.homePage.homeBtnLinkE().click()

    def test_validateCheckOutBtnCounter(self, homePage, shopPage ):
        self.homePage.shopBtnLinkE().click()
        for i in self.shopPage.cardDevicesAddBtnE():
            i.click()
        assert "( 4 )" in self.shopPage.checkOutBtnE().text
        self.homePage.homeBtnLinkE().click()

