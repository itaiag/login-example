'''
Created on Jul 9, 2015

@author: Itai
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class ActionBot(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver

    @pytest.allure.step("Click on element with locator '{1}'")
    def click_on_element_by(self, locator):
        element = self.driver.find_element(locator.by, locator.value)
        element.click()

    @pytest.allure.step("Send keys to element with locator '{1}'")
    def send_keys_to_element_by(self, locator, keys):
        element = self.driver.find_element(locator.by, locator.value)
        element.clear()
        element.send_keys(keys)

    @pytest.allure.step("Wait for element with locator '{1}'")
    def wait_for_element_by(self,locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((locator.by, locator.value)))



class Locator(object):


    def __init__(self, by, value):
        self.by = by
        self.value = value

    @classmethod
    def id(Locator,value):
        return Locator(By.ID, value)

    @classmethod
    def name(Locator,value):
        return Locator(By.NAME, value)

    @classmethod
    def link_text(Locator,value):
        return Locator(By.LINK_TEXT, value)

    @classmethod
    def css_selector(Locator,value):
        return Locator(By.CSS_SELECTOR, value)

    @classmethod
    def xpath(Locator,value):
        return Locator(By.XPATH, value)
    
    def __str__(self, *args, **kwargs):
        return "{0}:{1}".format(self.by, self.value)
    
