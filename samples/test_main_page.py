# encoding: utf-8
#@author: newdream_daliu
#@file: test_main_page.py
#@time: 2020-08-09 16:22
from common.browser import Browser
from actions.login_ation import LoginAction

if __name__=="__main__":
    driver=Browser().get_driver()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    main_page=LoginAction(driver).login_success('test01','newdream123')
    value=main_page.get_username()
    print(value)