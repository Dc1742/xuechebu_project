"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    phone=page.phone
    pwd=page.pwd
    login_btn=page.login_btn
    confirm_btn=page.comfirm_btn

    def input_phone(self,phone):
        self.input_func(self.phone,phone)

    def input_pwd(self,pwd):
        self.input_func(self.pwd,pwd)

    def click_login_btn(self):
        self.click_func(self.login_btn)

    def click_confirm_btn(self):
        self.click_func(self.confirm_btn)
