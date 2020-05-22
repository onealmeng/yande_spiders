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
    name = "d"
    allowed_domains = ["danbooru.donmai.us"]
    start_urls = ['https://danbooru.donmai.us/posts?tags=' + str(tags)]
    SQLTools = SQLTools()
    dirs = os.path.join(IMAGES_STORE, tags)
    if not os.path.exists(dirs):
        try:
            os.makedirs(dirs)
        except Exception as e:
            print(e)
    print("Pic Save Path-->", dirs)

    def parse(self, response):
        time.sleep(5)
        item = WeburlgetorItem()
        sel = scrapy.Selector(text=response.body)
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        result1 = pattern.findall(response.text)
        print(result1)

        for item in result1:
            if "preview" in item or "logo" in item or "pixiv" in item or "pximg" in item or "sample" in item or "crop" in item:
                pass
            elif not (item.endswith(".png") or item.endswith(".jpg")):
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
                        print("Save Success!Save Path-->%s" % file_name)
                        self.SQLTools.insert_into_new_db(file_name, tags)
                    except:
                        pass

        links_in_a_page = sel.xpath('//a[@href]')  # 页面内的所有链接
        for link_sel in links_in_a_page:
            print("page-->", str(result1[0]))
            aa = link_sel.re('href="(.*?)"')
            for i in range(0, len(aa)):
                link = str(aa[i])  # 每一个url
                if link.startswith("https://danbooru.donmai.us") and (link.endswith(".png") or link.endswith(".jpg")):
                    if "File/" not in link and "preview" not in link:
                        file_name = str(link.split("/")[-1:][0])
                        path = os.path.join(self.dirs, file_name)

                        if os.path.exists(path):
                            pass
                        elif len(self.SQLTools.query_from_UserNew_more_info(file_name)) > 0:
                            pass
                        else:
                            try:
                                time.sleep(1)
                                res = requests.get(link, timeout=180, verify=False)
                                img = res.content
                                print(tags)
                                print("link-->", link)
                                with open(path, 'wb') as f:
                                    f.write(img)
                                f.close()
                                print("保存成功！文件名为%s" % file_name)
                                self.SQLTools.insert_into_new_db(file_name, tags)
                            except:
                                pass
                        yield item
        next_page = scrapy.Selector(text=response.body)
        next_page = next_page.xpath("//a[@rel='next' and @id='paginator-next']").extract_first()
        if next_page:
            pattern = re.compile(r'\d+')  # 查找数字
            result1 = pattern.findall(next_page)
            print("Next page-->", str(result1[0]))
            next_page_url = self.start_urls[0] + "&page=" + str(result1[0])
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
        else:
            sys.exit(str(tags) + "D站爬取完成！")
