# -*-coding:utf-8-*- 
'''
Created on 2013-3-29
Description C:/Users/lenovo/workspace/research/testcase/mainpage/ClickNews.py
@author: wyq
'''
import unittest, random, time
from testcase.common.CommonLogin import CommonLogin
from datetime import datetime
from xml.etree.ElementTree import ElementTree
from testcase.common.database import Database


class ClickNews(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_click_news(self):
        sel = self.selenium
        locateNum = random.randint(1, 6)
        xpathString = '//div[1]/div[2]/div[2]/div[2]/div[' + str(2) + ']//a'
#        newsId = int(str(sel.get_attribute(xpathString+'@href')).partition('/s/')[2])
        newTitle = sel.get_text(xpathString).encode('utf8')
        sel.click(xpathString)
        sel.wait_for_page_to_load("5000")
        self.configroot = ElementTree(file='../../conf/conf.xml').getroot()
        screenshotrootpath = self.configroot.find("screenshot/path").text + datetime.now().strftime("%Y%m%d") + '\\mainpage\\'
        screenshotFilename = "clicknews_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        sel.capture_screenshot(screenshotrootpath + screenshotFilename)
#        asertion, compare news_title & news_content on page with database data
        databasenew = Database()
        databasenew.conndata()
        conn = databasenew.dbpool.acquire()
        cursor = conn.cursor()
        cursor.execute("""
            select news_title,content 
            from RES_SYS_NEWS t 
            where t.news_title like \'%""" + newTitle + """%\'""")
        for row in cursor:
            pass
        if newTitle == '中小企业调查中奖查询':
            print """the news title is '中小企业调查中奖查询'，can't do assertion check,please check the screenshot manually: """ + screenshotFilename
        else:
#           compare news title with database data
            self.assertIn(sel.get_text('//div[@class="message_select main_color2 main_text1"]/div[1]'),
                      row[0].decode('utf8'),
                      "news_title is wrong")
            print "the news title is: " + sel.get_text('//div[@class="message_select main_color2 main_text1"]/div[1]')
#            compare news content with database data
            self.assertEqual(sel.get_text('//div[@class="message_select main_color2 main_text1"]/div[2]'),
                         row[1].decode('utf8'),
                         "news content is wrong")
            print "the news content is: " + sel.get_text('//div[@class="message_select main_color2 main_text1"]/div[2]')
        time.sleep(3)
        cursor.close()
        
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
