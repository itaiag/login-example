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

    _USERNAME_TB_BY = Locator.id("username")
    _PASSWORD_TB_BY = Locator.id("password")
    _REGISTER_LNK_BY = Locator.link_text("Register")
    _LOGIN_BTN_BY = Locator.css_selector("div.form-actions > button")
        
    def __init__(self, driver):
        '''
        Construbdctor
        '''
        super(LoginPage, self).__init__(driver)
        self.bot.wait_for_element_by(Locator.xpath("//h2[text()='Login']"), "Waiting for page to load")
        
    def type_to_username_tb(self, username):
        self.bot.send_keys_to_element_by(self._USERNAME_TB_BY, username, "About to type to element username")
    
    def type_to_password_tb(self, password):
        self.bot.send_keys_to_element_by(self._PASSWORD_TB_BY, password, "About to type to password tb")
        
    def click_on_login_btb_and_go_to_dashboard_page(self):
        self.bot.click_on_element_by(self._LOGIN_BTN_BY, "About to click on login button")

    def click_on_register_lnk_and_go_to_register_page(self):
        self.bot.click_on_element_by(self._REGISTER_LNK_BY, "About to click on register link")
        return RegisterPage(self.driver)
    

class RegisterPage(BasePageObject):
    
    _FIRST_NAME_TB_BY = Locator.id("firstName")
    _LAST_NAME_TB_BY = Locator.name("lastName")
    _USERNAME_TB_BY = Locator.id("username")
    _PASSWORD_TB_BY = Locator.id("password")
    _REGISTER_BTN_BY = Locator.css_selector("div.form-actions > button")
    
    
    def __init__(self, driver): 
        super(RegisterPage, self).__init__(driver)
        self.bot.wait_for_element_by(Locator.xpath("//h2[text()='Register']"), "Waiting for page to load")
        
    def type_to_first_name_tb(self, firstName):
        self.bot.send_keys_to_element_by(self._FIRST_NAME_TB_BY, firstName, "About to send keys to first name tb")
    
    def type_to_last_name_tb(self, lastName):
        self.bot.send_keys_to_element_by(self._LAST_NAME_TB_BY, lastName, "About to type to last name tb")
    
    def type_to_username_tb(self, username):
        self.bot.send_keys_to_element_by(self._USERNAME_TB_BY, username, "About to type to username tb")
        
    def type_to_password_tb(self, password):
        self.bot.send_keys_to_element_by(self._PASSWORD_TB_BY, password, "About to type to password tb")
    
    def click_on_register_btn_and_go_to_login_page(self):
        self.bot.click_on_element_by(self._REGISTER_BTN_BY, "About to click on register button")
        return LoginPage(self.driver)
        
