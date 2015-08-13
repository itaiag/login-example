#@PydevCodeAnalysisIgnore
'''
Created on Jul 25, 2015

@author: Itai
'''
import pytest

#People
itai = pytest.mark.itai

#Test types
regressions = pytest.mark.itai
performance = pytest.mark.performance
web = pytest.mark.web
slow = pytest.mark.slow
fast = pytest.mark.fast
dev = pytest.mark.dev
fail = pytest.mark.fail

#Features
login = pytest.mark.login
register = pytest.mark.register

#Allure
step = pytest.allure.step
