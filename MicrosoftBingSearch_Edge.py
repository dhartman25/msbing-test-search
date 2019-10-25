from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-driverPath", help="Relative or absolute path to MicrosoftWebDriver.exe. Defaults to included driver at the base.")
parser.add_argument("-numSearches", help="Number of searches to perform. Defaults to 40.")
parser.add_argument("-startNum", help="Number appended to 'test' to start at. Defaults to 0.")

args=parser.parse_args()
mswebdriverpath = args.driverPath
number_of_searches = args.numSearches
start_number= args.startNum

if mswebdriverpath is None:
    mswebdriverpath = "C:\\Windows\\SysWOW64\\MicrosoftWebDriver.exe"
    print("No driverPath supplied. Using default Windows driver.")
else:
    print("Using driverPath supplied")
print("MicrosoftWebDriver Path: " + mswebdriverpath)
    
    
if number_of_searches is None:
    number_of_searches = 40
    print("No numSearches supplied. Using default of 40.")
else:
    number_of_searches = int(number_of_searches)
    print("Using numSearches supplied")
print("Number of Searches: " + str(number_of_searches))

if start_number is None:
    start_number = 0
    print("No startNum supplied. Using default of 0.")
else:
    start_number = int(start_number)
    print("Using start_number supplied")
print("Starting with number: " + str(start_number))

# create new Edge session
browser = webdriver.Edge(mswebdriverpath)

#go to Bing
browser.get("http://www.bing.com")

searchText = "test"

for x in range(0, number_of_searches):
    try:
        element = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "sb_form_q"))
        )
    except:
        #if something happened, just close the browser
        browser.close()
    searchbar = browser.find_element_by_id("sb_form_q")
    searchbutton = browser.find_element_by_id("sb_form_go")
    searchbar.clear()
    searchbar.send_keys(searchText + str(x + start_number))
    searchbutton.click()
    #wait two second to give search time to load
    time.sleep(2)

browser.close()



