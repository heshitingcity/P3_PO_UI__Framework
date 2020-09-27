# encoding: utf-8
#@author: newdream_daliu
#@file: quit_test.py
#@time: 2020-08-09 17:10
import unittest
from common.selenium_basc_case import  SeleniumBascCase
from common.test_data_utils import TestDadaUtils

from actions.login_ation import LoginAction
from actions.quit_action import QuitAction


class QuitTest(SeleniumBascCase):
     # test_class_data = TestDadaUtils('main_suite', 'QuitTest').convert_exceldata_to_testdata()
     test_class_data = TestDadaUtils('main_suite', 'quit_test','QuitTest').convert_exceldata_to_testdata()
     def setUp(self):
         super().setUp()

     @unittest.skipIf(test_class_data['test_quit']['isnot'], '条件为真跳过')
     def test_quit(self):
         test_function_data = self.test_class_data['test_quit']
         self._testMethodDoc = test_function_data['test_name']

         login_action=LoginAction(self.base_page.driver)
         main_page=login_action.default_login()

         quit_action=QuitAction(main_page.driver)
         login_page = quit_action.quit()
         actual_result=login_page.get_title()
         self.assertEqual(actual_result.__contains__(test_function_data['excepted_result']),True,'test_quit 用例不通过')

if __name__=="__main__":
    unittest.main(verbosity=2)