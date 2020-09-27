import  os
import time
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.log_utils import logger
from common.config_utils import local_config
from common import HTMLTestReportCN



class BasePage(object):
    def __init__(self,driver):
        self.driver = driver  # webdriver.Chrome()
        # self.driver= webdriver.Chrome()
        # self.chains=ActionChains(self.driver)
     #浏览器操作封装
    def open_url(self,url):
        try:
            self.driver.get(url)
            logger.info('打开url地址：%s '%url)
        except Exception as e:
            logger.error('不能打开指定的测试网址，原因是：%s'%e.__str__())

    def close_tab(self):
        self.wait(3)
        self.driver.close()
        logger.info('关闭当前的tab页')

    def exit_driver(self):
         self.driver.quit()
         logger.info('退出浏览器')

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器的最大化')
    #封装隐式等待
    def implicitly_wait(self,senconds=local_config.time_out):
        self.driver.implicitly_wait(senconds)

    def set_brower_min(self):
        self.driver.minimize_window()
        logger.info('浏览器的最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value=self.driver.title
        logger.info('获取网页标题，标题是%s'%value)
        return value

    def get_url(self):
        value=self.driver.current_url
        logger.info('获取网页网址，网址是%s'%value)
        return value

    # .... 浏览器操作补齐
    # self.username_inputbox = {'element_name': '用户名输入框',
    #                           'locator_type': 'xpath',
    #                           'locator_value': '//input[@name="account"]',
    #                           'timeout': 5}
    #元素识别封装
    def find_element(self,element_info):
        """
        根据提供的元素参数信息进行元素查找

        :param element_info:元素信息，自典类型{}
        :return: element对象
        """
        try:
            locator_type_name=element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['timeout']
            if locator_type_name == 'id':
                locator_type= By.ID
            elif  locator_type_name == 'name':
                locator_type=By.NAME
            elif  locator_type_name == 'link':
                locator_type=By.LINK_TEXT
            elif  locator_type_name == 'class':
                locator_type=By.CLASS_NAME
            elif   locator_type_name == 'xpath':
                locator_type=By.XPATH
            elif  locator_type_name == 'css':
                locator_type=By.CSS_SELECTOR
            element=WebDriverWait(self.driver,locator_timeout).\
                until(lambda x:x.find_element(locator_type,locator_value_info)) #最核心的代码
            logger.info('[%s]元素识别成功'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s]元素不识别成功,'%(element_info['element_name']))
            self.screenshot_as_file()  #元素识别识别，错误截图
        # finally:
        #     if  element is None:
        #         element = ''
        return element

    #元素操作封装
    def click(self,element_info):
        element = self.find_element(element_info)
        try:
             element.click()
             logger.info('[%s]元素进行点击操作'%element_info['element_name'])
        except Exception as e:
            logger.error('[%s]元素点击操作失败，原因是：%s'%(element_info['element_name'],e.__str__()))

    def input(self,element_info,content):
        try:
            element = self.find_element(element_info)
            element.send_keys(content)
            logger.info('[%s]元素输入数据: %s'%(element_info['element_name'],content))
        except Exception as e:
            logger.error('[%s]元素输入数据错误， 错误为：%s' % (element_info['element_name'],e.__str__()))

    def get_text(self,element_info):
        element = self.find_element(element_info)
        return element.text
    #鼠标键盘操作 （建议代码思路：判断操作系统类型）
    def move_to_element_by_mouse(self,element_info):
        element=self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element_info).perform()

    def long_press_element(self,element_info,senconds):
        element=self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(senconds).perform()

    def right_click_element(self,element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).context_click(element).perform()

    # #  鼠标封装方法2： 不推荐使用
    # def move_to_element_by_mouse(self,element_info):
    #     element=self.find_element(element_info)
    #     self.chains.move_to_element(element_info).perform()
    #
    # def long_press_element(self,element_info,senconds):
    #     element=self.find_element(element_info)
    #     self.chains.click_and_hold(element).pause(senconds).perform()

    #selenium执行js 移除元素属性
    # js = 'arguments[0].removeAttribute("value");'
    # driver.execute_script(js,wl)
    # driver.execute_script('arguments[0].removeAttribute("value");',wl)
    #给元素增加属性
    # js = 'arguments[0].setAttribute("value","newdream");'
    # driver.execute_script(js, wl)
   #封装selenium 执行 js
    def __execute_script(self,js_str,element=None):
        if element:
            self.driver.execute_script(js_str,element)
        else:
            self.driver.execute_script(js_str)

    def delete_element_attribute(self,element_info,attribute_name):
         element = self.find_element(element_info)
         self.__execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)

    def update_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value),element)

#切框架
    #思路1：
    def switch_to_frame(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    #思路2：
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)
    def switch_to_frame_by_element(self,element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)
    #思路3：
    def switch_to_frame(self,**element_dict):  #switch_to_frame(id=frameid) element=element_info
        if 'id' in element_dict.keys():
             self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to.frame(element)
    # 弹出框封装
    def switch_to_alert(self,action='accept',time_out=local_config.time_out):
        time.sleep(local_config.time_out)
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        alert_text=alert.text
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        return alert_text

    #切句柄的封装
    def get_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_window_by_title(self,title):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            # if self.get_title == title:
            if WebDriverWait(self.driver,local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break;

    def switch_to_window_by_url(self,url):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            # if self.get_url()== url:
            if WebDriverWait(self.driver,local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break;
    # 报告中添加截图
    def screenshot_as_file(self):
        report_path = os.path.join( os.path.abspath(os.path.dirname(__file__)) , '..', local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot( self.driver )


    # 截图的封装
    def screenshot_as_file_old(self,*screenshot_path):
        if len(screenshot_path)==0:
            screenshot_filepath=local_config.screent_shot_path
        else:
            screenshot_filepath=screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        current_dir=os.path.dirname(__file__)
        screenshot_filepath=os.path.join(current_dir,'..',screenshot_filepath,'UItest_%s.png'%now)
        self.driver.save_screenshot(screenshot_filepath)

    #固定等待
    def wait(self,senconds=local_config.time_out):
         time.sleep(senconds)
