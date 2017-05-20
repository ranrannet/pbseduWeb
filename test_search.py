# coding=utf-8
import os
import unittest

from selenium import webdriver
import util_interface
from vo.hot_word import hot_word
from time import sleep


class test_search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def fixed_select_course(self):
        driver = self.driver
        driver.get("http://www.pbsedu.com/");
        list = [];
        search_hotword_list = driver.find_elements_by_xpath("//div[@class='seach']/div[@class='hotword']/a");
        for search_hotword in search_hotword_list:
            search_url = search_hotword.get_attribute("href");
            print(search_url);
            print(search_hotword.text);
            hot_word_vo = hot_word(search_hotword.text, search_url);
            list.append(hot_word_vo);

        print(len(list));
        return list;

    # 搜索指定搜索词语（故事 英语 奥数 同步 七年级 八年级）
    def test_test_fixed_select_course(self):
        hot_word_list = self.fixed_select_course();
        for hot_word in hot_word_list:
            print("url ============" + hot_word.hot_word)
            driver = self.driver
            self.driver.get(hot_word.hot_word_url);
            search_key_word = driver.find_element_by_xpath(
                "//div[@class='searchKeywords']/span[@class='SearchElements']/span[@class='keywords']").text;
            self.assertEqual(search_key_word, hot_word.hot_word, "关键词不一致")
            print_search_count = driver.find_element_by_xpath(
                "//span[@class='searchResult']/span[@class='searchData']").text;
            print(print_search_count);
            page_size = util_interface.test_calculate_page(self, int(print_search_count), 20);
            if (len(print_search_count) > 0):
                for i in range(page_size):
                    print("index--------" + str(i));
                    print(hot_word.hot_word + "page_size:--------" + str(i));
                    if page_size > 0:
                        next_page = driver.find_element_by_xpath(
                            "//a[@class='num pnm'][last()]");
                        if (next_page is not None and i != 0):
                            next_page.click();
                            sleep(3)  # 强制等待3秒再执行下一步
                        search_course_list = driver.find_elements_by_xpath(
                            "//ul[@class='subjectinfo choosesortInfo clearfix']/li[@class='shadow']")
                        search_count = len(search_course_list)
                        print(search_count);
                        for search_course in search_course_list:
                            print(search_course.text);
                            print(search_course.find_element_by_tag_name("a").get_attribute("href"));
                            course_name = search_course.find_element_by_xpath("a/*").text;
                            print(course_name);
                            self.assertIn(hot_word.hot_word, course_name, "课程中不包含关键词");
                            organ_name = search_course.find_element_by_xpath(
                                "div[@class='organ']/span[@class='organName']").text;
                            assert organ_name is not None, "机构名称不能为空";


    # 根据关键词进行搜索
    def test_select_course(self):
        driver = self.driver
        search_key_word = "爱的初体验";
        driver.get("http://www-sit.pbsedu.com/");
        driver.find_element_by_xpath("//input[@class='inputEntry']").send_keys(search_key_word);
        driver.find_element_by_xpath("//input[@class='inputClick']").click();
        sleep(3)  # 强制等待3秒再执行下一步
        print_search_count = driver.find_element_by_xpath(
            "//span[@class='searchResult']/span[@class='searchData']").text;
        print(print_search_count);
        search_course_list = driver.find_elements_by_xpath(
            "//ul[@class='subjectinfo choosesortInfo clearfix']/li[@class='shadow']")
        search_count = len(search_course_list)
        assert int(print_search_count) == search_count, "实际搜索结果与总结果不一致";
        for search_course in search_course_list:
            print(search_course.find_element_by_tag_name("a").get_attribute("href"));
            print(search_course.find_element_by_xpath("a/*").text);
            course_name = search_course.find_element_by_xpath("a/*").text;
            watch_count = search_course.find_element_by_xpath(
                "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='watch']/span[2]").text;
            assert int(watch_count) is not None, "观看次数不能为空";
            like_count = search_course.find_element_by_xpath(
                "div[@class='subjectImg']/div[@class='imgFloat']/div[@class='like']/span[2]").text;
            assert int(like_count) is not None, "点赞次数不能为空";

            organ_name = search_course.find_element_by_xpath(
                "div[@class='organ']/span[@class='organName']").text;
            assert organ_name is not None, "机构名称不能为空";
            self.assertIn(search_key_word, course_name, "课程中不包含关键词");


    def tearDown(self):
        self.driver.close()
