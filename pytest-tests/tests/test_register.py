
'''
Created on Jul 9, 2015

Suite that tests the various ways to regsiter a new user

@author: Itai
'''

from infra.pages import LoginPage
from tests.fixtures import driver  # @UnusedImport
import tests.marks as m

# Marks the whole tests in the module as 'web' tests
pytestmark = [m.web, m.itai, m.register, m.regressions]


# Variables
FIRST_NAME = "Itai"
LAST_NAME = "Agmon"
USER_NAME = "itaiag"
PASSWORD = "s3cret"


@m.slow
@m.dev
def test_register_user(driver):
    with m.step('Step 1 - Registering new user'):
        login = LoginPage(driver)
        register = login.click_on_register_lnk_and_go_to_register_page()
        register.type_to_first_name_tb(FIRST_NAME)
        register.type_to_last_name_tb(LAST_NAME)
        register.type_to_username_tb(USER_NAME)
        register.type_to_password_tb(PASSWORD)
        login = register.click_on_register_btn_and_go_to_login_page()

    with m.step("Step 2 - Performing log in with the new user"):
        login.type_to_username_tb(USER_NAME)
        login.type_to_password_tb(PASSWORD)
        dashboard = login.click_on_login_btn_and_go_to_dashboard_page()

    with m.step("Step 3 - Deleting the new created user"):
        dashboard.click_on_delete_user_lnk(USER_NAME)
        login = dashboard.click_on_logout_btn_and_go_to_login_page()
#         login.do_failure()

@m.slow
def test_register_user_shorter(driver):
    with m.step('Step 1 - Registering new user'):
        login = LoginPage(driver)
        register = login.click_on_register_lnk_and_go_to_register_page()
        login = register.do_register_and_go_to_login_page(FIRST_NAME, LAST_NAME, USER_NAME, PASSWORD)

    with m.step("Step 2 - Performing log in with the new user"):
        dashboard = login.do_login_and_got_to_dashboard_page(USER_NAME, PASSWORD)

    with m.step("Step 3 - Deleting the new created user"):
        dashboard.click_on_delete_user_lnk(USER_NAME)
        dashboard.click_on_logout_btn_and_go_to_login_page()


