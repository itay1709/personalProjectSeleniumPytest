import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()
homeBtn = driver.find_elements_by_xpath("//h4[@class='card-title']/a")
for i in homeBtn:
    print(i.text)


#driver.quit()






