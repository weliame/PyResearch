'''
Created on 2013-4-5

@author: wyq
'''
from common.CommonLogin import CommonLogin
import unittest

class DownloadReport(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_download_report(self):
        sel = self.selenium
        #=======================================================================
        # In Download_center ,a nologin user click a report link ,then download the report
        #=======================================================================
        sel.click('xpath=//div[@class="top_menu"]/a[4]')
        sel.wait_for_page_to_load(5000)
        sel.click('xpath=//div[@class="down_select main_color1"]/div[2]/div[3]/input')
        
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()