import unittest

# 测试用例集管理
from selenium import webdriver

from page_object.login_page import LoginPage
from page_object.product_page import Product
from ddt import ddt, file_data

@ddt
class Cases(unittest.TestCase):
	# classmethod 修饰符
	@classmethod
	def setUpClass(cls) -> None:
		cls.driver = webdriver.Chrome()
		cls.lp = LoginPage(cls.driver)
		cls.pg = Product(cls.driver)

	@classmethod
	def tearDownClass(cls) -> None:
		cls.driver.quit()

	# 测试用例，实现登录+添加购物车流程
	@file_data('../data/user_data.yaml')
	def test_01(self, **kwargs):
		# 登录流程
		self.lp.login(kwargs['user'], kwargs['pwd'])
		# 添加购物车流程
		self.pg.choose(kwargs['time_'])
		print("购物车添加成功")

	def test_02(self, **kwargs):
		pass


if __name__ == '__main__':
	unittest.test_01()