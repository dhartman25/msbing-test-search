from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import json
import os
import time
import platform
from ParseArgsUtil import ParseArgs
import SearchUtil
import socket
from msedge.selenium_tools import EdgeOptions, Edge

print("Operating System: " + platform.system())

parseargs = ParseArgs()

mswebdriverpath = parseargs.getMSWebDriverPath()
number_of_searches = parseargs.getNumSearches()
start_number= parseargs.getStartNum()

#open config.json and get user_data_dir
config_path = os.path.join('config', 'config-' + socket.gethostname() + '.json')
with open(config_path) as json_data_file:
    config = json.load(json_data_file)

user_data_dir = config["user.data.dir.edge"]
print("user.data.dir.edge: " + user_data_dir)

#open edge and get going!
desired_cap = {
    "args":["userDataDir=/tmp/temp_profile"],
    "userDataDir": "/tmp/temp_profile"
}

browser = Edge(executable_path=mswebdriverpath, capabilities=desired_cap)

#go to Bing
browser.get("http://www.bing.com")

searchText = "test"

SearchUtil.runSearches(browser,searchText, number_of_searches, start_number)

browser.close()



