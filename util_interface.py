# coding=utf-8
from urllib import request, parse


def get_url_isexist(pic_url):
    try:
        response = request.urlopen(pic_url, timeout=3)
        httpCode = response.getcode()
    except Exception as e:
        return 0;
    return httpCode;


def test_calculate_page(self, total_count, one_page_count):
    # total_count = 42;
    print(int(total_count / one_page_count));
    print(int(total_count % one_page_count));

    pagesize = int(total_count / one_page_count);
    pagesize_other = int(total_count % one_page_count);
    if (total_count > 0 and pagesize == 0):
        pagesize = 1;
    else:
        if (pagesize != 0):
            if (pagesize_other > 0):
                pagesize = pagesize + 1;

    print("条数：" + str(total_count) + "总页数" + str(pagesize));
    return pagesize;
