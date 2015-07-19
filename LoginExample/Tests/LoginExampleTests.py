'''
Created on Jul 9, 2015

@author: Itai
'''
import unittest
from selenium import webdriver
from Infra.Pages import LoginPage

class LoginExampleTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080")
        self.driver.maximize_window()

    def testRegisterUser(self):
        login = LoginPage(self.driver)
        login.send_keys_to_login_tb("admin")
        registerPage = login.click_on_register_lnk_and_go_to_register_page()
        registerPage.type_to_first_name_tb("Itai")
        registerPage.type_to_last_name_tb("Agmon")
        pass
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
