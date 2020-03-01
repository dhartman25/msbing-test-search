import argparse
import os

class ParseArgs:

    def __init__(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("-driverPath", help="Relative or absolute path to chromedriver.exe. Defaults to included driver at the base.")
        parser.add_argument("-numSearches", help="Number of searches to perform. Defaults to 30.")
        parser.add_argument("-startNum", help="Number appended to 'test' to start at. Defaults to 0.")

        args = parser.parse_args()
        self.driverPath = args.driverPath
        self.numSearches = args.numSearches
        self.startNum = args.startNum

    def getChromeDriverPath(self):
        chromedriverpath = ""
        if self.driverPath is None:
            chromedriverpath = os.path.join('drivers', 'chromedriver.exe')
            print("No driverPath supplied. Using default driver packaged.")
        else:
            chromedriverpath = self.driverPath
            print("Using driverPath supplied")
        print("chromedriverpath Path: " + chromedriverpath)
        return chromedriverpath

    def getMSWebDriverPath(self):        
        mswebdriverpath = ""
        if self.driverPath is None:
            mswebdriverpath = "C:\\Windows\\SysWOW64\\MicrosoftWebDriver.exe"
            print("No driverPath supplied. Using default Windows driver.")
        else:
            mswebdriverpath = self.driverPath
            print("Using driverPath supplied")
        print("MicrosoftWebDriver Path: " + mswebdriverpath)
        return mswebdriverpath

    def getNumSearches(self): 
        number_of_searches = 0
        if self.numSearches is None:
            number_of_searches = 30
            print("No numSearches supplied. Using default of 30.")
        else:
            number_of_searches = int(self.numSearches)
            print("Using numSearches supplied")
        print("Number of Searches: " + str(number_of_searches))
        return number_of_searches

    def getStartNum(self):
        start_number = 0
        if self.startNum is None:
            start_number = 0
            print("No startNum supplied. Using default of 0.")
        else:
            start_number = int(self.startNum)
            print("Using start_number supplied")
        print("Starting with number: " + str(start_number))
        return start_number


