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
    pattern = re.compile(r'Creator: </strong>(?:[a-zA-Z]|[0-9]|\s*|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+<br')
    results = pattern.findall(res.text)
    res_lists = []
    if len(results) == 0:
        print("The result is None!")
        return "resultisNone"
    else:
        for result in results:
            creator = result[18:-3]

            res = SQLTools.query_from_UserNew_more_info_by_tag(creator)
            if len(res) > 0:
                print("The Creator:" + str(creator) + " HasGot")
                return "HasGot"
            else:
                print("new res!--->" + str(creator))
                creator = creator.strip()
                creator = creator.replace(" ", "_")
                SQLTools.insert_into_new_db(str(time.time()), tags_name=creator)
                append_to_file(creator)


def append_to_file(tag_name):
    res_path = os.path.join("/Users/dingtone/Documents", "res.txt")
    need = False
    with open(res_path, "r") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
        text = file.read()
        if tag_name not in text:
            need = True
    with open(res_path, "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
        if need:
            file.write(str(tag_name) + "\n")
        else:
            print("刚刚已经检索到这个画师了！")


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
            elif res == "resultisNone":
                rename_file(file_path)
            elif res == "HasGot":
                try:
                    os.remove(file_path)
                except Exception as e:
                    print("删除失败，原因：", str(e))
            else:
                try:
                    os.remove(file_path)
                except Exception as e:
                    print("删除失败，原因：", str(e))
