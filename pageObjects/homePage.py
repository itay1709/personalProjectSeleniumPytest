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
    nameAlertMinChar = "Name should be at least 2 characters"
    nameAlertEmptyChar = "Name is required"
    genderDropDown = ['Male', 'Female']
    formE2eName = "Itay"
    formE2eEmail = "itayzisman@gmail.com"
    formE2ePassword = "itay1234"
    successMsgAlert = "Success! The Form has been submitted successfully!"




    #locators:
    protoCommerce = (By.CLASS_NAME, "navbar-brand")
    homeBtnLink = (By.LINK_TEXT, "Home")
    shopBtnLink = (By.LINK_TEXT, "Shop")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    nameField = (By.XPATH, "//label[text()='Name']")
    nameInput = (By.NAME, "name")
    nameAlert = (By.XPATH, "//div[@class='alert alert-danger']")
    email = (By.XPATH, "//form/div[2]/label")
    emailInput = (By.XPATH, "//form/div[2]/input")
    password = (By.XPATH, "//form/div[3]/label")
    passwordInput = (By.XPATH, "//form/div[3]/input")
    checkBox = (By.XPATH, "//form/div[4]/input")
    checkBoxText = (By.XPATH, "//form/div[4]/label")
    gender = (By.XPATH, "//form/div[5]/label")
    genderSelect = (By.ID, "exampleFormControlSelect1")
    employmentStatus = (By.XPATH, "//form/div[6]/label")
    studentRadioBtn = (By.ID, "inlineRadio1")
    employedRadioBtn = (By.ID, "inlineRadio2")
    entrepreneurRadioBtn = (By.ID, "inlineRadio3")
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

    def nameFieldE(self):
        return self.driver.find_element(*HomePage.nameField)

    def nameInputE(self):
        return self.driver.find_element(*HomePage.nameInput)

    def nameAlertE(self):
        return self.driver.find_element(*HomePage.nameAlert)

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

    def genderE(self):
        return self.driver.find_element(*HomePage.gender)

    def genderSelectE(self):
        return self.driver.find_element(*HomePage.genderSelect)

    def employmentStatusE(self):
        return self.driver.find_element(*HomePage.employmentStatus)

    def studentRadioBtnE(self):
        return self.driver.find_element(*HomePage.studentRadioBtn)

    def employedRadioBtnE(self):
        return self.driver.find_element(*HomePage.employedRadioBtn)

    def entrepreneurRadioBtnE(self):
        return self.driver.find_element(*HomePage.entrepreneurRadioBtn)

    def dateOfBirthE(self):
        return self.driver.find_element(*HomePage.dateOfBirth)

    def dateOfBirthInputE(self):
        return self.driver.find_element(*HomePage.dateOfBirthInput)

    def submitBtnE(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def successMsgE(self):
        return self.driver.find_element(*HomePage.successMsg)
