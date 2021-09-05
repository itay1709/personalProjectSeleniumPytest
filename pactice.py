import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//label[text()='Name']")))
shopBtn = driver.find_element_by_link_text("Shop")
shopBtn.click()
addBtn = driver.find_elements_by_xpath("//div[@class='card-footer']/button")
addBtn[1].click()
checkOutBtn = driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
checkOutBtn.click()
quantity = driver.find_elements_by_id("exampleInputEmail1")
price = driver.find_elements_by_xpath("//tbody/tr[1]/td[3]/strong[1]")
quantity[0].is_selected()
quantity[0].send_keys("2")
checkOutBtnSumPage = driver.find_element_by_xpath("//button[@class='btn btn-success']")
checkOutBtnSumPage.click()
countyInput = driver.find_element_by_id("country")
countyInput.send_keys("fi")
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))
countryResults = driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
for i in countryResults:
    assert "in" or "In" in i.text
    """
        assert "in" in i.text
    elif "In" in i.text:
        assert "In" in i.text
    else:
        print("country doesnt contain 'in'. the text is: " + i.text)
        break


#driver.quit()
"""





