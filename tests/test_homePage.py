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
        assert self.homePage.protoCommerceE().text == self.homePage.upperNavigatorFirstETxt
        assert self.homePage.homeBtnLinkE().text == self.homePage.upperNavigatorSecondETxt
        assert self.homePage.shopBtnLinkE().text == self.homePage.upperNavigatorThirdETxt

    def test_upperNavigatorTagType(self, homePage):
        assert self.homePage.protoCommerceE().tag_name == "a"
        assert self.homePage.homeBtnLinkE().tag_name == "a"
        assert self.homePage.shopBtnLinkE().tag_name == "a"





