'''
Created on Jul 9, 2015

@author: Itai
'''

from Infra.Pages import LoginPage
from Tests.WebFixture import driver  # @UnusedImport
import Tests.marks as m

# Marks the whole tests in the module as 'web' tests
pytestmark = [m.web, m.itai, m.login]


# Varaibles
FIRST_NAME = "Itai"
LAST_NAME = "Agmon"
USER_NAME = "itaiag"
PASSWORD = "s3cret"

@m.slow
def test_register_user(driver):
    login = LoginPage(driver)
    register = login.click_on_register_lnk_and_go_to_register_page()
    register.type_to_first_name_tb(FIRST_NAME)
    register.type_to_last_name_tb(LAST_NAME)
    register.type_to_username_tb(USER_NAME)
    register.type_to_password_tb(PASSWORD)
    login = register.click_on_register_btn_and_go_to_login_page()
    login.type_to_username_tb(USER_NAME)
    login.type_to_password_tb(PASSWORD)
    dashboard = login.click_on_login_btn_and_go_to_dashboard_page()
    dashboard.click_on_delete_user_lnk(USER_NAME)
    dashboard.click_on_logout_btn_and_go_to_login_page()

@m.fast
def test_login_with_wrong_user_name(driver):
    login = LoginPage(driver)
    login.type_to_username_tb("WrongUser")
    login.type_to_password_tb("Wrong password")
    login.click_on_login_btn_and_stay_in_login_page()
    
