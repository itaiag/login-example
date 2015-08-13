
'''

@author: agmon
'''
import sys

class StdoutReporter:
    def init(self):
        print "Init stdout reporter"
    
    def report(self, title, message):
        if message is not None:
            print title + " " + message
        elif title is not None:
            print title
        
            
    
    def step(self, title):
        if title is not None:
            print "***" + title + "****"
    
    

reporters = []

def init():
    global reporters
    print "Initializing reporters"
    reporters = [StdoutReporter()]
    for reporter in reporters:
        try:
            reporter.init()
        except:
            print "Unexpected error:", sys.exc_info()[0]

def report(title, message = None):
    for reporter in reporters:
        try:
            reporter.report(title, message)
        except:
            print "Unexpected error:", sys.exc_info()[0]

def step(title):
    for reporter in reporters:
        try:
            reporter.step(title)
        except:
            print "Unexpected error:", sys.exc_info()[0]


init()

    
