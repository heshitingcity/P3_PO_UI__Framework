# encoding: utf-8
#@author: newdream_daliu
#@file: browser.py
#@time: 2020-08-05 20:50
# 作用:打开浏览器，提供driver
import os
from  selenium import  webdriver
from common.config_utils import local_config
from selenium.webdriver.chrome.options import Options
from common.log_utils import logger

current = os.path.dirname(__file__)
dri_path = os.path.join(current,'..',local_config.driver_path)

class Browser(object):
     def __init__(self,drvier_path=dri_path,driver_name=local_config.driver_name):
         self.__driver_path=drvier_path
         self.__driver_name=driver_name

     #二次封装
     def get_driver(self):
         if self.__driver_name.lower() =='chrome':
             return Browser().__get_chrome_driver()
         elif self.__driver_name.lower() == 'firefox':
              return Browser().__get_firefox_driver()
         elif self.__driver_name.lower() == 'edge':
              return Browser().__get_edge_driver()

     def __get_chrome_driver(self):
         chrome_options = Options()
         chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
         chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
         chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
         chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
         chrome_driver_path=os.path.join(self.__driver_path,'chromedriver.exe')
         driver = webdriver.Chrome(executable_path=chrome_driver_path)
         logger.info('初始化Google浏览器并启动')
         return driver

     def __get_firefox_driver(self):
         firefox_driver_path=os.path.join(self.__driver_path,'geckodriver.exe')
         # driver = webdriver.firefox(executable_path=firefox_driver_path)
         driver = webdriver.Firefox(executable_path=firefox_driver_path)
         logger.info('初始化Firefox浏览器并启动')
         return driver

     def __get_edge_driver(self):
         edge_driver_path = os.path.join(self.driver_path, 'MicrosoftWebDriver.exe')
         driver = webdriver.Edge(executable_path=edge_driver_path)
         logger.info('初始化Edge浏览器并启动')
         pass

     # 分布式，远程的浏览器
     def __get_remote_driver(self):  # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
         pass

if __name__=="__main__":
    Browser().get_driver();



