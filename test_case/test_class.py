# coding=utf-8
import os
import unittest
from time import sleep
from selenium import webdriver


# 分类
import util_interface
from util import config


class test_case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        abspath = os.path.abspath(r"/Users/wangranran/Downloads/chromedriver")
        self.dr_chrome = webdriver.Chrome(abspath)
        # self.driver =self.driver.set_window_size(480,800);
    #     google v64  2.35
    #

    def test_login(self):
        driver = self.driver
        driver.get("https://7fresh.m.jd.com/my.html?from=");
        # driver = self.driver.set_window_size(480, 800);

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

    def test_class_one(self, null=None):
        driver = self.driver
        self.test_login();
        driver.get("https://7fresh.m.jd.com/index.html?storeId=131229");
        class_icon = driver.find_element_by_xpath("//div[@class='tools-icon to-cat']")
        class_icon.click();
        sleep(5);
        class_tr_list = driver.find_elements_by_xpath("/html/body/div[3]/table/tbody/tr")
        for class_tr in class_tr_list:
            class_td_list = class_tr.find_elements_by_xpath("td[@id='category1']");
            for class_td in class_td_list:
                img_src = class_td.find_element_by_tag_name("img").get_attribute("src");
                class_name = class_td.find_element_by_xpath("daiv").text;
                print(img_src, '-------src-------name----------', class_name);
                assert class_name != null, "分类名称不能为null";
                assert class_name is not None, "分类名称不能为空";
                status = util_interface.get_url_isexist(img_src);
                assert status == config.URL_SUCCESS_CODE, "分类图片地址不存在";

    def test_class_one_search(self):
        driver = self.driver
        self.test_login();
        driver.get("https://7fresh.m.jd.com/index.html?storeId=131229");
        class_icon = driver.find_element_by_xpath("//div[@class='tools-icon to-cat']")
        class_icon.click();
        sleep(5);
        search_input = driver.find_element_by_id("searchInput");
        search_input.clear();
        search_input.send_keys("苹果");
        search_result_li_list = driver.find_elements_by_xpath("//div[@class='autospell-container']/ul[@class='autospell-wrapper']/li");
        print(len(search_result_li_list), '------------size------------');
        for result_li in search_result_li_list:
            span_text = result_li.find_element_by_tag_name("span").text;


    # 调用二级分类
    def test_class_one(self, null=None):
        driver = self.driver
        self.test_login();
        driver.get("https://7fresh.m.jd.com/index.html?storeId=131229");
        class_icon = driver.find_element_by_xpath("//div[@class='tools-icon to-cat']")
        class_icon.click();
        sleep(5);
        class_tr_list = driver.find_elements_by_xpath("/html/body/div[3]/table/tbody/tr")
        for class_tr in class_tr_list:
            class_td_list = class_tr.find_elements_by_xpath("td[@id='category1']");
            for class_td in class_td_list:
                cid = class_td.get_attribute('cid');
                self.get_class_visit_two(cid);

                # 二级分类请求

    def get_class_visit_two(self, cid):
        dr_chrome = self.test_login_chrome()
        dr_chrome.get("https://7fresh.m.jd.com/category2.html?cid=%s&from=" % cid)
        sleep(8)
        product_list = dr_chrome.find_elements_by_xpath("//div[@class='items-wrapper']/ul[@class='items-ul']/li")
        for product in product_list:
            img = product.find_element_by_xpath("div[@class='item-content']/div[@class='item-img']/img").get_attribute("src");
            title = product.find_element_by_xpath("div[@class='item-content']/div[@class='right']/div[@class='top']/div[@class='title']").text;
            price = product.find_element_by_xpath(
                "div[@class='item-content']/div[@class='right']/div[@class='bottom']/div[@class='item-price']/div[@class='now']/span[1]").text;
            company = product.find_element_by_xpath(
                "div[@class='item-content']/div[@class='right']/div[@class='bottom']/div[@class='item-price']/div[@class='now']/span[2]").text;
            assert title is not None, "商品名称不能为空";
            assert price is not None, "价格不能为空";
            assert company is not None, "单位不能为空";

    # 三级分类请求
    def test_class_visit_three(self):
        dr_chrome = self.test_login_chrome()
        dr_chrome.get("https://7fresh.m.jd.com/category2.html?cid=1368&from=")
        sleep(5)
        product_list_left_class = dr_chrome.find_elements_by_xpath("//div[@class='category2-container']/div[@class='cate2-left-container']/div")
        for left_class in product_list_left_class:
            assert left_class.text is not None, "三级分类名称不能为空";
            sleep(3);
            left_class.click();
            sleep(3);
            # 请求商品列表
            product_list = dr_chrome.find_elements_by_xpath("//div[@class='items-wrapper']/ul[@class='items-ul']/li")
            for product in product_list:
                img = product.find_element_by_xpath("div[@class='item-content']/div[@class='item-img']/img").get_attribute("src");
                title = product.find_element_by_xpath("div[@class='item-content']/div[@class='right']/div[@class='top']/div[@class='title']").text;
                price = product.find_element_by_xpath(
                    "div[@class='item-content']/div[@class='right']/div[@class='bottom']/div[@class='item-price']/div[@class='now']/span[1]").text;
                company = product.find_element_by_xpath(
                    "div[@class='item-content']/div[@class='right']/div[@class='bottom']/div[@class='item-price']/div[@class='now']/span[2]").text;
                assert title is not None, "商品名称不能为空";
                assert price is not None, "价格不能为空";
                assert company is not None, "单位不能为空";

    def tearDown(self):
        print("test")
        self.driver.close()
        self.dr_chrome.close()
