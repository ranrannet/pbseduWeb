# coding=utf-8
import os
import unittest

from selenium import webdriver
from urllib import request
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from util import config
import util_interface
from splinter.browser import Browser


class test_shopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        abspath = os.path.abspath(r"/Users/wangranran/Downloads/chromedriver")
        self.dr_chrome = webdriver.Chrome(abspath)

    def test_login(self):
        driver = self.driver
        driver.get("https://7fresh.m.jd.com/my.html?from=");
        login = driver.find_element_by_xpath("//div[@class='user-name']/span");
        print("-----------login text22", login.text, "-------------------------")
        sleep(5);
        login.click();
        username = driver.find_element_by_id("username");
        password = driver.find_element_by_id("password");
        username.clear();
        password.clear();
        username.send_keys("15010074631_p");
        password.send_keys("ranran_123");
        driver.find_element_by_id("loginBtn").click();

        # .set_window_size(400, 585)
        # 登录

    def test_login_chrome(self):
        driver = self.dr_chrome
        driver.get("https://7fresh.m.jd.com/my.html?from=");
        sleep(3)
        login = driver.find_element_by_xpath("//div[@class='user-name']/span");
        if "马上登录".__eq__(login.text) | "".__eq__(login.text):
            sleep(5);
            login = driver.find_element_by_xpath("//div[@class='user-name']/span");
            login.click();
            username = driver.find_element_by_id("username");
            password = driver.find_element_by_id("password");
            username.clear();
            password.clear();
            username.send_keys("15010074631_p");
            password.send_keys("ranran_123");
            driver.find_element_by_id("loginBtn").click();
            return driver
        else:
            return driver

    # def test_Jump_shop(self):
    #     self.test_login();
    #     driver = self.driver;
    #     driver.get("https://7fresh.m.jd.com/category2.html?cid=1368&from=")
    #     car_btn = driver.find_element_by_xpath("//div[@class='to-cart-btn']")
    #     car_btn.click();



    # #购物车页面未选中任何商品检查总额、合计、去结算
    # def test_all_no_checked(self):
    #     self.test_login();
    #     driver = self.driver;
    #     sleep(3);
    #     driver.find_element_by_xpath("//div[@class='footer-tools']/ul/li[3]").click();
    #     class_name_check = driver.find_element_by_xpath("//div[@class='bottom-sub']/div[@class='left-part']/label/span");
    #     class_name = class_name_check.get_attribute("class");
    #     if "check no-check".__eq__(class_name):
    #         sub_btn_class_name = driver.find_element_by_xpath("//div[@class='bottom-sub']/div[@class='right-part']/div").get_attribute("class");
    #         discountTotalPrice = driver.find_element_by_xpath("//div[@class='bottom-sub-main']/div[@class='bottom-sub-main-top']/em["
    #                                                           "@class='discountTotalPrice']").text;
    #         baseTotalPrice = driver.find_element_by_xpath("//div[@class='bottom-sub-main']/div[@class='bottom-sub-main-bottom']/em["
    #                                                       "@class='baseTotalPrice']").text;
    #         reduceTotalPrice = driver.find_element_by_xpath("//div[@class='bottom-sub-main']/div[@class='bottom-sub-main-bottom']/em["
    #                                                         "@class='reduceTotalPrice']").text;
    #         assert "sub-btn disabled".__eq__(sub_btn_class_name), "分类名称不能为空";
    #         assert "0.00".__eq__(discountTotalPrice), "没有选中任何商品，合计应为0.00";
    #         assert "0.00".__eq__(baseTotalPrice), "没有选中任何商品，总额应为0.00";
    #         assert "0.00".__eq__(reduceTotalPrice), "没有选中任何商品，优惠应为0.00";
    #     else:
    #         print("---checked--")




    #     #购物车页面选中商品检查总额、合计、去结算
    # def test_all_checked(self):
    #     self.test_login();
    #     driver = self.driver;
    #     driver.get("https://7fresh.m.jd.com/cart.html?from=");
    #     sleep(5)
    #     class_name_check = driver.find_element_by_xpath("//div[@class='bottom-sub']/div[@class='left-part']/label/span");
    #     class_name = class_name_check.get_attribute("class");
    #     if "check no-check".__eq__(class_name):
    #         class_name_check.click();
    #         self.check_shopping_price(driver)
    #     else:
    #         self.check_shopping_price(driver)
    #
    #
    #
    #
    # #
    # def check_shopping_price(self, driver):
    #     sub_btn_class_name = driver.find_element_by_xpath("//div[@class='bottom-sub']/div[@class='right-part']/div").get_attribute("class");
    #     discountTotalPrice = driver.find_element_by_xpath("//div[@class='bottom-sub-main']/div[@class='bottom-sub-main-top']/em["
    #                                                       "@class='discountTotalPrice']").text;
    #     baseTotalPrice = driver.find_element_by_xpath("//div[@class='bottom-sub-main']/div[@class='bottom-sub-main-bottom']/em["
    #                                                   "@class='baseTotalPrice']").text;
    #     self.assertNotEqual("0.00", discountTotalPrice, "合计不应该为0.00元");
    #     self.assertNotEqual("0.00", baseTotalPrice, "合计不应该为0.00元");
    #     self.assertEqual("sub-btn", sub_btn_class_name, "结算按钮应为可点击状态");




            # 调用二级分类
    def test_shopping(self, null=None):
        driver = self.driver
        self.test_login();
        driver.get("https://7fresh.m.jd.com/cart.html?from=");
        product_items = driver.find_elements_by_xpath("//div[@class='cart-items-main']/div[@class='cart-items-list']/div[@class='items-list']/div[@class='filter-item']")
        for product in product_items:
            goods_name = product.find_element_by_xpath("div[@class='items-detail']/div[@class='goods-name']");
            specification = product.find_element_by_xpath("div[@class='items-detail']/div[@class='goods-specification']");
            price = product.find_element_by_xpath("div[@class='items-detail']/div[@class='goods-price']");
            operate = product.find_element_by_xpath("div[@class='items-detail']/div[@class='operate']");
            subtotal = product.find_element_by_xpath("div[@class='items-detail']/div[@class='subtotal']");






    def tearDown(self):
        print("test")
        self.driver.close()
        self.dr_chrome.close()
