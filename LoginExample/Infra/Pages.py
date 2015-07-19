'''
Created on Jul 9, 2015

@author: Itai
'''


from Infra.ActionBot import Locator

from Infra.BasePageObject import BasePageObject

class LoginPage(BasePageObject):
    '''
    classdocs
    '''

    _USER_NAME_BY = Locator.id("username")
    _REGISTER_LNK_BY = Locator.link_text("Register")
        
    def __init__(self, driver):
        '''
        Construbdctor
        '''
        super(LoginPage, self).__init__(driver)
        
    def send_keys_to_login_tb(self, text):
        self.actionBot.send_keys_to_element_by(self._USER_NAME_BY, text, "About to send keys to element username")
        return self
        
    def click_on_register_lnk_and_go_to_register_page(self):
        self.actionBot.click_on_element_by(self._REGISTER_LNK_BY, "About to click on register link")
        return RegisterPage(self.driver)

class RegisterPage(BasePageObject):
    
    _FIRST_NAME_TB_BY = Locator.id("firstName")
    _LAST_NAME_TB_BY = Locator.name("lastName")
    
    def __init__(self, driver): 
        super(RegisterPage, self).__init__(driver)
        
    def type_to_first_name_tb(self, text):
        self.actionBot.send_keys_to_element_by(self._FIRST_NAME_TB_BY, text, "About to send keys to first name tb")
        return self
    
    def type_to_last_name_tb(self, text):
        self.actionBot.send_keys_to_element_by(self._LAST_NAME_TB_BY, text, "About to type to last name tb")
        return self