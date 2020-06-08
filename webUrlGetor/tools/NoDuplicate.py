# -*- coding:utf-8 -*-
from PIL import Image
from PIL import ImageFile
import sys
import os
import argparse

ImageFile.LOAD_TRUNCATED_IMAGES = True

parser = argparse.ArgumentParser()
parser.add_argument('app_name', help='Specify test app')


class SavePic(object):

    def __init__(self):
        self.like = float(0.95)  # 删除阈值，高于这个相似度的图片会删除大小较小的一个
        self.accuracy = ".8f"  # 计算 两张图片相似度时，精确到小数点后几位

    def getGray(self, image_file):
        tmpls = []
        for h in range(0, image_file.size[1]):  # h
            for w in range(0, image_file.size[0]):  # w
                tmpls.append(image_file.getpixel((w, h)))

        return tmpls

    def getAvg(self, ls):  # 获取平均灰度值
        return sum(ls) / len(ls)

    def getImgHash(self, fne):
        Image.MAX_IMAGE_PIXELS = None
        image_file = Image.open(fne)  # 打开
        image_file = image_file.resize((480, 480))  # 重置图片大小我12px X 12px
        image_file = image_file.convert("L")  # 转256灰度图
        Grayls = self.getGray(image_file)  # 灰度集合
        avg = self.getAvg(Grayls)  # 灰度平均值
        bitls = ''  # 接收获取0或1
        # 除去变宽1px遍历像素
        for h in range(1, image_file.size[1] - 1):  # h
            for w in range(1, image_file.size[0] - 1):  # w
                if image_file.getpixel((w, h)) >= avg:  # 像素的值比较平均值 大于记为1 小于记为0
                    bitls = bitls + '1'
                else:
                    bitls = bitls + '0'
        return bitls

    def getMH(self, a, b):  # 比较100个字符有几个字符相同
        dist = 0
        for i in range(0, len(a)):
            if a[i] == b[i]:
                dist = dist + 1
        dist_done = format(float(dist) / float(len(a)), self.accuracy)
        return dist_done

    def compare_pic_hash(self, hash_a, hash_b):
        """
        :param hash_a: 图片A的hash
        :param hash_b: 图片b的hash
        :return:
        """
        compare = self.getMH(hash_a, hash_b)
        return compare

    def get_file_name_list_from_path(self, file_path):
        """
        :return:
        """
        file_name_list = []
        for file_name in os.listdir(file_path):
            if os.path.getsize(os.path.join(file_path,
                                            file_name)) < 102400 or "File" in file_name or "index.php" in file_name \
                    or "?f_shash" in file_name:
                try:
                    os.remove(os.path.join(os.path.join(file_path, file_name)))
                except Exception as e:
                    print "删除失败，原因：", str(e)
            else:
                if not (os.path.split(file_name)[1].endswith(".jpg") or os.path.split(file_name)[1].endswith(".png")):
                    pass
                else:
                    file_name_list.append(file_name)

        return file_name_list

    def get_file_hash_list_from_file_name_list(self, file_path, file_name_list):
        """
        :return:
        """
        file_hash_list = []
        try:
            for i in range(0, len(file_name_list)):
                hash_of_file = self.getImgHash(os.path.join(file_path, file_name_list[i]))
                file_hash_list.append(hash_of_file)
                self.view_bar(i, len(file_name_list))
        except Exception as e:
            print "获取文件hash错误！", str(e)
        return file_hash_list

    def getDocSize(self, path):
        try:
            size = os.path.getsize(path)
            return size
        except Exception as err:
            print(err)

    def view_bar(self, num, total):
        rate = float(num) / total
        rate_num = int(rate * 100) + 1
        r = '\r[%s%s]%d%%' % ("#" * rate_num, " " * (100 - rate_num), rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush()

    def compare_pic_hash_list(self, file_hash_list, file_path, file_name_list):
        """

        :param file_name_list:
        :param file_path:
        :param file_hash_list:
        :return:
        """
        if len(file_name_list) != len(file_hash_list):
            sys.exit("hash list 与 file list下标不一致！")
        total = (len(file_name_list) * (len(file_name_list) - 1)) / 2
        print "\n共需要对比", total
        need_delete_list_file_name = []
        count = 0
        for i in range(0, len(file_hash_list)):
            for j in range(i + 1, len(file_hash_list)):
                compare = self.compare_pic_hash(file_hash_list[i], file_hash_list[j])
                if float(compare) - float(self.like) > 0:
                    file_i_size = self.getDocSize(os.path.join(file_path, file_name_list[i]))
                    file_j_size = self.getDocSize(os.path.join(file_path, file_name_list[j]))
                    if file_i_size - file_j_size > 0:
                        need_delete_list_file_name.append(file_name_list[j])
                        break
                    else:
                        need_delete_list_file_name.append(file_name_list[i])
                        continue
                count = count + 1
                self.view_bar(count, total)

        news_ids = []
        for need_delete_file_path in need_delete_list_file_name:
            if need_delete_file_path not in news_ids:
                news_ids.append(need_delete_file_path)
        print "\n去重后的需要删除的长度", len(news_ids)

        return news_ids

    def delete_file(self, file_path, need_delete_list_file_name):
        """

        :return:
        """
        for need_delete_file_name in need_delete_list_file_name:
            try:
                os.remove(os.path.join(file_path, need_delete_file_name))
            except Exception as e:
                print "删除失败，原因：", str(e)

    def main(self, file_path):
        """
        aa
        :return:
        """
        # 获取所有文件的文件名，放入list
        # 获取所有文件的hash    多线程
        # 对比文件hash值
        # 如果hash值相似度大于95%
        # 删小留大，否则pass 将需要删除的文件放入 待删除list
        # 单线程删除文件
        file_path = self.rename_path_start(file_path)
        file_name_list = self.get_file_name_list_from_path(file_path)
        print "文件夹下共包含文件", len(file_name_list), "个"
        file_hash_list = self.get_file_hash_list_from_file_name_list(file_path, file_name_list)
        need_delete_list_file_name = self.compare_pic_hash_list(file_hash_list, file_path, file_name_list)
        need_delete_list_file_name_new = []
        for item in need_delete_list_file_name:
            if "uncensored" not in item:
                need_delete_list_file_name_new.append(item)
        self.delete_file(file_path, need_delete_list_file_name_new)
        self.rename_path(file_path)
        return need_delete_list_file_name_new

    def file_name(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            return dirs  # 当前路径下所有子目录

    def rename_path(self, file_path):
        try:
            os.rename(file_path, file_path + "_ndDone")
        except Exception as e:
            print e
            print file_path, 'rename dir fail\r\n'
        else:
            print file_path, 'rename dir success\r\n'

    def rename_path_start(self, file_path):
        try:
            new_path = file_path + "_ndStart"
            os.rename(file_path, new_path)

        except Exception as e:
            print e
            print file_path, 'rename dir fail\r\n'
        else:
            print file_path, 'rename dir success\r\n'
            return new_path


if __name__ == '__main__':
    x = SavePic()
    parser = argparse.ArgumentParser()
    parser.add_argument('floderName', help='floderName')
    parser.add_argument('-z', '--zip', action='store', dest='zip_file', default='1',
                        help='need zpied')
    parser.add_argument('-a', '--adb', action='store', dest='adb_push', default='0',
                        help='need zpied')
    args = parser.parse_args()
    print args.floderName
    print args.zip_file
    print args.adb_push
    # now_dir = os.path.dirname(os.path.abspath(__file__))
    # project_dir = os.path.split(now_dir)[0]
    # img_path = os.path.join(project_dir, "images")
    # img_info = x.file_name(img_path)
    img_path = "/Users/dingtone/PycharmProjects/yande_spiders/webUrlGetor/images"

    # print img_info
    # for i in range(0, len(img_info)):奥
    #     print "当前对比的文件夹", img_info[i]
    #     for j in range(0, 3):
    #         print "正在进行的去重次数", i
    #         file_patha = os.path.join(img_path, img_info[i])
    #         need_delete_list_file_namemikagami_mamizu = x.main(file_patha)
    #         if len(need_delete_list_file_name) == 0:
    #             break
    floderName = args.floderName
    file_patha = os.path.join(img_path, floderName)
    need_delete_list_file_name = x.main(file_patha)
    floderName_new = floderName + "_ndStart_ndDone"
    print floderName_new
    if args.zip_file =='1':
        cd_cmd = 'cd ' + str(img_path)
        zipcmd = 'zip -rj %s.zip %s/' % (floderName_new, floderName_new)
        mv_cmd = 'mv ./%s.zip /Users/dingtone/Downloads/pic_need_to/%s.zip' % (floderName_new, floderName)
        delete_cmd = 'rm -rf %s' % floderName_new
        all_cmd = cd_cmd + "&&" + zipcmd + "&&" + mv_cmd + "&&" + delete_cmd
        os.system(all_cmd)

    if args.adb_push =='1':
        cmd_adb='adb push '+ '/Users/dingtone/Downloads/pic_need_to/%s.zip'%floderName + " /sdcard/ACG图片"
        print cmd_adb
        os.system(cmd_adb)

    print "去重完成！"
