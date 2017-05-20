class course_detail_vo:
    course_image = "";
    course_name = '';
    watch_num = 0;
    like_num = 0;
    course_type = '';
    course_ware_count = 0;
    course_summary = '';

    def __init__(self, course_image, course_name, watch_num, like_num, course_type, course_ware_count, course_summary):
        self.course_image = course_image;
        self.course_name = course_name;
        self.watch_num = watch_num;
        self.like_num = like_num;
        self.course_type = course_type;
        self.course_ware_count = course_ware_count;
        self.course_summary = course_summary;


