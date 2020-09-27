import os
import  configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '../config/config.ini')

class ConfigUtils():
    def __init__(self,path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path,encoding='utf-8')
    @property
    def url(self):
        value=self.cfg.get('default','url')
        return value

    @property
    def driver_path(self):
        value=self.cfg.get('default','driver_path')
        return value

    @property
    def driver_name(self):
        value=self.cfg.get('default','driver_name')
        return value
    @property
    def time_out(self):
        value=float(self.cfg.get('default','time_out'))
        return value
    @property
    def screent_shot_path(self):
        value=self.cfg.get('default','screent_shot_path')
        return value
    @property
    def username(self):
        value=self.cfg.get('default','username')
        return value

    @property
    def password(self):
        value=self.cfg.get('default','password')
        return value

    @property
    def log_path(self):
        value=self.cfg.get('default','log_path')
        return value

    @property
    def log_level(self):
        value=int(self.cfg.get('default','log_level'))
        return value

    @property
    def testdata_path(self):
        value=self.cfg.get('default','testdata_path')
        return value

    @property
    def report_path(self):
        value=self.cfg.get('default','report_path')
        return value

    @property
    def case_path(self):
        value=self.cfg.get('default','case_path')
        return value

    @property
    def smtp_server(self):
        value=self.cfg.get('email','smtp_server')
        return value
    @property
    def smtp_sender(self):
        value=self.cfg.get('email','smtp_sender')
        return value
    @property
    def smtp_password(self):
        value=self.cfg.get('email','smtp_password')
        return value
    @property
    def smtp_receiver(self):
        value=self.cfg.get('email','smtp_receiver')
        return value
    @property
    def smtp_cc(self):
        value=self.cfg.get('email','smtp_cc')
        return value
    @property
    def smtp_subject(self):
        value=self.cfg.get('email','smtp_subject')
        return value

    @property
    def element_info_path(self):
        value=self.cfg.get('default','element_info_path')
        return value

#改造2
local_config=ConfigUtils()

if __name__ == '__main__':
    print(local_config.url)
    print(local_config.driver_path)
    print(local_config.driver_name)
    print(local_config.time_out)
    print(local_config.screent_shot_path)
    print(local_config.log_path)
    print(local_config.log_level)
    print(local_config.testdata_path)
    print(local_config.report_path)
    print(local_config.case_path)
    print(local_config.smtp_sender)
    print(local_config.smtp_password)
    print(local_config.element_info_path)


