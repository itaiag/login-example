'''
Created on Jul 9, 2015

@author: Itai
'''


from infra.actionbot import Locator

from infra.base_page import BasePageObject

import tests.marks as m

class LoginPage(BasePageObject):
    '''
    classdocs
    '''

    _USERNAME_TB_BY = Locator.id("username")
    _PASSWORD_TB_BY = Locator.id("password")
    _REGISTER_LNK_BY = Locator.link_text("Register")
    _LOGIN_BTN_BY = Locator.css_selector("div.form-actions > button")
        
    @m.step("In login page")
    def __init__(self, driver):
        '''
        Construbdctor
        '''
        super(LoginPage, self).__init__(driver)
        self.bot.wait_for_element_by(Locator.xpath("//h2[text()='Login']"))
        
    @m.step
    def type_to_username_tb(self, username):
        self.bot.send_keys_to_element_by(self._USERNAME_TB_BY, username)
    
    @m.step
    def type_to_password_tb(self, password):
        self.bot.send_keys_to_element_by(self._PASSWORD_TB_BY, password)
        
    @m.step
    def click_on_login_btn_and_go_to_dashboard_page(self):
        self.bot.click_on_element_by(self._LOGIN_BTN_BY)
        return DashboardPage(self.driver)
    
    @m.step
    def click_on_login_btn_and_stay_in_login_page(self):
        self.bot.click_on_element_by(self._LOGIN_BTN_BY)
        # We want to make sure that we are still in the login page.
        return LoginPage(self.driver)

    @m.step
    def click_on_register_lnk_and_go_to_register_page(self):
        self.bot.click_on_element_by(self._REGISTER_LNK_BY)
        return RegisterPage(self.driver)
    
    @m.step
    def do_login_and_got_to_dashboard_page(self,username,password):
        self.type_to_username_tb(username)
        self.type_to_password_tb(password)
        return self.click_on_login_btn_and_go_to_dashboard_page()
    

class RegisterPage(BasePageObject):
    
    _FIRST_NAME_TB_BY = Locator.id("firstName")
    _LAST_NAME_TB_BY = Locator.name("lastName")
    _USERNAME_TB_BY = Locator.id("username")
    _PASSWORD_TB_BY = Locator.id("password")
    _REGISTER_BTN_BY = Locator.css_selector("div.form-actions > button")
    
    @m.step("In register page")
    def __init__(self, driver): 
        super(RegisterPage, self).__init__(driver)
        self.bot.wait_for_element_by(Locator.xpath("//h2[text()='Register']"))
        
    @m.step
    def type_to_first_name_tb(self, firstName):
        self.bot.send_keys_to_element_by(self._FIRST_NAME_TB_BY, firstName)
 
    @m.step
    def type_to_last_name_tb(self, lastName):
        self.bot.send_keys_to_element_by(self._LAST_NAME_TB_BY, lastName)
    
    @m.step
    def type_to_username_tb(self, username):
        self.bot.send_keys_to_element_by(self._USERNAME_TB_BY, username)
        
    @m.step
    def type_to_password_tb(self, password):
        self.bot.send_keys_to_element_by(self._PASSWORD_TB_BY, password)
    
    @m.step
    def click_on_register_btn_and_go_to_login_page(self):
        self.bot.click_on_element_by(self._REGISTER_BTN_BY)
        return LoginPage(self.driver)
    
    @m.step
    def do_register_and_go_to_login_page(self, firstname, lastname,username,password):
        self.type_to_first_name_tb(firstname)
        self.type_to_last_name_tb(lastname)
        self.type_to_username_tb(username)
        self.type_to_password_tb(password)
        return self.click_on_register_btn_and_go_to_login_page()
        
class DashboardPage(BasePageObject):
    
    _LOGOUT_LNK = Locator.css_selector(".btn-primary")
    
    @m.step("In dash board page")
    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)
        self.bot.wait_for_element_by(Locator.xpath("//h1[contains(.,'Hi')]"))
        
    @m.step
    def click_on_delete_user_lnk(self, user_name):
        self.bot.click_on_element_by(Locator.xpath("//li[contains(.,'{0}')]/a".format(user_name)))
    
    @m.step
    def click_on_logout_btn_and_go_to_login_page(self):
        self.bot.click_on_element_by(self._LOGOUT_LNK)
        return LoginPage(self.driver)
        
