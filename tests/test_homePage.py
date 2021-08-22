import pytest
from conftest import *
from pageObjects.homePage import HomePage


@pytest.mark.usefixtures("setupBrowser")
class TestHomePage:

    @pytest.fixture()
    def homePage(self):  #create an object from home page class
        self.homePage = HomePage(self.driver)
        return self.homePage

    def test_upperNavigatorUI(self, homePage):
        assert self.homePage.protoCommerceE().text == "ProtoCommerce"
        assert self.homePage.homeBtnLinkE().text == "Home"
        assert self.homePage.shopBtnLinkE().text == "Shop"





