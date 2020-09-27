# encoding: utf-8
#@author: newdream_daliu
#@file: test_data_utils.py
#@time: 2020-08-16 11:09
#@desc:


import  os
from common.excel_utils  import ExcelUtils
from  common.log_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
testdata_path = os.path.join(current_path,'..',local_config.testdata_path)

class TestDadaUtils(object):
    def __init__(self,test_suite_name,test_file_name,test_class_name=None,testdata_path=testdata_path):
        self.test_class_name=test_class_name
        testdata_path=os.path.join(testdata_path,test_suite_name,test_file_name+'.xlsx')
        self.excel_data= ExcelUtils(testdata_path,test_class_name).get_sheet_data_by_list()
        self.excel_row=len(self.excel_data)

    # {' test_login_success ':{
    #      'test_name':'验证是否能成功进行登录',
    #      'isnot':'是',
    #      'excepted_result':'测试人员1',
    #      'test_parameter':{' username':'test01',' password':'newdream123'}
    #    }}
    def convert_exceldata_to_testdata(self):
        test_data_infos={}  #所有的测试用例
        for i in range(1,self.excel_row):
            test_data_info={}  #一条测试用例的数据
            test_data_info['test_name']= self.excel_data[i][1]
            # 如果执行用例为是，返回 False,如果不执行就返回True
            test_data_info['isnot'] =False if self.excel_data[i][2].__eq__('是') else True
            test_data_info['excepted_result'] = self.excel_data[i][3]
            test_parameter={}
            for j in range(4,len(self.excel_data[i])):
                    #参数里面包含=号，或者长度大于2,才算一个正常的参数（a=1）
                    if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j])>2:
                        # username = test01
                        parameter_info=self.excel_data[i][j].split('=')
                        test_parameter[parameter_info[0]]=parameter_info[1]
            test_data_info['test_parameter']=test_parameter
            test_data_infos[self.excel_data[i][0]] = test_data_info  # 所有的测试用例
        return test_data_infos

if __name__=="__main__":
    infos=TestDadaUtils('login_suite','login_case_test').convert_exceldata_to_testdata()
    # infos = TestDadaUtils('main_suite', 'quit_test').convert_exceldata_to_testdata()
    for s in infos.values():
        print(s)



