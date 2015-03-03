# -*-coding:utf-8-*- 
'''
Created on 2013-3-28
Description C:/Users/lenovo/workspace/research/testcase/mainpage/ClickNews.py
@author: wyq
'''
import unittest, time
from testcase.common.CommonLogin import CommonLogin
from testcase.common.database import Database
from datetime import datetime
from xml.etree.ElementTree import ElementTree

class AttendLottery(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_attend_lottery(self):
        sel = self.selenium
#       To get the first lettory's id on the mainpage
        lty_id = sel.get_attribute('xpath=//ul/li[@class="lty_item"][1]/input[@class="lty_id"]@value')
#        function test:the first setp , 参加第一个抽奖，click 立即参加  
        sel.click('//ul/li[@class="lty_item"][1]')
        sel.wait_for_page_to_load("5000")
#        get the screenshot save directory ,then capture_screenshot
        self.configroot = ElementTree(file='../../conf/conf.xml').getroot()
        screenshotrootdir = self.configroot.find("screenshot/path").text + datetime.now().strftime("%Y%m%d") + '\\mainpage\\'
        clicklettory_shotfilename = "clicklettory_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        sel.capture_screenshot(screenshotrootdir + clicklettory_shotfilename)
     
        databasenew = Database()
        databasenew.conndata()
        conn = databasenew.dbpool.acquire()
        cursor = conn.cursor()
#        given lettory_Id,select lettory data 
        cursor.execute("""
            select l.lid,
                l.lettory_title,
                to_char(unix_to_oracle(l.lettory_start),'yyyy-mm-dd HH24:MI'),
                to_char(unix_to_oracle(l.lettory_end),'yyyy-mm-dd HH24:MI'),
                to_char(unix_to_oracle(l.lettory_prodate),'yyyy-mm-dd HH24:MI'),
                l.lettory_points,
                l.lettory_gift,
                l.lettory_desc,
                l.lettory_nums,
                l.lettory_maxnums,
                l.lettory_class, 
                l.lettory_pic
            from res_lettory l where l.lid = """ + lty_id)
        for row in cursor:
            pass
#        asert the nivigateor 
        self.assertIn(row[1].decode('utf8'),
                      sel.get_text('xpath=//div[@class="center"]/div[2]'),
                      "location is wrong")
#        assert the lettory title
        self.assertEqual(row[1].decode('utf8'),
                         sel.get_text('xpath=//div[@class="message_select main_color2 main_text1"]/div[@class="title"]'),
                         "lettory_title is wrong")
#        assert the lettory start date
        self.assertEqual(row[2].decode('utf8'),
                         sel.get_text('//div[@class="message_select main_color2 main_text1"]/div/div[1]/div[@class="ltry_cnt"]'),
                         "lettory_begin_date is wrong")
#        assert the lettory end date
        self.assertEqual(row[3].decode('utf8'),
                         sel.get_text('//div[@class="message_select main_color2 main_text1"]/div/div[2]/div[@class="ltry_cnt"]'),
                         "lettory_end_date is wrong")
#        assert the lettory public date
        self.assertEqual(row[4].decode('utf8'),
                         sel.get_text('//div[@class="message_select main_color2 main_text1"]/div/div[3]/div[@class="ltry_cnt"]'),
                         "lettory_public_date is wrong")
#        assert the lettory points requirement
        self.assertEqual(str(row[5]).decode('utf8'),
                         sel.get_text('//div[@class="message_select main_color2 main_text1"]/div/div[4]/div[@class="ltry_cnt"]'),
                         "lettory_require_point is wrong")
#        assert the lettory gift
        self.assertEqual(row[6].decode('utf8'),
                         sel.get_text('//div[@class="message_select main_color2 main_text1"]/div/div[5]/div[@class="ltry_cnt"]'),
                         "lettory_gift is wrong")
#        assert the lettory desc
        self.assertIn(sel.get_text('//*[@id="ltry_desc"]'),
                      str(row[7]).decode('utf8'),
                      "lettory_desc is wrong") 
#        function test:the second setp         
        sel.click('id=ltry_btn')
        sel.wait_for_page_to_load("5000")
#        assert : when attending the lettory, lettory_nums >= lettory_maxnums,then hint user out of number limition
        if row[8] >= row[9]:
            self.assertIn('人数已达上限',
                          sel.get_text('xpath=/html/body/div[1]/div[3]/div[2]/div[2]/div[2]'),
                          'out of limition num,bug the hints is wrong')
        attendlettory_shotfilename = "attendlettory_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        sel.capture_screenshot(screenshotrootdir + attendlettory_shotfilename)
        time.sleep(3)
        self.assertEqual(str(sel.get_location()), sel.browserURL + "lettory", "url is not right")
        cursor.close()
        
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
