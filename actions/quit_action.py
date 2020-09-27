# encoding: utf-8
#@author: newdream_daliu
#@file: quit_action.py
#@time: 2020-08-09 16:50
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from common.config_utils import local_config

class QuitAction(object):
    def __init__(self,driver):
        self.main_page=MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return  LoginPage(self.main_page.driver) #退出操作后，返回到主页面