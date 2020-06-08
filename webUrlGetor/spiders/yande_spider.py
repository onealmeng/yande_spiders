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
import random

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
urllib3.disable_warnings()


class ScrapyOschinaSpider(scrapy.Spider):
    name = "y"
    allowed_domains = ["yande.re", "files.yande.re"]
    start_urls = ['https://yande.re/post?tags=' + str(tags)]
    # start_urls = ['https://yande.re/tag?name=azur_lane&type=&order=date&commit=Search']
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
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        result1 = pattern.findall(response.text)
        print(result1)

        for item in result1:
            if "preview" in item or "logo" in item or "pixiv" in item or "pximg" in item or "sample" in item \
                    or "screen" in item or "Fichier:" in item:
                pass
            elif not (item.endswith(".png") or item.endswith(".jpg")):
                pass
            # elif "uncensored" not in item:
            #     pass
            else:
                file_name = str(item.split("/")[-1:][0])
                path = os.path.join(self.dirs, file_name)

                if os.path.exists(path):
                    pass
                elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                    pass
                else:
                    try:
                        time.sleep(random.randint(1, 5))
                        res = requests.get(item, timeout=1809, verify=False, headers=headers)
                        img = res.content
                        print(tags)
                        print("pic_link_png-->", item)
                        with open(path, 'wb') as f:
                            f.write(img)
                        print("保存成功！文件名为%s" % file_name)
                        self.SQLTools.insert_into_new_db(file_name, tags)
                    except:
                        pass
                time.sleep(1)

        links_in_a_page = sel.xpath('//a[@href]')  # 页面内的所有链接
        for link_sel in links_in_a_page:
            print("page-->", str(result1[0]))
            aa = link_sel.re('href="(.*?)"')
            for i in range(0, len(aa)):
                link = str(aa[i])  # 每一个url
                if link.startswith("https://files.yande.re") and "Fichier:" not in link and "screen" not in link and (
                        link.endswith(".png") or link.endswith(".jpg")):
                    file_name = str(link.split("/")[-1:][0])
                    path = os.path.join(self.dirs, file_name)

                    if os.path.exists(path):
                        pass
                    elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                        pass
                    # elif "uncensored" not in link:
                    #     pass
                    else:
                        try:
                            time.sleep(random.randint(1,5))
                            res = requests.get(link, timeout=1809, verify=False, headers=headers)
                            img = res.content
                            print(tags)
                            print("link-->", link)
                            with open(path, 'wb') as f:
                                f.write(img)
                            print("保存成功！文件名为%s" % file_name)
                            self.SQLTools.insert_into_new_db(file_name, tags)
                        except:
                            pass
                    yield item
        next_page = scrapy.Selector(text=response.body)
        next_page = next_page.xpath("//a[@class='next_page' and @rel='next']").extract_first()
        if next_page:
            pattern = re.compile(r'\d+')  # 查找数字
            result1 = pattern.findall(next_page)
            print("Next page-->", str(result1[0]))
            # if "page=" not in self.start_urls[0]:
            next_page_url = self.start_urls[0] + "&page=" + str(result1[0])
            # else:
            #     url_pre = self.start_urls[0].split("&")
            #     next_page_url = url_pre[0] + "page=" + str(result1[0])
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
        else:
            sys.exit(str(tags) + "Y站爬取完成！")
