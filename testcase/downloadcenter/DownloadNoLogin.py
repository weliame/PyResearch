# -*-coding:utf-8-*-
'''
Created on 2013-4-5

@author: wyq
'''

from common.CommonNoLogin import CommonNoLogin
import unittest

class DownloadClient(CommonNoLogin):
    def setUp(self):
        CommonNoLogin.setUp(self)
    
    def test_download_client(self):
        sel = self.selenium
        #=======================================================================
        # In Download_center ,click "Download Client" button
        #=======================================================================
        sel.click('xpath=//div[@class="top_menu"]/a[4]')
        sel.wait_for_page_to_load(5000)
        sel.click('xpath=//div[@class="down_select main_color1"]/div[2]/div[3]/input')
        
        
    
    def tearDown(self):
        CommonNoLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
        