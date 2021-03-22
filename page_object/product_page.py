"""
	商品详细页面对象，实现商品详细页面添加商品到购物车的流程操作
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Product(BasePage):
	url = "http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html"
	button = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')

	def choose(self, time_):
		self.open()
		self.wait(time_)
		self.click(self.button)