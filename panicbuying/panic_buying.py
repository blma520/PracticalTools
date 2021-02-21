import datetime
import time
from selenium import webdriver

url_dict = {'taobao' : ['https://www.taobao.com', 'https://cart.taobao.com/cart.htm'],
 'jingdong' : []}


def login(browser, shop_name):
	browser.get(url_dict[shop_name][0])
	time.sleep(15)
	
	if shop_name == 'taobao':
		if browser.find_element_by_link_text("亲，请登录"):
			browser.find_element_by_link_text("亲，请登录").click()
			print("请90秒内扫码登录...")
			time.sleep(90)
			browser.get(url_dict[shop_name][1])
	elif shop_name == 'jingdong':
		pass
	time.sleep(5)
	now = datetime.datetime.now()
	print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
	
def buy(browser, shop_name, buy_time):
	while True:
		now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		if now >= buy_time:
			if shop_name == 'taobao':
				while True:
					try:
						if browser.find_element_by_id("J_Go"):
							browser.find_element_by_id("J_Go").click()	
						break
					except:
						pass
						
				while True:
					try:
						if browser.find_element_by_link_text('提交订单'):
							browser.find_element_by_link_text('提交订单').click()
							print("结算成功")
							break
					except:
						pass
			break
	

if __name__ == "__main__":
	buy_time = input("Please input buy time: type(2021-01-01 12:00:00.000000):")
	shop_name = input("Please choose shop: (taobao, jingdong):")
	browser = webdriver.Chrome("chromedriver.exe")
	browser.maximize_window()
	
	login(browser, shop_name)
	buy(browser, shop_name, buy_time)
	
	