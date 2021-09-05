from selenium.webdriver.common.by import By


class CheckOutPage:

    #constructor:
    def __init__(self, driver):
        self.driver = driver

    #test data:
    locationHeaderTxt = "Please choose your delivery location.\nThen click on purchase button"
    checkBoxTxt = "I agree with the term & Conditions"
    termsAndConditionTxt = "Please read the following terms and conditions carefully as it sets out the terms of a " \
                           "legally binding agreement between you (the reader) and Business Standard Private Limited."

    #locators:
    checkOutBtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    locationHeader = (By.XPATH, "//label[@for='country']")
    inputCountry = (By.ID, "country")
    countryResults = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    checkBox = (By.ID, "checkbox2")
    checkBoxText = (By.XPATH, "//label[@for='checkbox2']")
    checkBoxTerms = (By.XPATH, "//label[@for='checkbox2']/a")
    purchaseBtn = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    homeBtn = (By.LINK_TEXT, "ProtoCommerce Home")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    successMsgBtn = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']/a")

    tACHeader = (By.XPATH, "//h1[normalize-space()='Terms And Conditions']")
    tACTxt = (By.XPATH, "//p[contains(text(), 'Please read the following terms and conditions')]")
    tACCloseBtn = (By.XPATH, "//button[@class='btn btn-info']")
    tACXBtn = (By.XPATH, "//button[@aria-label='Close']")

    #elements:
    def checkOutBtnE(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)

    def locationHeaderE(self):
        return self.driver.find_element(*CheckOutPage.locationHeader)

    def inputCountryE(self):
        return self.driver.find_element(*CheckOutPage.inputCountry)

    def countryResultsE(self):
        return self.driver.find_elements(*CheckOutPage.countryResults)

    def checkBoxE(self):
        return self.driver.find_element(*CheckOutPage.checkBox)

    def checkBoxTextE(self):
        return self.driver.find_element(*CheckOutPage.checkBoxText)

    def checkBoxTermsE(self):
        return self.driver.find_element(*CheckOutPage.checkBoxTerms)

    def purchaseBtnE(self):
        return self.driver.find_element(*CheckOutPage.purchaseBtn)

    def homeBtnE(self):
        return self.driver.find_element(*CheckOutPage.homeBtn)

    def successMsgE(self):
        return self.driver.find_element(*CheckOutPage.successMsg)

    def successMsgBtnE(self):
        return self.driver.find_element(*CheckOutPage.successMsgBtn)

    def tACHeaderE(self):
        return self.driver.find_element(*CheckOutPage.tACHeader)

    def tACTxtE(self):
        return self.driver.find_element(*CheckOutPage.tACTxt)

    def tACCloseBtnE(self):
        return self.driver.find_element(*CheckOutPage.tACCloseBtn)

    def tACXBtnE(self):
        return self.driver.find_element(*CheckOutPage.tACXBtn)


