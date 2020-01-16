# -*- coding: utf-8 -*-
import os
from webUrlGetor.tools.model.sqltools import SQLTools
from webUrlGetor.tools.NoDuplicate import *
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class XX(object):
    SQLTools = SQLTools()
    SavePic = SavePic()

    def get_local_file_md5(self, file_path):
        file_name_list = self.SavePic.get_file_name_list_from_path(file_path)
        tag = os.path.split(file_path)[1]
        print "tag-->", tag
        need_d_list = []
        for file_name in file_name_list:
            res = self.SQLTools.query_from_UserNew_more_info(file_name)
            if len(res) == 0:
                self.SQLTools.insert_into_new_db(str(file_name),tag)
                print "插入成功"
            else:
                print "目标已经存在！"
                print res[0].fileName
                need_d_list.append(os.path.join(file_path, file_name))
                print need_d_list

    def file_name(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            return dirs  # 当前路径下所有子目录


if __name__ == '__main__':
    x = XX()

    img_path = "/Users/dingtone/Downloads/图片待处理"
    img_info = x.file_name(img_path)

    print img_info
    for i in range(0, len(img_info)):
        print "当前对比的文件夹", img_info[i]
        print "当前处理文件夹个数", i
        file_pa = os.path.join(img_path, img_info[i])
        x.get_local_file_md5(file_pa)
