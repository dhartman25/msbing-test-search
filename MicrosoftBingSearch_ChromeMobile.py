import time
import subprocess
import json
from selenium import webdriver
import os
import platform
from ParseArgsUtil import ParseArgs
import SearchUtil

print("Operating System: " + platform.system())

parseargs = ParseArgs()

chromedriverpath = parseargs.getChromeDriverPath()
number_of_searches = parseargs.getNumSearches()
start_number= parseargs.getStartNum()

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
    subprocess.call([os.path.join('ahk_scripts', 'OpenChromeDevTools.exe')])  
    time.sleep(2) #let dev tools open
    #toggle device toolbar to simulate mobile device
    subprocess.call([os.path.join('ahk_scripts', 'ToggleDeviceToolbarChrome.exe')])
    time.sleep(2) #let device load
#if an ahk path is supplied, use it
else: 
    print("ahk.path suppled: " + ahk_path + ", using ahk scripts")
    #open devtools
    subprocess.call([ahk_path,"ahk_scripts\\OpenChromeDevTools.ahk"])  
    time.sleep(2) #let dev tools open
    #toggle device toolbar to simulate mobile device
    subprocess.call([ahk_path,"ahk_scripts\\ToggleDeviceToolbarChrome.ahk"])
    time.sleep(2) #let device load

browser.refresh()
time.sleep(2)

searchText = "test"

SearchUtil.runSearches(browser,searchText, number_of_searches, start_number)

browser.close()