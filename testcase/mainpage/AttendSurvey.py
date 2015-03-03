'''
Created on 2013-3-28
Description C:/Users/lenovo/workspace/research/testcase/mainpage/ClickNews.py
@author: wyq
'''
# -*-coding:utf-8-*- 
import unittest
from testcase.common.CommonLogin import CommonLogin
from datetime import datetime
from xml.etree.ElementTree import ElementTree

class AttendSurvey(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_attend_survey(self):
        sel = self.selenium
        sel.click(u"xpath=//div[@class='text main_color1']/dl[1]//a")
        sel.wait_for_page_to_load("5000")
        self.configroot = ElementTree(file='../../conf/conf.xml').getroot()
        screenshotrootpath = self.configroot.find("screenshot/path").text + datetime.now().strftime("%Y%m%d") + '\\mainpage\\'
        screenshotFilename = "attendsurvey_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        sel.capture_screenshot(screenshotrootpath + screenshotFilename)
        
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
