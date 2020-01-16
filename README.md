【功能说明】
爬取yande.re网站上指定画师的所有图片。
【使用方法】
直接运行sp.sh（Windows端无法使用）
Windows端请cd如项目目录，运行 scrapy crawl + 你想运行的爬虫的名字。
注意：爬虫全部放在spider文件夹下。
注意：
【注意事项】
1.setting.py中的：已开启DOWNLOAD_DELAY暂时不使用多线程爬取，防止被封或者网站无法正常访问。
DOWNLOAD_DELAY 会影响 CONCURRENT_REQUESTS，不能使并发显现出来。
当有CONCURRENT_REQUESTS，没有DOWNLOAD_DELAY 时，服务器会在同一时间收到大量的请求。
当有CONCURRENT_REQUESTS，有DOWNLOAD_DELAY 时，服务器不会在同一时间收到大量的请求。

【免责声明】
该爬虫不针对任何网站，任何使用者均可以随意修改目标网站，本demo仅供学习和参考，请勿用于商业用途或者侵权行为，否则后果自负。

需要安装Python 2.7 开发环境，下载pycharm
安装requirements.txt中所需的Python包




