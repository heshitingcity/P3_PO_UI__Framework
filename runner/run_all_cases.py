# encoding: utf-8
#@author: newdream_daliu
#@file: run_all_cases.py
#@time: 2020-08-16 14:33
#@desc:
import os
import unittest
from common import HTMLTestReportCN
from common.config_utils import local_config
from common.email_utils import EmailUtils
from common.zip_utils import zip_dir

current_path = os.path.dirname(__file__)
report_path=os.path.join(current_path,'..',local_config.report_path)
case_path= os.path.join(current_path,'..',local_config.case_path)

class RunAllCases(object):
    def __init__(self):
        self.test_case_path =case_path
        self.report_path=report_path
        self.title = '禅道UI自动化测试报告'
        self.description = 'newdream_P3_test'

    def run(self):
        #测试套件的构建
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        #报告的处理
        report_dir=HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path=HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path=HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp=open(report_path,'wb')
        runner=HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                               title=self.title,
                                               description=self.description,
                                               tester='daliu')
        runner.run(all_suite)
        fp.close()
        return dir_path

if __name__=="__main__":
    # #演示1
    # dir_path = RunAllCases().run()  #执行报告，返回报告路径
    # print(dir_path)
    # report_zip_path= dir_path+'/../禅道UI自动化测试报告.zip'
    # zip_dir(dir_path,report_zip_path)
    # EmailUtils('PythonUI自动化测试报告(正式版)',report_zip_path).send_mail()

    # # #演示2
    dir_path=RunAllCases().run()
    print(dir_path)
    EmailUtils('PythonUI自动化测试报告',dir_path).zip_send_mail()
