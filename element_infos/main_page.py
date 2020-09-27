import  os
from selenium import  webdriver
from selenium.webdriver.common.by import By
from element_infos.login_page import LoginPage
from common.log_utils import logger
from common.element_data_utils import ElementDataUtils
from common.base_page import BasePage

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)  # 子类显示调用父类的构造方
        #元素定位信息
        elements = ElementDataUtils('main', 'main_page').get_element_info()
        self.myzone_link=elements['myzone_link']
        self.user_menu=elements['user_menu']
        self.quit_button=elements['quit_button']
    #控件的操作
    def goto_myzone(self):  #点击我的地盘
        self.click(self.myzone_link)

    def get_username(self):
        value=self.get_text(self.user_menu)
        return  value

    #点击用户名菜单
    def click_username(self):
        self.click(self.user_menu)

    #点击退出按钮
    def click_quit_button(self):
         self.click(self.quit_button)

