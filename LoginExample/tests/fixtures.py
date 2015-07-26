'''

@author: agmon
'''
import pytest
from infra.webdriver_factory import get_driver

url = "http://localhost:8080"

@pytest.fixture
def driver(request):
    driver = get_driver("firefox")
    driver.get(url)

    def fin():
        print ("finalizing")
        driver.quit()
    request.addfinalizer(fin)
    return driver