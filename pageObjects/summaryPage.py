from selenium.webdriver.common.by import By


class SummaryPage:

    #constructor:
    def __init__(self, driver):
        self.driver = driver


    #test data:
    tableHeadTxt = ['Product', 'Quantity', 'Price', 'Total', ' ']


    #locators:
    tableHead = (By.XPATH, "//table/thead/tr/th")
    tableDeviceName = (By.XPATH, "//div[@class='media-body']/h4/a")
    tableSupplierName = (By.XPATH, "//div[@class='media-body']/h5/a")
    tableStockStatus = (By.XPATH, "//div[@class='media-body']/span/strong")
    tableTotal = (By.XPATH, "//h3[text()='Total']")
    tableAmount = (By.XPATH, "//td[@class='text-right']/h3/strong")
    continueShoppingBtn = (By.XPATH, "//button[@class='btn btn-default']")
    checkOutBtn = (By.XPATH, "//button[@class='btn btn-success']")


    #elements:
    def tableHeadE(self):
        return self.driver.find_elements(*SummaryPage.tableHead)

    def tableDeviceNameE(self):
        return self.driver.find_elements(*SummaryPage.tableDeviceName)

    def tableSupplierNameE(self):
        return self.driver.find_elements(*SummaryPage.tableSupplierName)

    def tableTotalE(self):
        return self.driver.find_element(*SummaryPage.tableTotal)

    def tableAmountE(self):
        return self.driver.find_element(*SummaryPage.tableAmount)

    def continueShoppingBtnE(self):
        return self.driver.find_element(*SummaryPage.continueShoppingBtn)

    def checkOutBtnE(self):
        return self.driver.find_element(*SummaryPage.checkOutBtn)
