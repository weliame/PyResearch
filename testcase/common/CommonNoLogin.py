#-*-coding:utf-8-*-
'''
Created on 2013-4-5

@author: wyq
'''

from selenium import selenium
import unittest,time
from xml.etree.ElementTree import ElementTree

class CommonNoLogin(unittest.TestCase):
    
    
    
    def test(self,a):
        self.a = a;
        
    def add(self,other):
        return CommonNoLogin().test(self.a+other.a);
    
    def setUp(self):
        """
        setUp method will create a selenium connection to the selenium driver.All parameters here are read from conf.xml
        """
        self.verificationErrors = []
        self.configfile = ElementTree(file='..\..\conf\conf.xml').getroot()
        self.weburl = self.configfile.find("weburl/url").text
        self.seleserver = self.configfile.find('seleniumserver/server').text
        self.seleport = self.configfile.find('seleniumserver/port').text
        self.browsername = self.configfile.find('browser/name').text
        self.selenium = selenium(self.seleserver, self.seleport, self.browsername, self.weburl)
        self.selenium.start()
        self.selenium.window_maximize()
        self.selenium.open("/")
        self.selenium.wait_for_page_to_load("5000") 
        self.username = self.configfile.find('userdata/username').text
        self.password = self.configfile.find('userdata/password').text
        

    def tearDown(self):
        self.selenium.close()
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
#
if __name__ == "__main__":
    unittest.main()       