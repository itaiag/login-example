'''
Created on Jul 9, 2015

@author: Itai
'''

from Infra.Pages import LoginPage
from Tests.WebFixture import driver

def test_register_user(driver):
    login = LoginPage(driver)
    register = login.click_on_register_lnk_and_go_to_register_page()
    register.type_to_first_name_tb("Itai")
    register.type_to_last_name_tb("Agmon")
    register.type_to_username_tb("Itai")
    register.type_to_password_tb("12345")
    login = register.click_on_register_btn_and_go_to_login_page()
    login.type_to_username_tb("Itai")
    login.type_to_password_tb("12345")
    login.click_on_login_btb_and_go_to_dashboard_page()
  
