import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def runSearches(browser,searchText, number_of_searches, start_number):
    for x in range(0, number_of_searches):
        try:
            WebDriverWait(browser, 10).until(
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