"""
	登录页面对象，实现系统的登录流程操作
	核心操作流程：
		登录流程
		关联元素：
			账号
			密码
			登录按钮
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
	# url
	url = "http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html"
	# 页面元素
	user = (By.NAME, "accounts")
	pwd = (By.NAME, "pwd")
	button = (By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button")

	# 元素的操作流
	def login(self, username, password):
		# 访问url
		self.open()
		# 输入账号
		self.input_(self.user, username)
		# 输入密码
		self.input_(self.pwd, password)
		# 点击登录按钮
		self.click(self.button)


if __name__ == '__main__':
	driver = webdriver.Chrome()
	user = 'xuzhu666'
	pwd = '123456'
	# 实例化登录页
	lp = LoginPage(driver)
	lp.login(user, pwd)