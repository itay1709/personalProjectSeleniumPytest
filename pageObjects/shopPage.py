from selenium.webdriver.common.by import By


class ShopPage:

    # contructor:
    def __init__(self, driver):
        self.driver = driver

    #locators
    checkOutBtn = (By.XPATH, "//li[@class='nav-item active']")
