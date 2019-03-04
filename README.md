#MicrosoftBingSearch - Edge/Chrome Mobile Emulator
Includes python/selenium scripts to open a browser at bing.com and execute a configured number of test searches.

##Running MicrosoftBingSearch_Edge
Opens Edge at bing.com executes configured number of searches
1. Install python
2. Ensure python is on your system path (you can open a command prompt and type `python`)
3. Open command prompt and navigate to MicrosoftBingSearch folder
4. Run `python MicrosoftBingSearch_Edge.py`
	optional parameter `-driverPath` used if you have a different version of Windows, necessitating a different version of the driver
	optional parameter `-numSearches` used to execute a custom number of searches. Defaults to 40.

##Running MicrosoftBingSearch_ChromeMobile
Opens Chrome at bing.com, opens devtools, toggles device toolbar to simulate mobile device, execute configured number of searches
1. Install python
2. Ensure python is on your system path (you can open a command prompt and type `python`)
3. Install AutoHotKey
4. Set properties and settings
	-Run `python MicrosoftBingSearch_ChromeMobile.py` and let Chrome open. The script will error, this is ok.
	-Sign into your microsoft account
	-Open a new tab in the Chrome that was opened and go to "chrome://version". Copy the value for "Profile Path"
	-Open config.ini
	-Replace the value for user.data.dir with the value from "Profile Path" (this will let Chrome use previously set settings for device used and bing sign-in)
	-Replace the value for ahk.path with the install path of AutoHotKey
	-Open dev tools, toggle the device toolbar, choose "iPhone 6,7,8" from the dropdown (Chrome will now remember this when you run the script)
	-Close Chrome
5. Run "python MicrosoftBingSearch_ChromeMobile.py"
	optional parameter `-driverPath` used if you need to run a different version of Chrome
	optional parameter `-numSearches` used to execute a custom number of searches. Defaults to 30.

##Troubleshooting
* If MS Edge won't open, you may need a different version of the MicrosoftWebDriver - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
* If issues occur with the supplied Chrome driver, you may need an updated version - http://chromedriver.chromium.org/downloads
* Drivers can either be replaced in the "drivers" folder or the path can be supplied via -driverPath
