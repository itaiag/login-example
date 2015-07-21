from selenium import webdriver
'''

@author: agmon
'''

def get_driver(driver):
    if driver=="firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver