from selenium.webdriver.common.by import By


class ShopPage:

    # contructor:
    def __init__(self, driver):
        self.driver = driver

    #test data
    devices = ["iphone X", "Samsung Note 8", "Nokia Edge", "Blackberry"]
    categoriesSideMenu = ['Category 1', 'Category 2', 'Category 3']

    #locators:
    checkOutBtn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    shopHeadline = (By.XPATH, "//h1[@class='my-4']")
    categories = (By.XPATH, "//div[@class='list-group']/a")
    cardDevicesName = (By.XPATH, "//h4[@class='card-title']/a")
    cardDevicesPrice = (By.XPATH, "//div[@class='card-body']/h5")
    cardDevicesDesc = (By.XPATH, "//div[@class='card-body']/p")
    cardDevicesAddBtn = (By.XPATH, "//div[@class='card-footer']/button")

    #elements:
    def checkOutBtnE(self):
        return self.driver.find_element(*ShopPage.checkOutBtn)

    def shopHeadlineE(self):
        return self.driver.find_element(*ShopPage.shopHeadline)

    def categoriesE(self):
        return self.driver.find_elements(*ShopPage.categories)

    def cardDevicesNameE(self):
        return self.driver.find_elements(*ShopPage.cardDevicesName)

    def cardDevicesPriceE(self):
        return self.driver.find_elements(*ShopPage.cardDevicesPrice)

    def cardDevicesDescE(self):
        return self.driver.find_elements(*ShopPage.cardDevicesDesc)

    def cardDevicesAddBtnE(self):
        return self.driver.find_elements(*ShopPage.cardDevicesAddBtn)





#  validate add button



