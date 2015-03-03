# -*-coding:utf-8-*-
'''
Created on 2013-4-5

@author: wyq
'''
from testcase.common.CommonNoLogin import CommonNoLogin
import unittest

class NoLoginUserCenter(CommonNoLogin):
    def setUp(self):
        CommonNoLogin.setUp(self)
    
    def test_no_login_user_center(self):
        sel = self.selenium
        #=======================================================================
        # A nologin user click the user_center menu,login into system,then show "My Mainpage"
        #=======================================================================
        sel.click('xpath=//div[@class="top_menu"]/a[2]')
        sel.wait_for_page_to_load(5000)
        sel.type('xpath=//div[1]/input[@id="username"]', self.username)
        sel.type('xpath=//div[2]/input[@id="password"]', self.password)
        sel.click('xpath=//div[@class="div_td1"]/div[6]/input')
        sel.wait_for_page_to_load(8000)
    
    def tearDown(self):
        CommonNoLogin.tearDown(self)
        
if __name__ == "__main__":
    unittest.main()