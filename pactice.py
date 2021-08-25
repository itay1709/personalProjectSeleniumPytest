import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
homeBtn = driver.find_element_by_link_text("Home")
homeBtn.is_displayed()
homeLinks = driver.find_elements_by_xpath("//ul[@class='navbar-nav']/li")
btn = driver.find_element_by_xpath("//input[@value='Submit']")
btn.click()
time.sleep(3)
cb = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']")
assert "Success! The Form has been submitted successfully!" in cb.text

#driver.quit()





#ddt with pytest add form

