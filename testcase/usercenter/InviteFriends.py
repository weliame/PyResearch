# -*-coding:utf-8-*-
'''
Created on 2013-4-5

@author: wyq
'''
import unittest
from testcase.common.CommonLogin import CommonLogin

class InviteFriends(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_Invite_Friends(self):
        sel = self.selenium
        #=======================================================================
        # A login user click "Invite Friends" menu on the left bar of user_center page
        #=======================================================================
        sel.click('xpath=//div[@class="top_menu"]/a[2]')
        sel.wait_for_page_to_load(5000)
        sel.click('xpath=//div[@class="part_div1_1 main_color2"]/div[3]/strong/a')
        sel.wait_for_page_to_load(5000)
    
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()