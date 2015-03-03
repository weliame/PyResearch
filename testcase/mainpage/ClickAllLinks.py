# -*-coding:utf-8-*- 
'''
Created on 2013-3-29
Description C:/Users/lenovo/workspace/research/testcase/mainpage/ClickNews.py
@author: wyq
'''
import unittest
from testcase.common.CommonLogin import CommonLogin
from datetime import datetime


class ClickAllLinks(CommonLogin):
    def setUp(self):
        CommonLogin.setUp(self)
    
    def test_click_all_links(self):
        sel = self.selenium
#===============================================================================
# 第一部分：验证页面上链接是否正确
#===============================================================================
#        click 左边栏-免费注册  link
        sel.click('//div[@class="div1 fade"]/a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-注册', "click left-free-register link, page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/u/reg', 'click left-free-register link, page url is wrong')
        sel.go_back()
#        click 左边栏-常见问题 link
        sel.click('//div[@class="div3 fade"]/a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-使用帮助', "click left-normal-questions link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/help', 'click left-normal-questions link,page url is wrong')
        sel.go_back()
#        clikc 左边栏-消息公告  更多 link
        sel.click('//div[@class="text main_list1"]/span/a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-消息公告', "click left-news more link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/news/list', 'click left-news more link,page url is wrong')
        sel.go_back()
#        clikc 热点调查  更多 link
        sel.click('//div[@class="bg1"]/div[@class="title"]//a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-调查大厅', "click survey more link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/sv', 'click survey more link,page url is wrong')
        sel.go_back()
#        clikc 抽奖活动   更多 link
        sel.click('//div[@class="bg1"]/div[@class="title2"]//a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-抽奖活动', "click lettory more link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/lettory', 'click lettory more link,page url is wrong')
        sel.go_back()
#===============================================================================
# 第二部分：验证菜单栏的链接是否正确
#===============================================================================
#        验证网站首页菜单链接
        sel.click('//div[@class="top_menu"]/a[1]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区', "click main menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/', 'click main menu,page url is wrong')
#        验证用户中心菜单链接
        sel.click('//div[@class="top_menu"]/a[2]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区', "click user-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/u', 'click user-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证调查大厅菜单链接
        sel.click('//div[@class="top_menu"]/a[3]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-调查大厅', "click survey menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/sv', 'click survey menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证下载中心菜单链接
        sel.click('//div[@class="top_menu"]/a[4]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-下载中心', "click download-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/download', 'click download-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证奖励中心菜单链接
        sel.click('//div[@class="top_menu"]/a[5]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-奖励专区', "click reword-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/rewardcenter', 'click reword-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 消息公告 菜单链接
        sel.click('//div[@class="top_menu"]/a[6]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-消息公告', "click news menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/news/list', 'click news menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 常见问题 菜单链接
        sel.click('//div[@class="top_menu"]/a[7]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-使用帮助', "click normal-questions menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/help', 'click normal-questions menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 企业服务 菜单链接
        sel.click('//div[@class="top_menu"]/a[8]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区', "click enterprise-service menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/business/apply_ac', 'click enterprise-service menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#===============================================================================
# 第三部分：验证页脚的各个链接
#===============================================================================
#        验证 BottomMenu 网站首页 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[1]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区', "Bottom main menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/', 'Bottom main menu,page url is wrong')
#        验证 BottomMenu 用户中心 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[2]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区', "Bottom user-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/u', 'Bottom user-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 BottomMenu 调查大厅 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[3]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-调查大厅', "Bottom survey menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/sv', 'Bottom survey menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 BottomMenu 下载中心 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[4]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-下载中心', "Bottom download-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/download', 'Bottom download-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 BottomMenu 奖励专区 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[5]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-奖励专区', "Bottom reward-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/rewardcenter', 'Bottom reward-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 BottomMenu 消息公告 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[6]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-消息公告', "Bottom news menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/news/list', 'Bottom news menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        验证 BottomMenu 常见问题 链接
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[7]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '中国互联网调查社区-使用帮助', "Bottom normal-questions menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/help', 'Bottom normal-questions menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
        
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
