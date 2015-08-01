
'''
Created on Jul 9, 2015

@author: Itai
'''

from infra.pages import LoginPage
from tests.fixtures import driver  # @UnusedImport
import tests.marks as m

# Marks the whole tests in the module as 'web' tests
pytestmark = [m.web, m.itai, m.login]


@m.fast
def test_login_with_wrong_user_name(driver):
    with m.step("Step 1 - Performing log in with wrong user"):
        login = LoginPage(driver)
        login.type_to_username_tb("WrongUser")
        login.type_to_password_tb("Wrong password")
        login.click_on_login_btn_and_stay_in_login_page()
