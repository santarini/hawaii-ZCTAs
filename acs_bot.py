import time
from selenium import webdriver

#open csv
#get zip code

zipCode = "96817"

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
print("Total Population: " + totalPopulation)

#total men
totalMen = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[3]/td[1]')
totalMen = totalMen.get_attribute('innerHTML')
print("Total Men: " + totalMen)

#total women
totalWomen = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[4]/td[1]')
totalWomen = totalWomen.get_attribute('innerHTML')
print("Total Women: " + totalWomen)

#median age
medianAge = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[20]/td[1]')
medianAge = medianAge.get_attribute('innerHTML')
print("Median Age: " + medianAge)

#native hawaiians
nativeHawaiians = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[57]/td[1]')
nativeHawaiians = nativeHawaiians.get_attribute('innerHTML')
print("Number of Native Hawaiians: " + nativeHawaiians)

#go back
driver.execute_script("window.history.go(-1)")
time.sleep(1)

#go to Housing Stats
housingNav = driver.find_element_by_xpath('//*[@id="leftnav"]/a[6]')
housingNav.click()
housingCharacteristics = driver.find_element_by_partial_link_text('Selected Housing Characteristics')
housingCharacteristics.click()
time.sleep(3)

##driver.quit()
