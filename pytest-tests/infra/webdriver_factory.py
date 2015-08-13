from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver\
    import EventFiringWebDriver
from infra.webdriver_reporter_listener import WebdriverReporterListener
'''

@author: agmon
'''


def get_driver(driver):
    if driver == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return EventFiringWebDriver(driver, WebdriverReporterListener())
