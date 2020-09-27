# encoding: utf-8
#@author: newdream_daliu
#@file: demo2.py
#@time: 2020-08-09 10:08

from  common.element_data_utils import ElementDataUtils

str1='bug的标题：%s'
title='班级管理页面存在错别字'
print('bug的标题：%s'%title)
print(str1%title)

str2=str1%title
print(str2)
#############################################################
elements=ElementDataUtils('login').get_element_info('bug_page')
bug_link=elements['bug_link']
print(bug_link)
#方法1
locator_value=bug_link['locator_value']%title
print('方式1：'+locator_value)
#方法2
locator_value=bug_link.get('locator_value')%title
print('方式2：'+locator_value)

#最终的处理
bug_link['locator_value']=bug_link.get('locator_value')%title
bug_link['element_name']=bug_link.get('element_name')%title
print(bug_link)