# -*-coding:utf-8-*- 
from selenium import selenium
import unittest, re
from xml.etree.ElementTree import ElementTree
from testcase.common.database import Database
from datetime import datetime


class CommonLogin(unittest.TestCase):
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
#        if you want change usernameEmail ,don't forget to modify relative assertion
        self.selenium.type("id=username", "weliam@163.com")
        self.selenium.type("id=password", "abcd1234")
        self.selenium.click("css=input[type=\"submit\"]")
        self.selenium.wait_for_page_to_load("5000")

    def tearDown(self):
        self.selenium.close()
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
#
if __name__ == "__main__":
    unittest.main()
