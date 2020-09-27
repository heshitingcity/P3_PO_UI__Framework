# encoding: utf-8
#@author: newdream_daliu
#@file: login_case.py
#@time: 2020-08-09 15:21

import unittest

from common.browser import Browser
from common.base_page import  BasePage
from common.config_utils import local_config
from common.selenium_basc_case import SeleniumBascCase
from actions.login_ation import LoginAction
from common.test_data_utils import TestDadaUtils

class LoginTest(SeleniumBascCase):
    # test_class_data = TestDadaUtils('login_suite', 'LoginTest').convert_exceldata_to_testdata()
    test_class_data = TestDadaUtils('login_suite', 'login_case_test','LoginTest').convert_exceldata_to_testdata()

    def setUp(self):
        super().setUp()

    #不执行未True 执行未False
    @unittest.skipIf(test_class_data['test_login_success']['isnot'], '条件为真跳过')
    def test_login_success(self):
        test_function_data=self.test_class_data['test_login_success']
        self._testMethodDoc=test_function_data['test_name']

        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_success(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        # self.assertEqual('测试人员1','测试人员1','test01登录失败')
        self.assertEqual(main_page.get_username(),test_function_data['excepted_result'],'test01登录失败')

    @unittest.skipIf(test_class_data['test_login_fail']['isnot'], '条件为真跳过')
    def test_login_fail(self):
        test_function_data=self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name']

        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        print('actual_result:%s'%actual_result)
        self.assertEqual(actual_result,test_function_data['excepted_result'])

if __name__=="__main__":
    unittest.main()