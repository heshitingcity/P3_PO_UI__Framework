# encoding: utf-8
#@author: newdream_daliu
#@file: selenium_basc_case.py
#@time: 2020-08-12 20:27

import os
import unittest
from common.config_utils import  local_config
from common.browser import  Browser
from common.base_page import BasePage
from common.log_utils import logger

class SeleniumBascCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info(' ')
        logger.info('=====测试类初始化=====================')
        cls.url = local_config.url

    @classmethod
    def tearDownClass(cls):
        logger.info('======测试类执行完毕=====================')
        pass

    def setUp(self):
        '''
         测试用例的初始化
        :return:
        '''
        logger.info('--------测试方法初始化---------------')
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)

    def tearDown(self):
        # 测试用例失败的截图
        errors = self._outcome.errors
        for test,exc_info in errors: #断言失败，就会有错误的信息
            if exc_info:
                self.base_page.wait()
                self.base_page.screenshot_as_file()  # 截图
        self.base_page.close_tab()
        logger.info('--------测试方法执行完毕---------------')


