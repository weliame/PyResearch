# -*-coding:utf-8-*- 
from selenium import selenium
import unittest
from xml.etree.ElementTree import ElementTree
from testcase.common.database import Database
from datetime import datetime


class LoginBar(unittest.TestCase):
    def setUp(self):
        """
        setUp method will create a selenium connection to the selenium driver.All parameters here are read from conf.xml
        """
        self.verificationErrors = []
        self.configfile = ElementTree(file='..\..\conf\conf.xml').getroot()
        self.weburl = self.configfile.find("weburl/url").text
        self.seleserver = self.configfile.find('seleniumserver/server').text
        self.seleport = self.configfile.find('seleniumserver/port').text
        self.browsername = self.configfile.find('browser/name').text
        self.selenium = selenium(self.seleserver, self.seleport, self.browsername, self.weburl)
        self.selenium.start()
        self.selenium.window_maximize()
    
    def test_login_bar(self):
        """
        This is the main testcase.Selenium will run this method automatically.The method name need to be start with "test"
        """
#===============================================================================
# 模拟登陆操作
#===============================================================================
        sel = self.selenium
        sel.open("/")
#        if you want change usernameEmail ,don't forget to modify relative assertion
#        username&password is from conf.xml
        username = self.configfile.find("userdata/username").text
        password = self.configfile.find("userdata/password").text
        sel.type("id=username", username)
        sel.type("id=password", password)
        sel.click("css=input[type=\"submit\"]")
        sel.wait_for_page_to_load("5000")
        screenshotdir = self.configfile.find('screenshot/path').text + datetime.now().strftime("%Y%m%d") + '\\common\\'
        screenshotFilename = "loginbar_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        sel.capture_screenshot(screenshotdir + screenshotFilename)
        
#        check the website tile,assert the website title
        self.assertEqual("中国互联网调查社区", sel.get_title() , "The websit title is not correct")

#       create database connection using Database class.The Database is just a custom class 
        data = Database()
        data.conndata()
        newpool = data.dbpool
        conn = newpool.acquire()
        cursor = conn.cursor()
#===============================================================================
# 验证登录后，登录状态栏的数据是否正确，比如：用户的nickname，积分，金币，在线天数，等级
#===============================================================================
        cursor.execute("""
            select u.userid,u.username,
                u.password,u.nickname,
                u.points,u.coin,u.online_num_day 
            from res_user u where u.username = \'"""+username+'\'')
        for row in cursor:
            pass
#        check if user's nickname is right  
        loginstatus = str(sel.get_text('xpath=//div[@class="center_login_ed"]'))
#        userpoints = int((str(loginstatus.partition('|')[1])).partion(':')[1])
        
        self.assertEqual(row[3].decode('utf8'), 
                         sel.get_text('//div[@class="center_login_ed"]/span'), 
                         "User's nickname is not correct")
        
#===============================================================================
# 验证左侧消息公告的内容与库表数据是否一致
#===============================================================================
#        the newslist is to store the news name in webpage
        newslist = []     
        for i in range(1, sel.get_xpath_count('//div[@class="text main_list1"]/div') + 1):
            newsxpath = '//div[@class="text main_list1"]/div[' + str(i) + ']'           
            newslist.append(sel.get_text(newsxpath))
#        select news data from database 
        cursor.execute("""
            select news_title from (
                select news_title from RES_SYS_NEWS t 
                where t.if_del=1 and t.status=1  
                order by t.created_at desc) 
            where rownum <=6""")
        datalist = []
        for row in cursor:  # like fetchall() 
            datalist.append((str(row[0])).decode('utf8'))
#       check whether data on page is right
        for j in range(6):
            self.assertIn((newslist[j]), datalist[j], "the news data is wrong")
