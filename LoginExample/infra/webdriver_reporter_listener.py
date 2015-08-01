# @PydevCodeAnalysisIgnore
'''
Created on Aug 1, 2015

@author: Itai
'''
import pytest
import tests.marks as m
from allure.constants import AttachmentType

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

class WebdriverReporterListener(AbstractEventListener):
    
    def before_find(self, by, value, driver):
        with pytest.allure.step("About to find element by:'{0}' value:'{1}'".format(by, value)):
            # I really interested here only on the step message. But since I have to put here something
            # I do this...
            a = 1
    
    def on_exception(self, exception, driver):
        pytest.allure.attach("Failure screenshot", driver.get_screenshot_as_png(), type=AttachmentType.PNG)
