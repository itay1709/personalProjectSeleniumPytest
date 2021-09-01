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
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//label[text()='Name']")))
shopBtn = driver.find_element_by_link_text("Shop")
shopBtn.click()
addBtn = driver.find_elements_by_xpath("//div[@class='card-footer']/button")
addBtn[1].click()
checkOutBtn = driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']")
checkOutBtn.click()
quantity = driver.find_elements_by_id("exampleInputEmail1")
for i in quantity:
    print(i.get_attribute("value"))
#homeBtn = driver.find_elements_by_xpath("//div[@class='list-group']/a")
#tableHead = driver.find_elements_by_xpath("//table/thead/tr/th")

#extableHead = []
#for i in tableHead:
#    extableHead.append(i.text)
#print(extableHead)


#driver.quit()






