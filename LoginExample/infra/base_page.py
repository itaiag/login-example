'''
Created on Jul 9, 2015

@author: Itai
'''
from infra import actionbot

class BasePageObject(object):
    '''
    classdocs
    '''
    

    def __init__(self, driver):
        '''
        Constructor
        '''
        
        self.driver = driver
        self.bot = actionbot(driver)
        