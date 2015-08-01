from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from infra.webdriver_reporter_listener import WebdriverReporterListener
'''

@author: agmon
'''

def get_driver(driver):
    if driver=="firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        event_listener_driver = EventFiringWebDriver(driver,WebdriverReporterListener())
        return event_listener_driver