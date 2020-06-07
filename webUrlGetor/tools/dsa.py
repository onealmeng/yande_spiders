import requests
import re
from webUrlGetor.settings import *
import random
from webUrlGetor.tools.model.sqltools import SQLTools
import os
import time

SQLTools = SQLTools()


def search(cover_path):
    UserAgent = random.choice(USER_AGENT_LIST)
    done_list = []
    headers = {
        "User-Agent": UserAgent,
        "Host": "saucenao.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",

    }
    files = {'file': open(cover_path, 'rb')}
    url = "https://saucenao.com/search.php"
    res = requests.post(url=url, files=files, headers=headers)

    print("httpCode:" + str(res.status_code))
    if res.status_code != 200:
        return "error"
    # print(res.text)
    pattern = re.compile(r'Creator: </strong>(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+<br')
    results = pattern.findall(res.text)
    res_lists = []
    for result in results:
        creator = result[18:-3]
        if creator not in res_lists:
            res_lists.append(creator)
    if len(res_lists) == 0:
        print("The result is None!")
        return "None res"
    else:
        for res_list in res_lists:
            res = SQLTools.query_from_UserNew_more_info_by_tag(res_list)
            if len(res) > 0:
                print("The Creator:" + str(res_list) + " Has Got")
            else:
                print("new res!--->" + str(res_list))
                append_to_file(res_list)


def append_to_file(tag_name):
    res_path = os.path.join("/Users/dingtone/Documents", "res.txt")
    with open(res_path, "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
        file.write(str(tag_name) + " " + "\n")


def rename_file(file_path):
    try:
        os.rename(file_path, os.path.join("/Users/dingtone/Desktop/检索无结果", "Noresult" + str(time.time()) + ".jpg"))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    cover_path = "/Users/dingtone/Desktop/待检索2"
    listdirs = os.listdir(cover_path)
    hhhh = []
    for listdir in listdirs:
        time.sleep(random.randint(5, 15))
        if not listdir.endswith(".jpg"):
            pass
        else:
            file_path = os.path.join(cover_path, listdir)
            res = search(file_path)
            if res == "error":
                sys.exit("Error in Search!")
            elif res == "None res":
                rename_file(file_path)
            else:
                try:
                    os.remove(file_path)
                except Exception as e:
                    print("删除失败，原因：", str(e))
