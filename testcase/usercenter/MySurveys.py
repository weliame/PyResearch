# -*-coding:utf-8-*-
'''
Created on 2013-4-5

@author: wyq
'''
import unittest
from testcase.common.CommonLogin import CommonLogin

class MySurveys(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_my_surveys(self):
        sel = self.selenium
        #=======================================================================
        # A login user click "My Surveys" menu on the left bar of user_center page
        #=======================================================================
        sel.click('xpath=//div[@class="top_menu"]/a[2]')
        sel.wait_for_page_to_load(5000)
        sel.click('xpath=//div[@class="part_div1_1 main_color2"]/div[3]/a[5]')
        sel.wait_for_page_to_load(5000)
    
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()