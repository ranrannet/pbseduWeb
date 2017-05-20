# coding=utf-8
import os
import unittest

from selenium import webdriver
from urllib import request
import util_interface
from vo.course_detail_vo import course_detail_vo
from vo.hot_word import hot_word
from time import sleep
import config

#课程详情
class test_detail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    # 获取课程详情
    def test_course_detail(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/newWeb/courseDetails.php?courseId=HSNVC470&schoolId=HSNSW003");
        cour_img = driver.find_element_by_xpath("//div[@class='courseImg']/img[@*]");
        # 课程图片的Url
        course_image = cour_img.get_attribute("src");
        status = util_interface.get_url_isexist(course_image);
        assert status == config.URL_SUCCESS_CODE, "课程图片地址不存在";

        # 课程名称
        course_name = driver.find_element_by_xpath("//div[@class='coursefont']/h1[@class='title']");
        assert course_name.text is not None, "课程名称不能为空";

        # 观看次数
        watch_num = driver.find_element_by_xpath(
            "//div[@class='numinfo clearfix']/div[@class='watch']/span[@class='watchNum']")
        assert watch_num.text is not None, "观看次数不能为空";

        # 点赞次数
        like_num = driver.find_element_by_xpath(
            "//div[@class='numinfo clearfix']/div[@class='like']/span[@class='likenum']")
        assert like_num.text is not None, "收藏次数不能为空";

        # 科目类别
        course_type = driver.find_element_by_xpath("//div[@class='courseClass clearfix']/div[1]/span[2]");
        assert course_type.text is not None, "所属机构不能为空";

        # 课件总数
        course_ware_count = driver.find_element_by_xpath("//div[@class='courseClass clearfix']/div[2]/span[2]");
        assert course_ware_count.text is not None, "课件总数不能为空";
        ware_count = int(course_ware_count.text);

        # 课程简介
        course_summary = driver.find_element_by_xpath("//div[@class='DetailsLeft']/div[@class='courseIntr']/p[1]")
        print(course_summary.text)
        assert course_summary.text is not None, "课程简介不能为空";


        # 遍历检查课件
        course_ware_list = driver.find_elements_by_xpath("//div[@class='courseDire']/ul[@class='playList']")
        self.check_course_ware_list(course_ware_list)

        # 播放全部
        play = driver.find_element_by_xpath(
            "//div[@class='content']/div[@class='courseinfo']/div[@class='info clearfix']/div[@class='userClick']/a[1]")
        play_link = play.get_attribute("href");
        print(play_link);

        # 续费VIP视频
        pay_btn = driver.find_element_by_xpath("//div[@class='info clearfix']/div[@class='userClick']/a[2]")
        pay_link = pay_btn.get_attribute("href");
        print(pay_link);





    # 遍历检查课件
    def check_course_ware_list(self, course_ware_list):
        for course_ware in course_ware_list:
            contact_a = course_ware.find_elements_by_tag_name("li");
            for a_tag in contact_a:
                is_free = a_tag.get_attribute("class");
                print(is_free);
                print(a_tag.find_element_by_tag_name("a").text);
                print(a_tag.find_element_by_tag_name("a").get_attribute("href"));
                print(a_tag.find_element_by_xpath("a/span/i").text);
                em = a_tag.find_element_by_xpath("a/span");
                if "免费" in em.text:
                    print(a_tag.find_element_by_xpath("a/span/em").text);

    # 热门课程遍历
    def test_check_hot_course_list(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/newWeb/courseDetails.php?courseId=HSNVC470&schoolId=HSNSW003");
        hot_course_list = driver.find_elements_by_xpath("//ul[@class='hotCourse subjectinfo']/li");
        for hot_course in hot_course_list:
            course_link = hot_course.find_element_by_tag_name("a").get_attribute("href");
            assert course_link is not None,"课程详情地址不能为空";

            course_name = hot_course.find_element_by_xpath("a/*").text;
            assert course_name is not None,"课程名称不能为空";

            watch = hot_course.find_element_by_xpath(
                "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='watch']/span[2]")
            print(watch.text);
            assert watch.text is not None,"观看数量不能为空";

            like = hot_course.find_element_by_xpath(
                "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='like']/span[2]")
            print(like.text);
            assert like.text is not None,"收藏课程数量不能为空";

            organ_name = hot_course.find_element_by_xpath("div[@class='organ clearfix']/span[@class='organName']")
            print(organ_name.text);
            assert organ_name.text is not None,"机构名称不能为空";



            # 获取课程详情

    def get_course_detail_vo(self):
        driver = self.driver
        driver.get("http://www-sit.pbsedu.com/newWeb/courseDetails.php?courseId=HSNVC470&schoolId=HSNSW003");
        cour_img = driver.find_element_by_xpath("//div[@class='courseImg']/img[@*]");
        # 课程图片的Url
        course_image = cour_img.get_attribute("src");

        # 课程名称
        course_name = driver.find_element_by_xpath("//div[@class='coursefont']/h1[@class='title']").text;

        # 观看次数
        watch_num = driver.find_element_by_xpath(
            "//div[@class='numinfo clearfix']/div[@class='watch']/span[@class='watchNum']").text;

        # 点赞次数
        like_num = driver.find_element_by_xpath(
            "//div[@class='numinfo clearfix']/div[@class='like']/span[@class='likenum']").text;

        # 科目类别
        course_type = driver.find_element_by_xpath("//div[@class='courseClass clearfix']/div[1]/span[2]").text;

        # 课件总数
        course_ware_count = driver.find_element_by_xpath("//div[@class='courseClass clearfix']/div[2]/span[2]").text;

        # 课程简介
        course_summary = driver.find_element_by_xpath("//div[@class='DetailsLeft']/div[@class='courseIntr']/p[1]").text;

        course_detail =course_detail_vo(course_image,course_name,watch_num,like_num,course_type,course_ware_count,course_summary);
        return course_detail;



    def tearDown(self):
        self.driver.close()
        self.driver.quit()

