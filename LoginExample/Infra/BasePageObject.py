'''
Created on Jul 9, 2015

@author: Itai
'''
from Infra.ActionBot import ActionBot

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
        