# -*-coding:utf-8-*-
import unittest
from testcase.common.CommonNoLogin import CommonNoLogin


class FindPassword(CommonNoLogin):
    def setUp(self):
        CommonNoLogin.setUp(self)
    
    def test_find_password(self):
        sel = self.selenium
        sel.open("/")
        sel.click("link=Íü¼ÇÃÜÂë")
        sel.wait_for_page_to_load("5000")
        sel.type("id=reg_email", "test_reg1@cnnic.cn")
#        sel.click("css=input.btn1.firepath-matching-node")
        sel.click('xpath=//div[@class="div_tr"]/div/input[@class="btn1"]')
        sel.wait_for_page_to_load("5000")
    
    def tearDown(self):
        CommonNoLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
