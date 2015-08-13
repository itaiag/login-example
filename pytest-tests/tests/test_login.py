
'''
Created on Jul 9, 2015

Suite that tests the various login possibilities which
most of them should result as unsuccessful login

@author: Itai
'''

from infra.pages import LoginPage
from tests.fixtures import *
import tests.marks as m

# Marks the whole tests in the module as 'web' tests
pytestmark = [m.web, m.itai, m.login, m.regressions]


def test_login_with_wrong_user_name(driver):
    with m.step("Step 1 - Performing log in with wrong user"):
        login = LoginPage(driver)
        login.type_to_username_tb("WrongUser")
        login.type_to_password_tb("Wrong password")
        login.click_on_login_btn_and_stay_in_login_page()
        text = login.get_alert_msg_text()
        assert text == "Username or password is incorrect"


@m.fail
def test_that_fails_with_error(driver):
    with m.step("Step 1 - Doing some operations and then fails"):
        login = LoginPage(driver)
        login.type_to_username_tb("WrongUser")
        login.type_to_password_tb("Wrong password")
        login.click_on_login_btn_and_stay_in_login_page()
        login.do_failure()


@m.fail
def test_that_fails_with_failure(driver):
    with m.step("Step 1 - Performing log in with wrong user"):
        login = LoginPage(driver)
        login.type_to_username_tb("WrongUser")
        login.type_to_password_tb("Wrong password")
        login.click_on_login_btn_and_stay_in_login_page()
        text = login.get_alert_msg_text()
        assert text == "Some silly message"
