from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import platform
from ParseArgsUtil import ParseArgs
import SearchUtil

print("Operating System: " + platform.system())

parseargs = ParseArgs()

mswebdriverpath = parseargs.getMSWebDriverPath()
number_of_searches = parseargs.getNumSearches()
start_number= parseargs.getStartNum()

# create new Edge session
browser = webdriver.Edge(mswebdriverpath)

#go to Bing
browser.get("http://www.bing.com")

searchText = "test"

SearchUtil.runSearches(browser,searchText, number_of_searches, start_number)

browser.close()



