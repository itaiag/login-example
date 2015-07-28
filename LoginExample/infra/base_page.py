# @PydevCodeAnalysisIgnore
'''
Created on Jul 9, 2015

@author: Itai
'''
from infra.actionbot import ActionBot
from allure.constants import AttachmentType
import pytest

class BasePageObject(object):
    '''
    classdocs
    '''
    

    def __init__(self, driver):
        '''
        Constructor
        '''
        
        self.driver = driver
        self.bot = ActionBot(driver)
        self.add_screenshot(self.__class__.__name__)
        
    def add_screenshot(self, description):
        pytest.allure.attach(description, self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        
