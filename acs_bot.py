import time
from selenium import webdriver


zipCode = "96817"
driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver.get('https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml')
time.sleep(1)
searchBox = driver.find_element_by_id('cfsearchtextboxmain')
goButton = driver.find_element_by_class_name('autoCompleteGoButton')
searchBox.send_keys(zipCode)
goButton.click()
time.sleep(3)
ACShousingdemos = driver.find_element_by_partial_link_text('Demographic and Housing Estimates')
ACShousingdemos.click()
time.sleep(3)
totalPopulation = driver.find_element_by_xpath("//*[@id='data']/tbody/tr[2]/td[1]")
totalPopulation = totalPopulation.get_attribute('innerHTML')
print(totalPopulation)

##driver.quit()
