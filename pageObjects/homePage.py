import pytest
from selenium.webdriver.common.by import By


class HomePage:

    #contructor:
    def __init__(self, driver):
        self.driver = driver

    #locators:
    protoCommerce = (By.CLASS_NAME, "navbar-brand")
    homeBtnLink = (By.LINK_TEXT, "Home")
    shopBtnLink = (By.LINK_TEXT, "Shop")

    nameField = (By.XPATH, "//label[text()='Name']")
    nameInput = (By.NAME, "name")
    nameAlert = (By.XPATH, "//div[text()='Name is required']")




    #elements:
    def protoCommerceE(self):
        return self.driver.find_element(*HomePage.protoCommerce)

    def homeBtnLinkE(self):
        return self.driver.find_element(*HomePage.homeBtnLink)

    def shopBtnLinkE(self):
        return self.driver.find_element(*HomePage.shopBtnLink)

