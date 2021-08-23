from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\P0022990\Desktop\Personal\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
homeBtn = driver.find_element_by_link_text("Home")
homeLinks = driver.find_elements_by_xpath("//ul[@class='navbar-nav']/li")
for i in homeLinks:
    print(i.text)
driver.quit()