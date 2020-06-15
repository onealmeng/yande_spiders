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
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
    # 'cache-control': 'no-cache',
    # 'cookie': 'forum_post_last_read_at=%222020-06-04T18%3A21%3A35.710%2B09%3A00%22; country=US; vote=1; yande.re=Yml2U0c5amNwUFMya2NGblBZYWZka0FGRFkwVXRobCs4aWYvZ0czNGRvTlRLQUVvWmxKd254MFNUcnpMVVptSSt1VWlIR2tBdlRiMnVJMmlYN2dXeVh2cjhuNFA3dTBOVlU3eXVvSkthM3BHMVdiWkhER0ZTNlhtTmlySnNNSzNLQTgvU2xld2tzRGQ1bG1HQTRVMmFBPT0tLVVuMzJldDB6L1h3Tmdjb2oyK0hvU3c9PQ%3D%3D--3513325308b38cdbf70f60a6391a0b7f6b8d6c28; __utma=5621947.1728659374.1591262501.1591262501.1591262501.1; __utmc=5621947; __utmz=5621947.1591262501.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=5621947.1.10.1591262501',
    # 'pragma': 'no-cache',
    # 'referer': 'https://yande.re/post',
    # 'sec-fetch-dest': 'document',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-site': 'sec-fetch-site',
    # 'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1'

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
            print "id_of--->", id_of

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
                print "next_page_url--->" + str(next_page_url)
                yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=False)

    def parse2(self, response):
        time.sleep(random.randint(5, 10))
        sel = scrapy.Selector(text=response.body)
        deep_links = sel.xpath("//*[@id=\"image-link\"]/@href").extract()
        print "deep_links--->", deep_links

        if len(deep_links) > 0:
            for item in deep_links:
                file_name_pre = item.split("?")[0]
                file_name = str(file_name_pre.split("/")[-1:][0])
                path = os.path.join(self.dirs, file_name)
                url = "https:" + str(item)

                if os.path.exists(path):
                    print ("file exit in path")
                elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                    print ("file exit in db")
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
            print "deep_link is None"
            sample_links = sel.xpath("//*[@id=\"post-content\"]//img/@src").extract()
            video_links = sel.xpath("//*[@id=\"post-content\"]//video/@src").extract()
            if len(video_links) > 0:
                for video_link in video_links:
                    sample_links.append(video_link)
            if len(sample_links) == 0:
                print "sample_links is also None", sample_links
                print "URL--->", response.url
            for sample_link in sample_links:
                file_name_pre = sample_link.split("?")[0]
                file_name = str(file_name_pre.split("/")[-1:][0])
                path = os.path.join(self.dirs, file_name)
                url = "https:" + str(sample_link)
                print "path---->", path

                if os.path.exists(path):
                    print ("file exit in path")
                elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                    print ("file exit in db")
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


