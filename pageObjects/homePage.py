import pytest
from selenium.webdriver.common.by import By


class HomePage:

    #contructor:
    def __init__(self, driver):
        self.driver = driver

    #test data
    upperNavigatorFirstETxt = "ProtoCommerce"
    upperNavigatorSecondETxt = "Home"
    upperNavigatorThirdETxt = "Shop"

    #locators:
    protoCommerce = (By.CLASS_NAME, "navbar-brand")
    homeBtnLink = (By.LINK_TEXT, "Home")
    shopBtnLink = (By.LINK_TEXT, "Shop")

    nameField = (By.XPATH, "//label[text()='Name']")
    nameInput = (By.NAME, "name")
    nameAlert = (By.XPATH, "//div[text()='Name is required']")
    email = (By.XPATH, "//form/div[2]/label")
    emailInput = (By.XPATH, "//form/div[2]/input")
    password = (By.XPATH, "//form/div[3]/label")
    passwordInput = (By.XPATH, "//form/div[3]/input")
    checkBox = (By.XPATH, "//form/div[4]/input")
    checkBoxText = (By.XPATH, "//form/div[4]/label")
    gender = (By.XPATH, "//form/div[5]/label")
    genderSelect = (By.ID, "exampleFormControlSelect1")
    employmentStatus = (By.XPATH, "//form/div[6]/label")
    studentCheckBox = (By.ID, "inlineRadio1")
    employedCheckBox = (By.ID, "inlineRadio2")
    entrepreneurCheckBox = (By.ID, "inlineRadio3")
    student = (By.XPATH, "//form/div[6]/div[1]/label")
    dateOfBirth = (By.XPATH, "//form/div[7]/label")
    dateOfBirthInput = (By.XPATH, "//form/div[7]/input")

    submitBtn = (By.XPATH, "//input[@value='Submit']")

    #elements:
    def protoCommerceE(self):
        return self.driver.find_element(*HomePage.protoCommerce)

    def homeBtnLinkE(self):
        return self.driver.find_element(*HomePage.homeBtnLink)

    def shopBtnLinkE(self):
        return self.driver.find_element(*HomePage.shopBtnLink)

    def emailE(self):
        return self.driver.find_element(*HomePage.email)

    def emailInputE(self):
        return self.driver.find_element(*HomePage.emailInput)

    def passwordE(self):
        return self.driver.find_element(*HomePage.password)

    def passwordInputE(self):
        return self.driver.find_element(*HomePage.passwordInput)

    def checkBoxE(self):
        return self.driver.find_element(*HomePage.checkBox)

    def checkBoxTextE(self):
        return self.driver.find_element(*HomePage.checkBoxText)

    def genderSelectE(self):
        return self.driver.find_element(*HomePage.genderSelect)

    def studentCheckBoxE(self):
        return self.driver.find_element(*HomePage.studentCheckBox)

    def employedCheckBoxE(self):
        return self.driver.find_element(*HomePage.employedCheckBox)

    def entrepreneurCheckBoxE(self):
        return self.driver.find_element(*HomePage.entrepreneurCheckBox)

    def dateOfBirthInputE(self):
        return self.driver.find_element(*HomePage.dateOfBirthInput)

    def submitBtnE(self):
        return self.driver.find_element(*HomePage.submitBtn)
