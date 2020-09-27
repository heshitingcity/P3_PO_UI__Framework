# encoding: utf-8
#@author: newdream_daliu
#@file: login_ation.py
#@time: 2020-08-09 14:56
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from common.config_utils import local_config

class LoginAction:
    def __init__(self,driver):
        self.login_page=LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self,username,password):
        self.login_action(username,password)
        return MainPage(self.login_page.driver) #如果登录成功，跳转到mainpage页面

    def login_fail(self,username,password):
        self.login_action(username,password)
        return self.login_page.get_login_fail_alert_content()

    #默认登录成功
    def default_login(self):
        self.login_success(local_config.username,local_config.password)
        return MainPage(self.login_page.driver)

        #扩展
    def login_by_cookie(self):
        pass
