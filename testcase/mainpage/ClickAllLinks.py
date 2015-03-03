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
# ��һ���֣���֤ҳ���������Ƿ���ȷ
#===============================================================================
#        click �����-���ע��  link
        sel.click('//div[@class="div1 fade"]/a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-ע��', "click left-free-register link, page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/u/reg', 'click left-free-register link, page url is wrong')
        sel.go_back()
#        click �����-�������� link
        sel.click('//div[@class="div3 fade"]/a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-ʹ�ð���', "click left-normal-questions link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/help', 'click left-normal-questions link,page url is wrong')
        sel.go_back()
#        clikc �����-��Ϣ����  ���� link
        sel.click('//div[@class="text main_list1"]/span/a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-��Ϣ����', "click left-news more link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/news/list', 'click left-news more link,page url is wrong')
        sel.go_back()
#        clikc �ȵ����  ���� link
        sel.click('//div[@class="bg1"]/div[@class="title"]//a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-�������', "click survey more link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/sv', 'click survey more link,page url is wrong')
        sel.go_back()
#        clikc �齱�   ���� link
        sel.click('//div[@class="bg1"]/div[@class="title2"]//a')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-�齱�', "click lettory more link,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/lettory', 'click lettory more link,page url is wrong')
        sel.go_back()
#===============================================================================
# �ڶ����֣���֤�˵����������Ƿ���ȷ
#===============================================================================
#        ��֤��վ��ҳ�˵�����
        sel.click('//div[@class="top_menu"]/a[1]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������', "click main menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/', 'click main menu,page url is wrong')
#        ��֤�û����Ĳ˵�����
        sel.click('//div[@class="top_menu"]/a[2]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������', "click user-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/u', 'click user-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤��������˵�����
        sel.click('//div[@class="top_menu"]/a[3]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-�������', "click survey menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/sv', 'click survey menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤�������Ĳ˵�����
        sel.click('//div[@class="top_menu"]/a[4]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-��������', "click download-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/download', 'click download-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤�������Ĳ˵�����
        sel.click('//div[@class="top_menu"]/a[5]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-����ר��', "click reword-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/rewardcenter', 'click reword-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ ��Ϣ���� �˵�����
        sel.click('//div[@class="top_menu"]/a[6]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-��Ϣ����', "click news menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/news/list', 'click news menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ �������� �˵�����
        sel.click('//div[@class="top_menu"]/a[7]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-ʹ�ð���', "click normal-questions menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/help', 'click normal-questions menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ ��ҵ���� �˵�����
        sel.click('//div[@class="top_menu"]/a[8]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������', "click enterprise-service menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/business/apply_ac', 'click enterprise-service menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#===============================================================================
# �������֣���֤ҳ�ŵĸ�������
#===============================================================================
#        ��֤ BottomMenu ��վ��ҳ ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[1]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������', "Bottom main menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/', 'Bottom main menu,page url is wrong')
#        ��֤ BottomMenu �û����� ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[2]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������', "Bottom user-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/u', 'Bottom user-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ BottomMenu ������� ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[3]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-�������', "Bottom survey menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/sv', 'Bottom survey menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ BottomMenu �������� ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[4]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-��������', "Bottom download-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/download', 'Bottom download-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ BottomMenu ����ר�� ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[5]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-����ר��', "Bottom reward-center menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/rewardcenter', 'Bottom reward-center menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ BottomMenu ��Ϣ���� ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[6]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-��Ϣ����', "Bottom news menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/news/list', 'Bottom news menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
#        ��֤ BottomMenu �������� ����
        sel.click('//div[@class="bottom main_color1"]/div[2]/a[7]')
        sel.wait_for_page_to_load("5000")
        self.assertEqual(sel.get_title(), '�й���������������-ʹ�ð���', "Bottom normal-questions menu,page title is wrong")
        self.assertEqual(sel.get_location(), 'http://218.241.106.145/help', 'Bottom normal-questions menu,page url is wrong')
        sel.go_back()
        sel.wait_for_page_to_load("5000")
        
    def tearDown(self):
        CommonLogin.tearDown(self)

if __name__ == "__main__":
    unittest.main()
