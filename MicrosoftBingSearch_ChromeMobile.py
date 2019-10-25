import time
import subprocess
import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse
import os
import platform

print(platform.system())

parser = argparse.ArgumentParser()
parser.add_argument("-driverPath", help="Relative or absolute path to chromedriver.exe. Defaults to included driver at the base.")
parser.add_argument("-numSearches", help="Number of searches to perform. Defaults to 30.")
parser.add_argument("-startNum", help="Number appended to 'test' to start at. Defaults to 0.")

args=parser.parse_args()
chromedriverpath = args.driverPath
number_of_searches = args.numSearches
start_number= args.startNum

if chromedriverpath is None:
    chromedriverpath = os.path.join('drivers', 'chromedriver.exe')
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

if start_number is None:
    start_number = 0
    print("No startNum supplied. Using default of 0.")
else:
    start_number = int(start_number)
    print("Using start_number supplied")
print("Starting with number: " + str(start_number))

#open config.json and get user_data_dir
config_path = os.path.join('config', 'config.json')
with open(config_path) as json_data_file:
    config = json.load(json_data_file)

user_data_dir = config["user.data.dir"]
print("user.data.dir: " + user_data_dir)

#open chrome and get going!
options = webdriver.ChromeOptions() 
#Path to your chrome profile. Needed to use saved bing login session
options.add_argument("user-data-dir=" + user_data_dir)
browser = webdriver.Chrome(chromedriverpath, options=options)

browser.get('http://www.bing.com')
time.sleep(2)

#read config file for ahk install path
ahk_path = config["ahk.path"]
#if ahk path isn't supplied, go the easy route and use the exe's
if (ahk_path is None or ahk_path == ""):
    print("No ahk.path configured, using exe scripts")
    #open devtools
    subprocess.call([os.path.join('ahk_scripts', 'OpenChomeDevTools.exe')])  
    time.sleep(2) #let dev tools open
    #toggle device toolbar to simulate mobile device
    subprocess.call([os.path.join('ahk_scripts', 'ToggleDeviceToolbarChrome.exe')])
    time.sleep(2) #let device load
#if an ahk path is supplied, use it
else: 
    print("ahk.path suppled: " + ahk_path + ", using ahk scripts")
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
    searchbar.send_keys(searchText + str(x + start_number))
    #not using the search button anymore - for some reason in device mode the submit call gets lost
    searchbar.send_keys(Keys.ENTER)
    #wait two second to give search time to load
    time.sleep(2)

browser.close()