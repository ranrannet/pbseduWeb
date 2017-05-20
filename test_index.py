# coding=utf-8
import os
import unittest

from selenium import webdriver
from urllib import request
from time import sleep

from selenium.webdriver import ActionChains

import util_interface


class test_index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()



    # 鼠标移入事件
    def test_move_to_class_type(self):
        driver = self.driver
        driver.get("http://www.pbsedu.com");
        sleep(3);
        # 定位到鼠标移动到上面的元素
        above1 = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div/a[1]');
        # 对定位到的元素执行鼠标移动到上面的操作
        ActionChains(driver).context_click(above1).perform()


    # 获取分类及二级科目
    def test_index_left_type(self):
        driver = self.driver
        driver.get("http://www.pbsedu.com/");
        type_list = driver.find_elements_by_xpath("//div[@id='J-mainNav']/ul[@class='list']/li");
        for type_info in type_list:
            type_name = type_info.find_element_by_tag_name("a").text;
            print("type---name------", type_name);
            assert type_name is not None, "一级分类不能为空"
            subject_name_one = type_info.find_element_by_xpath('div/a[1]')
            print(subject_name_one.text)
            assert subject_name_one.text is not None, "科目名称不能为空"
            subject_name_second = type_info.find_element_by_xpath('div/a[2]')
            print(subject_name_second.text)
            assert subject_name_one.text is not None, "科目名称不能为空"

    # banner列表的图片、文本、及link
    def test_get_logo(self):
        driver = self.driver
        driver.get("http://www.pbsedu.com/");
        sleep(3);
        index_url = driver.title;
        image = driver.find_element_by_xpath("//div[@class='logoImg']/a/img");
        image.click();
        curl_title = driver.title;
        self.assertEqual(index_url, curl_title, "logo对应的地址错误");

    # 获取banner列表
    def test_get_banner_list(self):
        driver = self.driver
        driver.get("http://www.pbsedu.com/");

        banner_list = driver.find_elements_by_xpath("//div[@class='slide']/div[@class='slideimgBox']/a")
        for banner in banner_list:
            # 课程图片是否存在
            pic_url = banner.find_element_by_xpath("img").get_attribute("src");
            pic_url_status = util_interface.get_url_isexist(pic_url);
            assert pic_url_status == 200, "图片地址不存在";
            banner_title = banner.find_element_by_xpath("//div[@class='banner-title']").text;
            assert banner_title is not None, "banner标题不能为空";
            # 获取课程详情
            link = banner.get_attribute("href")
            # 待完善
            # driver.get(link);
            # driver.back();

    # 手动点击箭头播放课件
    def test_hand_get_banner_list(self):
        driver = self.driver
        driver.get("http://www.pbsedu.com/");

        banner_list = driver.find_elements_by_xpath("//div[@class='slide']/div[@class='slideimgBox']/a")
        for banner in banner_list:
            driver.find_element_by_xpath("//div[@class='slide']/span[@class='slide-R btnRight']").click();

    # 获取底部机构信息
    def test_get_orgion_list(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/");
        orgion_list = driver.find_elements_by_xpath("//div[@class='cooperation-box clearfix']/a")
        print(len(orgion_list));
        for orgion in orgion_list:
            print("机构的图片：" + orgion.find_element_by_tag_name("img").get_attribute("src"));
            orgion_pic = orgion.find_element_by_tag_name("img").get_attribute("src");
            print(orgion_pic);
            status = util_interface.get_url_isexist(orgion_pic);
            assert status == 200, "图片地址不存在";

    # 热门推荐
    def test_get_good_list(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/");
        banner_list = driver.find_elements_by_xpath("//div[@id='J-goodCourse']/a[@class='goodlist']")
        for banner in banner_list:
            course_name = banner.find_element_by_tag_name("p").text;
            print(course_name);
            assert course_name is not None, "课程名称不存在";
            link = banner.get_attribute("href");
            assert link is not None, "课程请求地址名称不存在";
            course_pic = banner.find_element_by_tag_name("img").get_attribute("src");
            course_pic_is_exist = util_interface.get_url_isexist(course_pic);
            assert course_pic_is_exist is not None, "课程图片地址不存在";

    # 获取分类及分类下的课程列表（检查分类名称、分类链接、分类大图片）
    def test_get_type_info(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/");
        course_Left = driver.find_elements_by_xpath("//div[@class='courseBox']/div[@class='course']")
        for course_type in course_Left:
            print("--------------------------------------------");
            type_info = course_type.find_element_by_xpath("div[@class='courseLeft']/h2[@class='coursename']/a");
            print("分类链接：", type_info.get_attribute("href"));
            print("分类名称:" + type_info.find_element_by_tag_name("span").text);
            type_name = type_info.find_element_by_tag_name("span").text;
            assert type_name is not None, "分类名称不能为空";
            print("--------------------------------------------");
            # 大的分类图片
            type_pic = course_type.find_element_by_xpath("div[@class='courseLeft']/a");
            print("大的分类图片对应的链接：" + type_pic.get_attribute("href"));
            print("大的分类图片的Url：" + type_pic.find_element_by_tag_name("img").get_attribute("src"));

    # 获取分类及分类下科目列表
    def test_get_type_subject_list(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/");
        course_Left = driver.find_elements_by_xpath("//div[@class='courseBox']/div[@class='course']")
        for course_type in course_Left:

            subject_list = course_type.find_elements_by_xpath("div[@class='courseRight']/div[@class='subjectlist']/a");
            for subject in subject_list:
                subject_name = subject.text;
                print("科目名称：" + subject_name);
                assert subject_name is not None, "科目名称不能为空";
                subject_href = subject.get_attribute("href");
                print("科目对应的地址：" + subject_href);
                assert subject_name is not None, "科目名称不能为空";

    # 获取分类下的课程信息
    def test_get_type_course_list(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/");
        course_Left = driver.find_elements_by_xpath("//div[@class='courseBox']/div[@class='course']")
        for course_type in course_Left:
            print("--------------------------------------------");
            print("分类下的课程课程详情")
            course_list = course_type.find_elements_by_xpath(
                "div[@class='courseRight']/ul[@class='subjectinfo']/li[@class='shadow']");
            for course in course_list:
                print(course.find_element_by_tag_name("a").get_attribute("href"));
                print(course.find_element_by_xpath("a/*").text);
                watch = course.find_element_by_xpath(
                    "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='watch']/span[2]")
                print(watch.text);
                assert watch.text is not None, "观看次数不能为空";

                like = course.find_element_by_xpath(
                    "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='like']/span[2]")
                print(like.text);
                assert like.text is not None, "收藏次数不能为空";

                organ_name = course.find_element_by_xpath("div[@class='organ']/span[@class='organName']")
                print(organ_name.text);
                assert organ_name.text is not None, "收藏次数不能为空";

    def tearDown(self):
        self.driver.close()
