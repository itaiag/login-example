'''
Created on Jul 9, 2015

@author: Itai
'''
from selenium.webdriver.common.by import By

class ActionBot(object):
    '''
    classdocs
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.driver = driver
    
    def click_on_element_by(self, locator, description):
        print description
        element = self.driver.find_element(locator.by, locator.value)
        element.click()
    
    def send_keys_to_element_by(self, locator, keys, description):
        print description
        element = self.driver.find_element(locator.by, locator.value)
        element.clear()
        element.send_keys(keys)
        
        
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
        return Locator(By.ID, value)
