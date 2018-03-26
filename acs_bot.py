import time
from selenium import webdriver

#open csv
#get zip code

#create webdriver
driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")

#navigate to webpage
driver.get('https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml')
time.sleep(1)

#enter zip code
searchBox = driver.find_element_by_id('cfsearchtextboxmain')
goButton = driver.find_element_by_class_name('autoCompleteGoButton')
searchBox.send_keys(zipCode)
goButton.click()
time.sleep(3)

#get ACS Demos
ACShousingdemos = driver.find_element_by_partial_link_text('Demographic and Housing Estimates')
ACShousingdemos.click()
time.sleep(3)

#total population
totalPopulation = driver.find_element_by_xpath("//*[@id='data']/tbody/tr[2]/td[1]")
totalPopulation = totalPopulation.get_attribute('innerHTML')
print(totalPopulation)

#go back
driver.execute_script("window.history.go(-1)")

#go to Housing Stats
housingNav = driver.find_element_by_xpath(//*[@id="leftnav"]/a[6])
housingNav.click()

##driver.quit()
