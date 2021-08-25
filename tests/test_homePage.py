import pytest
from selenium.webdriver.common.keys import Keys

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

    def test_minCharNameFieldError(self, homePage):
        self.homePage.nameInputE().send_keys("a")
        self.homePage.nameFieldE().click()
        assert self.homePage.nameAlertE().text == self.homePage.nameAlertMinChar
        self.homePage.homeBtnLinkE().click()

    def test_emptyCharNameFieldError(self, homePage):
        self.homePage.nameInputE().click()
        self.homePage.nameFieldE().click()
        assert self.homePage.nameAlertE().text == self.homePage.nameAlertEmptyChar
        self.homePage.homeBtnLinkE().click()

    def test_validateGenderDropdown(self, homePage):
        self.GenderDropdownA = []
        self.genderSelect = Select(self.homePage.genderSelectE())
        self.GenderDropdownO = self.genderSelect.options
        for i in self.GenderDropdownO:
            self.GenderDropdownA.append(i.get_attribute('value'))
        assert self.GenderDropdownA == self.homePage.genderDropDown

    def test_validateFormFields(self, homePage):
        assert self.homePage.nameFieldE().text == "Name"
        assert self.homePage.nameInputE().is_displayed()
        assert self.homePage.emailE().text == "Email"
        assert self.homePage.emailInputE().is_displayed()
        assert self.homePage.passwordE().text == "Password"
        assert self.homePage.passwordInputE().is_displayed()
        assert self.homePage.checkBoxE().is_enabled()
        assert self.homePage.checkBoxTextE().text == "Check me out if you Love IceCreams!"
        assert self.homePage.genderE().text == "Gender"
        assert self.homePage.employmentStatusE().text == "Employment Status:"
        assert self.homePage.dateOfBirthE().text == "Date of Birth"
        assert self.homePage.submitBtnE().is_enabled()
        assert self.homePage.submitBtnE().get_attribute('value') == "Submit"

    def test_validateRadioBtn(self, homePage):
        assert self.homePage.employedRadioBtnE().is_enabled()
        assert self.homePage.studentRadioBtnE().is_enabled()
        assert not self.homePage.entrepreneurRadioBtnE().is_enabled()  # entrepreneur btn should be disable

    def test_dateInputType(self, homePage):
        assert self.homePage.dateOfBirthInputE().get_attribute("type") == "date"

    def test_e2eForm(self, homePage):
        self.homePage.nameInputE().send_keys(self.homePage.formE2eName)
        self.homePage.emailInputE().send_keys(self.homePage.formE2eEmail)
        self.homePage.passwordInputE().send_keys(self.homePage.formE2ePassword)
        self.homePage.checkBoxE().click()
        self.genderSelect = Select(self.homePage.genderSelectE())
        self.genderSelect.select_by_index(1)
        self.homePage.employedRadioBtnE().click()
        self.homePage.dateOfBirthInputE().send_keys("1709")
        self.homePage.dateOfBirthInputE().send_keys(Keys.TAB)
        self.homePage.dateOfBirthInputE().send_keys("1986")
        self.homePage.submitBtnE().click()
        assert self.homePage.successMsgAlert in self.homePage.successMsgE().text
        self.homePage.homeBtnLinkE().click()

    @pytest.mark.parametrize("genderIndex", [0, 1])
    def test_e2eFormDDDT(self, homePage, genderIndex):  # connect the parmeter to the function by giving the param name
        self.homePage.nameInputE().send_keys(self.homePage.formE2eName)
        self.homePage.emailInputE().send_keys(self.homePage.formE2eEmail)
        self.homePage.passwordInputE().send_keys(self.homePage.formE2ePassword)
        self.homePage.checkBoxE().click()
        self.genderSelect = Select(self.homePage.genderSelectE())
        self.genderSelect.select_by_index(genderIndex)  # use the param name
        self.homePage.submitBtnE().click()
        assert self.homePage.successMsgAlert in self.homePage.successMsgE().text











