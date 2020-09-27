# encoding: utf-8
#@author: newdream_daliu
#@file: demo3.py
#@time: 2020-08-12 20:20
import unittest
from common.browser import  Browser
from common.base_page import BasePage
from common.config_utils import  local_config

from actions.login_ation import LoginAction
from actions.quit_action import QuitAction

class DemoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('==========测试类开始初始化================')
        cls.base_page = BasePage(Browser().get_driver())
        cls.base_page.set_browser_max()
        cls.base_page.implicitly_wait()
        cls.base_page.open_url(local_config.url)

    @classmethod
    def tearDownClass(cls):
        cls.base_page.wait(local_config.time_out)
        cls.base_page.close_tab()
        print('==========测试类执行完成完毕================')
    def setUp(self):
        print('------------测试用例开始测试化---------------')
    def tearDown(self):
        print('------------测试用例执行完毕-----------------')
    def test_01(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'), True, 'test_quit 用例不通过')

    def test_02(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'), True, 'test_quit 用例不通过')

    def test_03(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'), True, 'test_quit 用例不通过')

if __name__=="__main__":
    unittest.main()
