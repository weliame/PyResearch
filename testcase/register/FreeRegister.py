# -*-coding:utf-8-*-
import unittest, time
from testcase.common.CommonNoLogin import CommonNoLogin

class FreeRegister(CommonNoLogin):
    def setUp(self):
        CommonNoLogin.setUp(self)
    
    def test_free_register(self):
        sel = self.selenium
        #=======================================================================
        # free register flow,input right user information and then submit these information
        #=======================================================================
        sel.click('//div[@class="div1 fade"]/a[1]')
        sel.wait_for_page_to_load("5000")
#        sel.go_back()
#        sel.wait_for_page_to_load("5000")
#        sel.click('//div[@class="center_login"]//a[@href="/u/reg"]')
#        sel.wait_for_page_to_load("5000")
        sel.click('xpath=//*[@id="reg_form"]/div/div[2]/span/a')
        sel.wait_for_page_to_load(5000)
        sel.go_back()
        sel.wait_for_page_to_load(5000)
        sel.type("id=res_user_username", "test_reg1@cnnic.cn")
        sel.type("id=res_user_nickname", "test_reg1_nickname")
        sel.type("id=res_user_password", "abcd1234")
        sel.type("id=res_user_passwordconfirm", "abcd1234")
        sel.select("id=res_user_birthday", "label=1990")
        sel.click("id=res_user_gender_1")
        sel.select("id=res_user_loc_province", "label=����")
        time.sleep(1)
        sel.select("id=res_user_loc_city", "label=����")
        sel.select("id=res_user_iscity", "label=����")
        sel.select("id=res_user_job", "label=��ҵ/��˾һ��ְԱ")
        sel.select("id=res_user_education", "label=��ѧ����")
        sel.select("id=res_user_income", "label=3001��5000Ԫ")
        sel.click("id=license_f")
        sel.click("id=closeBut")
#        sel.click('xpath=//div[@class="div_btn"]/input[@class="btn1"]')
    
    def tearDown(self):
        CommonNoLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
