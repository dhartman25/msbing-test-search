import time
import subprocess
import configparser
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-driverPath", help="Relative or absolute path to chromedriver.exe. Defaults to included driver at the base.")
parser.add_argument("-numSearches", help="Number of searches to perform. Defaults to 30.")

args=parser.parse_args()
chromedriverpath = args.driverPath
number_of_searches = args.numSearches

if chromedriverpath is None:
    chromedriverpath = "drivers\\chromedriver.exe"
    print("No driverPath supplied. Using default driver packaged.")
else:
    print("Using driverPath supplied")
print("chromedriverpath Path: " + chromedriverpath)
    
    
if number_of_searches is None:
    number_of_searches = 30
    print("No numSearches supplied. Using default of 30.")
else:
    number_of_searches = int(number_of_searches)
    print("Using numSearches supplied")
print("Number of Searches: " + str(number_of_searches))


#get config values for chrome user data dir and ahk path
config = configparser.ConfigParser()
config.read("config\\config.ini")
default = config["DEFAULT"]

user_data_dir = default.get("user.data.dir")
print("user.data.dir: " + user_data_dir)

ahk_path = default.get("ahk.path")
print("ahk.path: " + ahk_path)


#open chrome and get going!
options = webdriver.ChromeOptions() 
#Path to your chrome profile. Needed to use saved bing login session
options.add_argument("user-data-dir=" + user_data_dir)
browser = webdriver.Chrome(chromedriverpath, options=options)

browser.get('http://www.bing.com');
time.sleep(2)

#open devtools
subprocess.call([ahk_path,"ahk_scripts\\OpenChomeDevTools.ahk"])  
time.sleep(2) #let dev tools open
#toggle device toolbar to simulate mobile device
subprocess.call([ahk_path,"ahk_scripts\\ToggleDeviceToolbarChrome.ahk"])
time.sleep(2) #let device load
browser.refresh()
time.sleep(2)

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
    searchbar.clear()
    searchbar.send_keys(searchText + str(x))
    #not using the search button anymore - for some reason in device mode the submit call gets lost
    searchbar.send_keys(Keys.ENTER);
    #wait two second to give search time to load
    time.sleep(2)

browser.close()