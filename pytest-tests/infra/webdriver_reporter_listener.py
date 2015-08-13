# @PydevCodeAnalysisIgnore
'''
Created on Aug 1, 2015

@author: Itai
'''
import pytest
from allure.constants import AttachmentType

from selenium.webdriver.support.abstract_event_listener\
    import AbstractEventListener


class WebdriverReporterListener(AbstractEventListener):

    @pytest.allure.step("About to find element with\
        locator '{1}'' and value '{2}'")
    def before_find(self, by, value, driver):
        stam = "Just because I need a body"

    def on_exception(self, exception, driver):
        pytest.allure.attach(
            "Failure screenshot", driver.get_screenshot_as_png(),
            type=AttachmentType.PNG)
