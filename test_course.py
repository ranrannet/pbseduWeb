# coding=utf-8
import os
import unittest

from selenium import webdriver
from urllib import request
import util_interface
from vo.hot_word import hot_word
from time import sleep
import config
from vo.course_detail_vo import course_detail_vo;



class test_course(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()



    # 获取课程列表
    def test_get_course(self,get_course_detail_vo):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/newWeb/courseAll.php?typeId=1&subjectId=GS011");
        course_list = driver.find_elements_by_xpath(
            "//div[@class='chooseSort']/ul[@class='subjectinfo choosesortInfo clearfix']/li[@class='shadow']")
        print(len(course_list))
        for course in course_list:
            print(course.find_element_by_tag_name("a").get_attribute("href"));
            print(course.find_element_by_xpath("a/*").text);
            watch = course.find_element_by_xpath(
                "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='watch']/span[2]")
            print(watch.text);
            like = course.find_element_by_xpath(
                "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='like']/span[2]")
            print(like.text);
            organ_name = course.find_element_by_xpath("div[@class='organ']/span[@class='organName']")
            print(organ_name.text);
            course_detail_link = course.find_element_by_xpath("div[@class='subjectImg']/a")
            print(course_detail_link.get_attribute("href"));
            course_image = course.find_element_by_xpath("div[@class='subjectImg']/a/img")
            print(course_image.get_attribute("src"));
            share_url_http_code = util_interface.get_url_isexist(course_image.get_attribute("src"));
            # assert share_url_http_code == config.URL_SUCCESS_CODE, "课程图片地址不存在";
            # 课程详情的课程信息


            print("");



    def tearDown(self):
        self.driver.close()
        self.driver.quit()
