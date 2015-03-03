'''
Created on 2013-3-27
Description C:/Users/lenovo/workspace/research/testcase/common/database.py
@author: lenovo
'''
import cx_Oracle
from xml.etree.ElementTree import ElementTree

class Database():

    def conndata(self):
        configfile  = ElementTree(file='../../conf/conf.xml').getroot()
        self.dsn = configfile.find('datasource/dsn').text
        self.user = configfile.find('datasource/username').text
        self.password = configfile.find('datasource/passowrd').text
        self.dbpool = cx_Oracle.SessionPool(user=self.user, password=self.password, dsn=self.dsn, min=1, max=2, increment=1)
        return self.dbpool

    def colse(self):
        self.dbpool.drop()
        