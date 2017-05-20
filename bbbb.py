from PIL import Image
import pytesseract
from selenium import webdriver
import sys


url = 'http://www.pbsedu.com/public/code/code_str.php'
# url ='http://www.pbsedu.com/'
driver = webdriver.Firefox()
driver.maximize_window();
driver.get(url)

driver.save_screenshot('/Users/wangranran/Downloads/aa.png')  # 截取当前网页，该网页有我们需要的验证码
# imgelement = driver.find_element_by_xpath('//*[@id="J-download"]/div[1]');  # 定位验证码
#
# location = imgelement.location  # 获取验证码x,y轴坐标
# size = imgelement.size  # 获取验证码的长宽
#
# left = int(location['x'])
# top = int(location['y'])
# right = int(location['x'] + size['width'])
# bottom = int(location['y'] + size['height']+200)
#
# print(left);
# print(top);
# print(right);
# print(bottom);
#
#
# rangle =(50,50,100,100);
# # 写成我们需要截取的位置坐标
# i = Image.open("/Users/wangranran/Downloads/aa.png")  # 打开截图
#
# frame4 = i.crop()  # 使用Image的crop函数，从截图中再次截取我们需要的区域
# frame4.save('/Users/wangranran/Downloads/frame4.png')
# qq = Image.open('/Users/wangranran/Downloads/frame4.png')
# text = pytesseract.image_to_string(qq).strip()  # 使用image_to_string识别验证码
# print("aaa",text);
