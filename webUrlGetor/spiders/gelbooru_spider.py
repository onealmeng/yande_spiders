# -*- coding: utf-8 -*-
import scrapy
import re
import time
from webUrlGetor.settings import *
from webUrlGetor.items import WeburlgetorItem
import requests
import urllib3
import sys
from webUrlGetor.tools.model.sqltools import SQLTools

urllib3.disable_warnings()


class ScrapyOschinaSpider(scrapy.Spider):
    name = "g"
    pid_list = []
    allowed_domains = ["gelbooru.com"]
    start_urls = ['https://gelbooru.com/index.php?page=post&s=list&tags=' + str(tags)]
    SQLTools = SQLTools()
    dirs = os.path.join(IMAGES_STORE, tags)
    if not os.path.exists(dirs):
        try:
            os.makedirs(dirs)
        except Exception as e:
            print(e)
    print("图片存储位置-->", dirs)

    def parse(self, response):
        time.sleep(5)
        item = WeburlgetorItem()
        sel = scrapy.Selector(text=response.body)

        deep_links = sel.xpath("//a[contains(@href,'//gelbooru.com/index.php?page=post&s=view&id=')]").extract()
        for deep_link in deep_links:
            pattern = re.compile(r'id="p[0-9]+"')
            result1 = pattern.findall(deep_link)
            id_of = result1[0].split("=")[1][2:-1]

            new_http = "https://gelbooru.com/index.php?page=post&s=view&id=" + str(id_of) + "&tags=" + tags
            yield scrapy.Request(new_http, callback=self.parse2, dont_filter=False)

            next_page_pre = scrapy.Selector(text=response.body)
            next_pages = next_page_pre.xpath("//a[contains(@href,'?page=post&s=list&tags=')]").extract()
            print("next_page-->", next_pages)
            next_pages_new = []
            for next_page in next_pages:
                if "pid" in next_page:
                    next_pages_new.append(next_page)

            if len(next_pages_new) > 0:
                for next_page_new in next_pages_new:
                    pattern = re.compile(r'pid=\d+')  # 查找数字
                    result1 = pattern.findall(next_page_new)
                    next_page_url = self.start_urls[0] + "&" + str(result1[0])
                    self.pid_list.append(next_page_url)
                    yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=False)

    def parse2(self, response):
        time.sleep(5)
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        result1 = pattern.findall(response.text)

        for item in result1:
            if not item.startswith("https://img2.gelbooru.com/images") or item.startswith(
                    "https://files.yande.re/image/"):
                pass
            elif not (item.endswith(".png") or item.endswith(".jpg") or item.endswith(".gif")):
                pass
            elif "samples" in item:
                pass
            else:
                file_name = str(item.split("/")[-1:][0])
                path = os.path.join(self.dirs, file_name)

                if os.path.exists(path):
                    pass
                elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                    pass
                else:
                    try:
                        time.sleep(1)
                        res = requests.get(item, timeout=180, verify=False)
                        img = res.content
                        print(tags)
                        print("pic_link_png-->", item)
                        with open(path, 'wb') as f:
                            f.write(img)
                        f.close()
                        print("保存成功！文件名为%s" % file_name)
                        self.SQLTools.insert_into_new_db(file_name, tags)
                    except:
                        pass
