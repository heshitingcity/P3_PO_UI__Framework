# encoding: utf-8
#@author: newdream_daliu
#@file: read_test_data.py
#@time: 2020-08-16 17:44
#@desc:
from common.excel_utils import ExcelUtils

file_path='D:/P3_PO_UI_Test_Framework/test_datas/test_data_infos.xlsx'
excel_data=ExcelUtils(file_path,'login_suite').get_sheet_data_by_list()
excel_row=len(excel_data)
test_class_name='LoginTest'

# print(excel_data)
# for s in excel_data:
#     print(s)


test_data_infos={}  #所有的测试用例
for i in range(1,excel_row):
    test_data_info={}  #一条测试用例的数据
    if excel_data[i][2].__eq__(test_class_name):
          test_data_info['test_name']= excel_data[i][1]
          # 如果执行用例为是，返回 False,如果不执行就返回True
          test_data_info['isnot'] =False if excel_data[i][3].__eq__('是') else True
          test_data_info['excepted_result'] = excel_data[i][4]
          test_parameter={}
          for j in range(5,len(excel_data[i])):
            #参数里面包含=号，或者长度大于2,才算一个正常的参数（a=1）
             if excel_data[i][j].__contains__('=') and len(excel_data[i][j])>2:
                # username = test01
                parameter_info=excel_data[i][j].split('=')
                #分割 parameter_info[0]=username parameter_info[1]=test01
                print('key:',parameter_info[0])
                print('value:',parameter_info[1])
                test_parameter[parameter_info[0]]=parameter_info[1]  #key 不存在即是添加
                # print(test_parameter)
          test_data_info['test_parameter']=test_parameter
    test_data_infos[excel_data[i][0]] = test_data_info  # 所有的测试用例
# print(test_data_infos)