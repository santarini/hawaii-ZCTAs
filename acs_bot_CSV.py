import time
import csv
from selenium import webdriver

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

with open("hawaii_zcta.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    with open('HawaiiZipData.csv', 'a') as csvfileB:
        fieldnames = ['Zip Code', 'Land Area', 'Water Area', 'Population','Square Meter per Person','Total Men','Percent Men','Total Women','Percent Women','Total Native Hawaiians','Percent Native Hawaiian','Median Age','Total Households','Square Meter per Household', 'Total Vacant','Vacancy Rate', 'Total Occupied','Occupancy Rate','Total Renter Occupied','Renter Occupancy Rate', 'Total Owner Occupied','Owner Occupancy Rate', 'Value: Less than $50,000', 'Value: $50,000 to $99,999', 'Value: $100,000 to $149,999', 'Value: $150,000 to $199,999', 'Value: $200,000 to $299,999', 'Value: $300,000 to $499,999', 'Value: $500,000 to $999,999', 'Value: $1,000,000 or more', 'Value: Median (dollars)', 'Total Owner Occupied with Mortgage', 'Total Owner Occupied without Mortgage', 'Monthly Cost with Mortgage:Less than $500', 'Monthly Cost with Mortgage:$500 to $999', 'Monthly Cost with Mortgage:$1,000 to $1,499', 'Monthly Cost with Mortgage:$1,500 to $1,999', 'Monthly Cost with Mortgage:$2,000 to $2,499', 'Monthly Cost with Mortgage:$2,500 to $2,999', 'Monthly Cost with Mortgage:$3,000 or more', 'Monthly Cost with Mortgage:Median (dollars)', 'Monthly Cost without Mortgage:Less than $250', 'Monthly Cost without Mortgage:$250 to $399', 'Monthly Cost without Mortgage:$400 to $599', 'Monthly Cost without Mortgage:$600 to $799', 'Monthly Cost without Mortgage:$800 to $999', 'Monthly Cost without Mortgage:$1,000 or more', 'Monthly Cost without Mortgage:Median (dollars)', 'Gross Rent:Less than $500', 'Gross Rent:$500 to $999', 'Gross Rent:$1,000 to $1,499', 'Gross Rent:$1,500 to $1,999', 'Gross Rent:$2,000 to $2,499', 'Gross Rent:$2,500 to $2,999', 'Gross Rent:$3,000 or more', 'Gross Rent:Median (dollars)', 
]
        writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()

        for row in reader:
            zipCode = (row['Zip'])
            landArea = (row['2010 Census land area (square meters)'])
            waterArea = (row['2010 Census water area (square meters)'])
            
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
            totalPopulation = totalPopulation.replace(',','')
            print("Total Population: " + totalPopulation)

            #squaremeter/person
            sqmtrPerPerson = int(landArea)/int(totalPopulation)
            print(sqmtrPerPerson)

            #total men
            totalMen = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[3]/td[1]')
            totalMen = totalMen.get_attribute('innerHTML')
            totalMen = totalMen.replace(',','')
            print("Total Men: " + totalMen)

            #percentMen
            percentMen = int(totalMen)/int(totalPopulation)

            #total women
            totalWomen = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[4]/td[1]')
            totalWomen = totalWomen.get_attribute('innerHTML')
            totalWomen = totalWomen.replace(',','')
            print("Total Women: " + totalWomen)

            #percentWomen
            percentWomen = int(totalWomen)/int(totalPopulation)

            #median age
            medianAge = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[20]/td[1]')
            medianAge = medianAge.get_attribute('innerHTML')
            medianAge = medianAge.replace(',','')
            print("Median Age: " + medianAge)

            #native hawaiians
            nativeHawaiians = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[57]/td[1]')
            nativeHawaiians = nativeHawaiians.get_attribute('innerHTML')
            nativeHawaiians = nativeHawaiians.replace(',','')
            print("Number of Native Hawaiians: " + nativeHawaiians)

            #percentHawaiian
            percentHawaiian = int(nativeHawaiians)/int(totalPopulation)

            #go back
            driver.execute_script("window.history.go(-1)")
            time.sleep(3)

            #go to Housing Stats
            housingNav = driver.find_element_by_xpath('//*[@id="leftnav"]/a[6]')
            housingNav.click()
            time.sleep(1)
            housingCharacteristics = driver.find_element_by_partial_link_text('Selected Housing Characteristics')
            housingCharacteristics.click()
            time.sleep(3)

            #total housing units
            totalHouseholds = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[2]/td[1]')
            totalHouseholds = totalHouseholds.get_attribute('innerHTML')
            totalHouseholds = totalHouseholds.replace(',','')
            print("Number of Households: " + totalHouseholds)

            #squaremeter/household
            sqmtrPerHousehold = int(landArea)/int(totalHouseholds)
            
            #total vacant
            totalVacant = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[4]/td[1]')
            totalVacant = totalVacant.get_attribute('innerHTML')
            totalVacant = totalVacant.replace(',','')
            print("Number of Vacant Households: " + totalVacant)

            #percent vacant
            percentVacant = int(totalVacant)/int(totalHouseholds)

            #total occupied
            totalOccupied = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[3]/td[1]')
            totalOccupied = totalOccupied.get_attribute('innerHTML')
            totalOccupied = totalVacant.replace(',','')
            print("Number of Occupied Households: " + totalOccupied)

            #percent occupied
            percentOccupied = int(totalOccupied)/int(totalHouseholds)

            #total renter occupied
            renterOccupied = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[59]/td[1]')
            renterOccupied = renterOccupied.get_attribute('innerHTML')
            renterOccupied = renterOccupied.replace(',','')
            print("Number of Renter Occupied: " + renterOccupied)

            #percent renter occupied
            percentRenterOccupied = int(renterOccupied)/int(totalOccupied)

            #total owner occupied
            ownerOccupied = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[58]/td[1]')
            ownerOccupied = ownerOccupied.get_attribute('innerHTML')
            ownerOccupied = ownerOccupied.replace(',','')
            print("Number of Owner Occupied: " + ownerOccupied)

            #percent owner occupied
            percentOwnerOccupied = int(ownerOccupied)/int(totalOccupied)

            #owner occupied value
            value1 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[106]/td[1]')
            value2 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[107]/td[1]')
            value3 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[108]/td[1]')
            value4 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[109]/td[1]')
            value5 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[110]/td[1]')
            value6 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[111]/td[1]')
            value7 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[112]/td[1]')
            value8 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[113]/td[1]')
            valueMedian = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[114]/td[1]')
            value1 = value1.get_attribute('innerHTML')
            value2 = value2.get_attribute('innerHTML')
            value3 = value3.get_attribute('innerHTML')
            value4 = value4.get_attribute('innerHTML')
            value5 = value5.get_attribute('innerHTML')
            value6 = value6.get_attribute('innerHTML')
            value7 = value7.get_attribute('innerHTML')
            value8 = value8.get_attribute('innerHTML')
            valueMedian = valueMedian.get_attribute('innerHTML')

            #owner occupied with mortgage
            withMortgage = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[118]/td[1]')
            withMortgage = withMortgage.get_attribute('innerHTML')

            #owner occupied without mortgage
            withoutMortgage = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[119]/td[1]')
            withoutMortgage = withoutMortgage.get_attribute('innerHTML')            

            #owner occupied monthly cost with mortgage
            monthlyCostWithMortgage1 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[123]/td[1]')
            monthlyCostWithMortgage2 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[124]/td[1]')
            monthlyCostWithMortgage3 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[125]/td[1]')
            monthlyCostWithMortgage4 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[126]/td[1]')
            monthlyCostWithMortgage5 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[127]/td[1]')
            monthlyCostWithMortgage6 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[128]/td[1]')
            monthlyCostWithMortgage7 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[129]/td[1]')
            monthlyCostWithMortgageMedian = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[130]/td[1]')

            monthlyCostWithMortgage1 = monthlyCostWithMortgage1.get_attribute('innerHTML')
            monthlyCostWithMortgage2 = monthlyCostWithMortgage2.get_attribute('innerHTML')
            monthlyCostWithMortgage3 = monthlyCostWithMortgage3.get_attribute('innerHTML')
            monthlyCostWithMortgage4 = monthlyCostWithMortgage4.get_attribute('innerHTML')
            monthlyCostWithMortgage5 = monthlyCostWithMortgage5.get_attribute('innerHTML')
            monthlyCostWithMortgage6 = monthlyCostWithMortgage6.get_attribute('innerHTML')
            monthlyCostWithMortgage7 = monthlyCostWithMortgage7.get_attribute('innerHTML')
            monthlyCostWithMortgageMedian = monthlyCostWithMortgageMedian.get_attribute('innerHTML')

            #owner occupied monthly cost without mortgage
            monthlyCostWithoutMortgage1 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[133]/td[1]')
            monthlyCostWithoutMortgage2 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[134]/td[1]')
            monthlyCostWithoutMortgage3 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[135]/td[1]')
            monthlyCostWithoutMortgage4 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[136]/td[1]')
            monthlyCostWithoutMortgage5 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[137]/td[1]')
            monthlyCostWithoutMortgage6 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[138]/td[1]')
            monthlyCostWithoutMortgageMedian = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[139]/td[1]')

            monthlyCostWithoutMortgage1 = monthlyCostWithoutMortgage1.get_attribute('innerHTML')
            monthlyCostWithoutMortgage2 = monthlyCostWithoutMortgage2.get_attribute('innerHTML')
            monthlyCostWithoutMortgage3 = monthlyCostWithoutMortgage3.get_attribute('innerHTML')
            monthlyCostWithoutMortgage4 = monthlyCostWithoutMortgage4.get_attribute('innerHTML')
            monthlyCostWithoutMortgage5 = monthlyCostWithoutMortgage5.get_attribute('innerHTML')
            monthlyCostWithoutMortgage6 = monthlyCostWithoutMortgage6.get_attribute('innerHTML')
            monthlyCostWithoutMortgageMedian = monthlyCostWithoutMortgageMedian.get_attribute('innerHTML')

            #gross rent
            grossRent1 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[164]/td[1]')
            grossRent2 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[165]/td[1]')
            grossRent3 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[166]/td[1]')
            grossRent4 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[167]/td[1]')
            grossRent5 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[168]/td[1]')
            grossRent6 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[169]/td[1]')
            grossRent7 = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[170]/td[1]')
            grossRentMedian = driver.find_element_by_xpath('//*[@id="data"]/tbody/tr[171]/td[1]')

            grossRent1 = grossRent1.get_attribute('innerHTML')
            grossRent2 = grossRent2.get_attribute('innerHTML')
            grossRent3 = grossRent3.get_attribute('innerHTML')
            grossRent4 = grossRent4.get_attribute('innerHTML')
            grossRent5 = grossRent5.get_attribute('innerHTML')
            grossRent6 = grossRent6.get_attribute('innerHTML')
            grossRent7 = grossRent7.get_attribute('innerHTML')
            grossRentMedian = grossRentMedian.get_attribute('innerHTML')

            #go back
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)

            #go to population nav
            populationNav = driver.find_element_by_xpath('//*[@id="leftnav"]/a[1]')
            populationNav.click()
            time.sleep(1)
            

            writer.writerow({'Zip Code': zipCode, 'Land Area': landArea, 'Water Area': waterArea, 'Population': totalPopulation,'Square Meter per Person': sqmtrPerPerson ,'Total Men': totalMen,'Percent Men':percentMen ,'Total Women': totalWomen,'Percent Women':percentWomen,'Total Native Hawaiians': nativeHawaiians,'Percent Native Hawaiian': percentHawaiian,'Median Age':medianAge, 'Total Households': totalHouseholds,'Square Meter per Household': sqmtrPerHousehold, 'Total Vacant': totalVacant,'Vacancy Rate':percentVacant,'Total Occupied': totalOccupied,'Occupancy Rate':percentOccupied,'Total Renter Occupied': renterOccupied,'Renter Occupancy Rate':percentRenterOccupied,'Total Owner Occupied': ownerOccupied,'Owner Occupancy Rate': percentOwnerOccupied,'Value: Less than $50,000': value1,'Value: $50,000 to $99,999': value2,'Value: $100,000 to $149,999': value3,'Value: $150,000 to $199,999': value4,'Value: $200,000 to $299,999': value5,'Value: $300,000 to $499,999': value6,'Value: $500,000 to $999,999': value7,'Value: $1,000,000 or more': value8,'Value: Median (dollars)': valueMedian,'Total Owner Occupied with Mortgage': withMortgage,'Total Owner Occupied without Mortgage': withoutMortgage,'Monthly Cost with Mortgage:Less than $500': monthlyCostWithMortgage1,'Monthly Cost with Mortgage:$500 to $999': monthlyCostWithMortgage2,'Monthly Cost with Mortgage:$1,000 to $1,499': monthlyCostWithMortgage3,'Monthly Cost with Mortgage:$1,500 to $1,999': monthlyCostWithMortgage4,'Monthly Cost with Mortgage:$2,000 to $2,499': monthlyCostWithMortgage5,'Monthly Cost with Mortgage:$2,500 to $2,999': monthlyCostWithMortgage6,'Monthly Cost with Mortgage:$3,000 or more': monthlyCostWithMortgage7,'Monthly Cost with Mortgage:Median (dollars)': monthlyCostWithMortgageMedian,'Monthly Cost without Mortgage:Less than $250': monthlyCostWithoutMortgage1,'Monthly Cost without Mortgage:$250 to $399': monthlyCostWithoutMortgage2,'Monthly Cost without Mortgage:$400 to $599': monthlyCostWithoutMortgage3,'Monthly Cost without Mortgage:$600 to $799': monthlyCostWithoutMortgage4,'Monthly Cost without Mortgage:$800 to $999': monthlyCostWithoutMortgage5,'Monthly Cost without Mortgage:$1,000 or more': monthlyCostWithoutMortgage6,'Monthly Cost without Mortgage:Median (dollars)': monthlyCostWithoutMortgageMedian,'Gross Rent:Less than $500': grossRent1,'Gross Rent:$500 to $999': grossRent2,'Gross Rent:$1,000 to $1,499': grossRent3,'Gross Rent:$1,500 to $1,999': grossRent4,'Gross Rent:$2,000 to $2,499': grossRent5,'Gross Rent:$2,500 to $2,999': grossRent6,'Gross Rent:$3,000 or more': grossRent7,'Gross Rent:Median (dollars)': grossRentMedian,
})

            
        #end loop for all zips in csv

driver.quit()
