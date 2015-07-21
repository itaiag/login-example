
from Infra.WebdriverFactory import get_driver
from Infra.Pages import LoginPage

global url 
url = "http://localhost:8080"


def _init_driver():
    global driver  
    global url      
    driver = get_driver("firefox")
    driver.get(url)
    return driver
        
def get_login_page():
    global driver
    _init_driver()
    return LoginPage(driver)

def quit_driver():
    global driver
    driver.quit()

