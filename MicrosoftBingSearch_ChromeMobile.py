from genericpath import isdir
import time
import subprocess
import json
from selenium import webdriver
import os
import platform
from ParseArgsUtil import ParseArgs
import SearchUtil
import shutil
import socket
from appscript import app
from appscript import k


parentOS = platform.system()
print("Operating System: " + parentOS)

parseargs = ParseArgs()

chromedriverpath = parseargs.getChromeDriverPath()
number_of_searches = parseargs.getNumSearches()
start_number = parseargs.getStartNum()
use_mobile = parseargs.getUseMobile()

#open config.json and get user_data_dir
config_path = os.path.join('config', 'config-' + socket.gethostname() + '.json')
with open(config_path) as json_data_file:
    config = json.load(json_data_file)

user_data_dir = config["user.data.dir"]
print("user.data.dir: " + user_data_dir)
user_data_dir_temp = user_data_dir + "_tmp"

#do a little pre-cleanup if things didn't shut down properly last time
if (os.path.isdir(user_data_dir_temp)):
    print("Cleaning up tmp data dir")
    shutil.rmtree(user_data_dir_temp, ignore_errors=True, onerror=None)

#copy the user data dir to a temp location, otherwise the next run will encounter locks
shutil.copytree(user_data_dir, user_data_dir_temp)

#open chrome and get going!
options = webdriver.ChromeOptions() 
#Path to your chrome profile. Needed to use saved bing login session
options.add_argument("user-data-dir=" + user_data_dir_temp)
browser = webdriver.Chrome(chromedriverpath, options=options)

browser.get('http://www.bing.com')
time.sleep(2)

if (use_mobile):
    #read config file for ahk install path
    ahk_path = config["ahk.path"]
    #if ahk path isn't supplied, use what the tool comes with
    if (ahk_path is None or ahk_path == ""):
        print("No ahk.path configured, using built in scripts")

        if (parentOS == "Windows"):
            #open devtools
            subprocess.call([os.path.join('ahk_scripts', 'OpenChromeDevTools.exe')])  
            time.sleep(2) #let dev tools open
            #toggle device toolbar to simulate mobile device
            subprocess.call([os.path.join('ahk_scripts', 'ToggleDeviceToolbarChrome.exe')])

        elif (parentOS == "Darwin"):
            #open devtools
            #hit cmd + option + i
            #k is a subpackage of appscript
            app('System Events').keystroke('i', using=[k.command_down, k.option_down])
            time.sleep(2) #let dev tools open
            app('System Events').keystroke('m', using=[k.command_down, k.shift_down])

        else: 
            print ("Whoops, don't have a solution for your OS!")

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

#cleanup - delete the tmp user data dir so that we can start again next run
shutil.rmtree(user_data_dir_temp, ignore_errors=True, onerror=None)