#===============================================================================
# 验证首页热点调查是否库表中数据一致
#===============================================================================
#        mainpage hot surveys sql
        cursor.execute("""
            select * from (
                select s.survey_title,to_char(s.survey_expires,'yyyy-mm-dd'),s.survey_points,s.survey_coin,s.survey_lettory 
                from res_surveys s 
                where s.is_end=0 and s.survey_active='Y' 
                order by s.survey_expires desc,s.created_at desc,s.survey_title) 
            where rownum <=8 """)
        data_surveytitlelist = []
        data_surveyexpirelist = []
        date_surveyawardlist = []
        print datetime.date(datetime.now())
        for row in cursor:
            data_surveytitlelist.append(str(row[0]).decode('utf8'))
            if datetime.strptime(row[1], '%Y-%m-%d').date() > datetime.date(datetime.now()):
                data_surveyexpirelist.append(str(row[1]).decode('utf8'))
            else:
                data_surveyexpirelist.append('已结束')
        surveyawardlist = []
        for k in range(1, sel.get_xpath_count('xpath=//div[@class="text main_color1"]/dl') + 1):
            surveytitlepath = '//div[@class="text main_color1"]/dl[' + str(k) + ']'
            self.assertIn(data_surveytitlelist[k - 1], sel.get_attribute(surveytitlepath + '@title'), "No." + str(k) + " survey's title is worng")
            self.assertIn(data_surveyexpirelist[k - 1], sel.get_text(surveytitlepath + '/dd/p[1]'), "No." + str(k) + " survey's expire date is worng")
#===============================================================================
# 验证首页的抽奖活动是否与库表中数据一致
#===============================================================================
#       these list is used to store lettory Database data
        data_lettorytitlelist = []
        data_lettorygiftlist = []
        data_lettoryexpirelist = []
        data_lettorylevellist = []
        data_lettorypointlist = []
#        mainpage lettory data sql
        cursor.execute("""
            select * from (
                select l.lettory_title,l.lettory_gift,to_char(unix_to_oracle(l.lettory_end),'yyyy-mm-dd'),l.lettory_class,l.lettory_points 
                from res_lettory l 
                where l.lettory_status=1  
                order by l.lettory_end desc) 
            where rownum <=4""")
        for row in cursor:
            data_lettorytitlelist.append(str(row[0]).decode('utf8'))
            data_lettorygiftlist.append(str(row[1]).decode('utf8'))
            if datetime.strptime(row[2], '%Y-%m-%d').date() >= datetime.date(datetime.now()):
                data_lettoryexpirelist.append(str(row[2]).decode('utf8'))
            else:
                data_lettoryexpirelist.append('已结束')
            if row[3] != '0':
                data_lettorylevellist.append(str(row[3].decode('utf8')))
            else:
                data_lettorylevellist.append('无限制')
            data_lettorypointlist.append(str(row[4]).decode('utf8'))
#       asserti the lettory from database,check if the data equals to the webpage data
        for n in range(1, sel.get_xpath_count('xpath=//ul/li[@class="lty_item"]') + 1):
            lettorylipath = '//ul/li[@class="lty_item"][' + str(n) + ']'
            if self.assertEqual(data_lettorytitlelist[n - 1], sel.get_text(lettorylipath + '//li[1]'), "lettory's title is wrong"):
                print "log sucess"
            self.assertIn(data_lettorygiftlist[n - 1], sel.get_text(lettorylipath + '//li[2]'), "No." + str(n) + " lettory's gift is wrong")
            self.assertIn(data_lettoryexpirelist[n - 1], sel.get_text(lettorylipath + '//li[3]'), "No." + str(n) + " lettory's expire date is wrong")
            self.assertIn(data_lettorylevellist[n - 1], sel.get_text(lettorylipath + '//li[4]'), "No." + str(n) + " lettory's level is wrong")
            self.assertIn(data_lettorypointlist[n - 1], sel.get_text(lettorylipath + '//li[5]'), "No." + str(n) + " lettory's points is wrong")
        cursor.close()
    
    def tearDown(self):
        self.selenium.close()
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
