# -*- coding: utf-8 -*-
import scrapy
import re
import time
from webUrlGetor.settings import *
from webUrlGetor.items import WeburlgetorItem
import requests
import urllib3
import sys
import random
from webUrlGetor.tools.model.sqltools import SQLTools

urllib3.disable_warnings()
user_agent = random.choice(USER_AGENT_LIST)
headers = {
    'User-Agent': user_agent,
}


class CchinaSpider(scrapy.Spider):
    name = "c"
    pid_list = []
    allowed_domains = ["chan.sankakucomplex.com"]
    start_urls = ['https://chan.sankakucomplex.com/?tags=' + str(tags)]
    SQLTools = SQLTools()
    dirs = os.path.join(IMAGES_STORE, tags)
    if not os.path.exists(dirs):
        try:
            os.makedirs(dirs)
        except Exception as e:
            print(e)
    print("图片存储位置-->", dirs)

    def parse(self, response):
        time.sleep(random.randint(5, 10))
        sel = scrapy.Selector(text=response.body)

        deep_links = sel.xpath("//span[contains(@class,'thumb')]").extract()
        for deep_link in deep_links:
            pattern = re.compile(r'id="p[0-9]+"')
            result1 = pattern.findall(deep_link)
            id_of = result1[0].split("=")[1][2:-1]
            print("id_of--->" + str(id_of))

            new_http = "https://chan.sankakucomplex.com/post/show/" + str(id_of)
            yield scrapy.Request(new_http, callback=self.parse2, dont_filter=False)

        next_page_pre = scrapy.Selector(text=response.body)
        next_pages = next_page_pre.xpath("//link[@rel='next']/@href").extract()
        print("next_pages-->", next_pages)

        no_page = sel.xpath("//div[@class='post-content-notification']").extract()
        if len(no_page) > 0:
            sys.exit("Done!")

        if len(next_pages) > 0:
            for next_page_new in next_pages:
                pattern = re.compile(r'page=\d+')  # 查找数字
                result1 = pattern.findall(next_page_new)
                next_page_url = self.start_urls[0] + "&" + str(result1[0])
                print("next_page_url--->" + str(next_page_url))
                yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=False)

    def parse2(self, response):
        time.sleep(random.randint(5, 10))
        sel = scrapy.Selector(text=response.body)
        deep_links = sel.xpath("//*[@id=\"image-link\"]/@href").extract()
        if len(deep_links) > 0:
            for item in deep_links:
                file_name_pre = item.split("?")[0]
                file_name = str(file_name_pre.split("/")[-1:][0])
                path = os.path.join(self.dirs, file_name)
                url = "https:" + str(item)

                if os.path.exists(path):
                    print("file exit in path")
                elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                    print("file exit in db")
                else:
                    try:
                        time.sleep(1)
                        if not url.startswith("http"):
                            url = "https:" + url
                        res = requests.get(url, timeout=18000, verify=False, headers=headers)
                        print("tags--->" + str(tags))
                        print("pic_url-->", url)
                        with open(path, 'wb') as f:
                            f.write(res.content)
                        print("保存成功！文件名为%s" % file_name)
                        self.SQLTools.insert_into_new_db(file_name, tags)
                        time.sleep(random.randint(3, 7))
                    except:
                        pass

        else:
            print("deep_link is None")
            sample_links = sel.xpath("//*[@id=\"post-content\"]//img/@src").extract()
            video_links = sel.xpath("//*[@id=\"post-content\"]//video/@src").extract()
            if len(video_links) > 0:
                for video_link in video_links:
                    sample_links.append(video_link)
            if len(sample_links) == 0:
                print("sample_links is also None", sample_links)
                print("URL--->", response.url)
            for sample_link in sample_links:
                file_name_pre = sample_link.split("?")[0]
                file_name = str(file_name_pre.split("/")[-1:][0])
                path = os.path.join(self.dirs, file_name)
                url = "https:" + str(sample_link)
                if os.path.exists(path):
                    print("file exit in path")
                elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                    print("file exit in db")
                else:
                    try:
                        time.sleep(1)
                        if not url.startswith("http"):
                            url = "https:" + url
                        res = requests.get(url, timeout=18000, verify=False, headers=headers)
                        print("tags--->" + str(tags))
                        print("pic_url-->", url)
                        with open(path, 'wb') as f:
                            f.write(res.content)
                        print("保存成功！文件名为%s" % file_name)
                        self.SQLTools.insert_into_new_db(file_name, tags)
                        time.sleep(random.randint(3, 5))
                    except:
                        pass
