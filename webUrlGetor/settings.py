# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

BOT_NAME = 'webUrlGetor'
SPIDER_MODULES = ['webUrlGetor.spiders']
NEWSPIDER_MODULE = 'webUrlGetor.spiders'
USER_AGENT_LIST = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
                   "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
                   "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
                   "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
                   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
                   "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
                   "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
                   "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                   "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
                   "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
                   "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
                   "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
                   "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
                   "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
                   "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
                   "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
                   "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
                   "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
                   "Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
                   "Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
                   "Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
                   "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
                   "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
                   "Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                   "Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
                   "Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
                   "Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
                   "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
                   "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
                   "Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
                   "Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
                   "Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
                   "Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
                   "Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
                   "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
                   "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
                   "Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
                   "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
                   "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
                   "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
                   "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
                   "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
                   "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
                   "Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
                   "Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
                   "Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
                   "Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
                   "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
                   "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
                   "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
                   "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
                   "Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
                   "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
                   "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
                   "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
                   "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
                   "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
                   "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
                   "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
                   "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
                   "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
                   "Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN", ]

ITEM_PIPELINES = {

    'webUrlGetor.pipelines.PicspiderPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

"""
tags = "rouka" done
tags = "kantoku" done
tags = "rurudo" done

tags = "unicorn_%28azur_lane%29" # 独角兽（碧蓝航线）done
tags = "takao_%28azur_lane%29"  # 高雄 done
tags = "ayanami_%28azur_lane%29"  # 凌波 done
tags = "javelin_%28azur_lane%29"  标枪 done
tags = "laffey_%28azur_lane%29" 拉菲 done
tags = "atago_%28azur_lane%29"  # 爱宕 done
tags = "nagato_%28azur_lane%29" # 长门 done
tags = "eldridge_%28azur_lane%29" # 埃尔德里奇
tags = "ame_nochi_yuki"  done
tags = "ibuki_%28azur_lane%29"  # 伊吹


tags = "rem_(re_zero)"  # re0 done tyone
tags = "rem_galleu" done 蕾姆 异界少女召唤术  rimuu yamashiro_(azur_lane)  schreibe_shura
tags = "myuseru_foaran" done    compile_heart  shiratama    momoko  atdan  nanahachi
tags = "bandaid" done  natsukawa_masuzu  yijian_ma  saya_(mychristian2)  abandon_ranka  heartsix
tags = "suomi_kp31_(girls_frontline)"   nazu-na  mvv  chunrijun_(springer)  superpig  sakai_kyuuta  kuang_(kzhw7588)
tags =   satsuki_neko  mizuhara_yuu  girl_cafe_gun  rin_yuu  haribote_(tarao)  jimmy  chiachun0621
tags = "ryuuou_no_oshigoto!" done  filings_(ailuo_c)  silver_(chenwen)  k_mugura  umibouz  hasekura_chiaki   kisaragi_yuri
tags = "shera_l._greenwood" done  junpaku_karen    pdxen  ringozaka_mariko  mirea  kanju  chita_(ketchup)
tags = "belfast_(azur_lane)"done  tomotake_yoshino  tomotake_yoshino  maid    niliu_chahui  saya_(mychristian2)
tags = "gyouzanuko" done  ichiyou_moka  yuudachi_(azur_lane) tomotake_yoshino parfaitlate mirei  masayo_(gin_no_ame)  infinote
tags = "minakami_rinka" done    maeda_shiori   araragikoyomis  bikini  motomiya_mitsuki  akishino_himeka  kim_eb  necomi ibara_riato
tags = "pantsu"  censored  "kyaru" done  bachibachi_(tisen)  koinu-chan nekomugiharu     suomi_kp31_(girls_frontline)
tags = "akashi_%28azur_lane%29" hammann_(azur_lane) illustrious_(azur_lane) formidable_(azur_lane)   akashio  fuyuumi_ai  lethe-shion
prinz_eugen_(azur_lane) yukikaze_(azur_lane) done  tokkzyu sunhyun  wsman  takimoto_hifumi  amashiro_natsuki  mikagami_mamizu
"""

""" 
suzumori_uina youzixiaoming sukja a20_(atsumaru)[Y站是a20]
chikotam yuuhagi_(amaretto-no-natsu) chikotam rikatan aa_(sin2324) mofuaki hisaka_hazara kiyo_(chaoschyan)
tsubaki_(yi) tsumiki_akeno  tokisaki_kurumi yoshino_(date_a_live) toketou yano_mitsuki yusan kujou_danbo urabi_(tomatohouse) kujou_danbo
snozaki hoshi_(snacherubi) u35 ogipote homura_subaru wasabi_(sekai)  takenoko_no_you habu.  yamcha_(cocololi)  ajigo tsubaki_(yi)  p19 natasha_(pommier)
shiratama_(shiratamaco)  cozyquilt  hiten_(hitenkei)  sex  kyubi  peco piukute062  haishiki peco hawah127  huwali_(dnwls3010)  gio_(artist)
gurande_(g-size) nagayama_yuunon kabako baseness  mokew  oyu_(sijimisizimi)  fuji_choko  mignon noboru_(kamine204136)  nyum  mignon
77gl pikuharu dre  yuna_(deadawon)  lisu soya_(torga)  ppyono apple_caramel  haru_(hiyori-kohal)  bison_cangshu  silltare  hanekoto  blush
kanadetsuki_shion sen_(astronomy) kurou_(quadruple_zero) kusano_houki uosaasou  yoshida_iyo  siloteddy  uncensored# y站爬到39 takehana_note
ikeuchi_tanuma kazuharu_kina kazutake_hazano yukishiro_arute nagishiro_mito kinokomushi h2o_(dfo) hyuuga_azuri yukimaru217 uncensored ryoutan
manda_(eyelashes)  kanadetsuki_shion  yatomi ririko_(zhuoyandesailaer) tsunako peko u2_(5798239) rurikoma tsuedzu  pinb piromizu yuran
fufumi  shiratama_akane jigatei_(omijin) denfunsan mayag nuko_miruku sukireto mechuragi rurikoma efe pan_(mimi)  usagihime hazuki_(sutasuta)

==============以下为特级画师   P站关注的画师已经看完第6页
mafuyu_(chibi21)
mitsuba_choco ame_usari maccha byulzzimon yuuki_hagure
mellozzo❤  cgny7477 tokkyu fifty1202 ohshit izayoi_miku coffee-kizoku
haneru ❤   kfr manda_(manda9n) sutorea misomiso_154 koyama_sao mkichi tsliuyixin hiroichi
nagayama_yuunon azuki_yui karutamo  yasuyuki takei_ooki  10eki_(tenchou) cccpo narae  kishiyo lambda calder ne-on sibyl
takei_ooki sasahara_wakaba viola1587 azuki_yui fuji_noyume hisasi agung_syaeful_anwar nitchi blade_(galaxist) hakuya_(white_night)
mamizu  risemu_(c_liesem)  mullpull  ichi_makoto kokusan_moyashi tsuuhan cenangam kaede suya2mori2 yamasan suihi uiri-na amashiro_natsuki
maruma_(maruma_gic)  otokuyou pnatsu ririko_(zhuoyandesailaer)  tsuruse motokonut  yu-ori ogata_tei katsushika_pachi 
kachayori  monety reinama qianjing sunege_(hp0715) unasaka_ryou shibainu_niki  aro_1801 giraffe_(ilconte) nagiha_kuten
baffu gomzi potco fujikura_ryuune  agekichi_(heart_shape)  pirorikin  kuaua kagiyama_(gen'ei_no_hasha)
fueru_nattou kagawa_yuusaku  tidsean tiv pot-palm  tsuchikure_(3105mitoko) tsuchikure ayamy maeha tougetsu tukise_33
cha_chya 5555_96 nayuta_hilo bxr tomoo>>tomoo_(tomo) narynn tomoo_(tomo) sasachin sasachin_%28k%2Bw%29  purinpu bada_(jksh5056)
shiny_shinx akyorapenyo  toriumi_harumi  cruel_gz pre_(17194196) yuuki_(yukinko-02727) umakuchi_shouyu shiruko27anko
cocona apple_ringo miko_92 tamakake murasaki_(murasakiiro_no_yoru) shiratama_(shiratamaco) na!?_(naxtuyasai)
hanato_(seonoaiko) unacchi_(nyusankin) haori_iori kisaragi_miyu curcumin lpip zjsstc silly_(marinkomoe) toosaka_asagi tomohiro_kai
mashiro_monaka mannaku hatafuta moemoe3345 mery_(apfl0515) peulopi hidebuu ero_waifu neki_(wakiko)  kouda_suzu suzuki_moeko
 irohasu nahaki mika_pikazo sazaki_ichiri  toba_hiyoko r_o_ha  agnam_ore tid gabiran aaeru hatafuta  kino_(kino_konomi) sousouman
pingo kotetu_han shen_hong torino_akua  kotetu_han ramchi sinsihukunokonaka suisen-21 cocoasabure baku_ph shinooji
mizuki_ryuu deadnooodles 
"""

"""
siu_(siu0207) seinen yappen niie nyatabe lisu kazu
nanoless usagihime stoyo_606 yamamoto_tomoha araragikoyomis gou_d white_l mash_kyrielight chixiao
fujima_takuya sakipsakip maosame takeg05 tokinohimitsu yang_guifei_(fate/grand_order) user_gypr5774
 kurumi_moka shichimiyagin love_makira tenzeru paaru yuuko_(030_yuko) terry_(pixiv3274443) solru piyodera_mucha
kurikara  riv marmoset0 marmoset_(marmoset0) haru_(re_ilust) tail sakura_(mtmr4354) hinaki_(hinaki_0102) motohara_moka sirius_(azur_lane)
bison_cangshu  miyase_mahiro tyot swimsuits rouka_(akatyann) gzsd natsumii_chan mizunashi_kenichi  tail akin_(asada0825p) kousaki_rui
z23_(azur_lane) yayoichi_(yoruyoru108) xue_lu  jakoujika john_zerowb  aki99  nekoko_(windcat429)
ibuki_notsu  matsukawa_(pale_scarlet) yoruciel koukoku masaoka_misaki lambda_(kusowarota) u4284g nironiro kuroduki_(pieat)
blackblades donedone lexis_yayoi ryoumoto_ken ozaki_mirai 1136002526 regumaki tia_(4017342)  fujimori_shiki azto_dio fay_(fay_axl)
nitro_(mugityaoisii) yuuzaki sawada_yuusuke kase_daiki hisenkaede sukisukiharami obiwan kana616 michou akchu aogi_(pixiv9459043)
youqiniang ken_ill miyakure tef matokechi fujieda_uzuki  swiftsure_(azur_lane) theleopardcat denchu_(kazudentyu)
dyolf jjkl9195 gijang chaou amasora_taichi mauve kanadetsuki_shion taya taya_5323203 fukai_ryousuke hajikaji kleune foka_(beginner)
shiino_sera hisasi hisashi_(nekoman) kaisu pupupu_(1053378452) hitaki_yuu hitsukuya nekonabe_ao keiran_(ryo170)
sakura_ani kinty natsuki_marina aye game_cg minato_(ojitan_gozaru)  ame. rimo akashio_(loli_ace) angel_no_shousou sencha
 kuria_(clear_trip_second) chinomaron himiya_ramune sasai_saji agnam_ore necomi ggatip matatabi_maru  tarachine
suisen nonono naoto_(tulip) chao_wu_xing_xian squchan naoto_(tulip) macaron_taitei sino_(sionori) sakura_neko kaetzchen
rei_(rei's_room) mayogii gochou_(atemonai_heya) cai_geng yuririn_poi sama akieda lerome akatsuki_ikki tsukudani_norio
kouyafu  leria_v sahara386 pochi_(pochigoya) kouzuki_fukurou fuji_dorokai kaede_(003591163) hanbenp  torano
shanghmely  anmi tagme_(artist) komeshiro_kasu fukahire_(ruinon) saru mishima_kurone hokori_sakuni
tming matsui_hiroaki gei_daipf nagu  azuuru analog_kenshi_(moto) roslyria konomi urata_asao
t6_ti minato_aqua fast-runner-2024 kamishiro_(rsg10679) tamano_kedama criin chikuwa. kinokorec dreamcatcher
hasune aimee_(emi) siino emily_(pure_dream)  ohara_tometa fuumi_(radial_engine) yuxian_youka nanotaro konomi hoshi
u35 tokenbox jaga_yamatarawo k-doku clouble onineko hirotan_insitao tomo_(user_hes4085) fallen_heaven
amedamacon oryou sakuragi_ren yunamaro misumi_(macaroni) toridamono jyt ju_(a793391187) maritaki yano_momoko user_yzzn3747
hidaka0503 seon_(seonon_) anparu cait shuugetsu_karasu umibouzu_(niito) momoko_(momopoco) hiraga_matsuri wasabi_(sekai)
yashiro_seika wowoguni ke-ta miwabe_sakura
sawa_(sawasaku)  to_naive miruto_netsuki
youmu_(tomgoku2) nari_(narikashi)
"""
tags = "okota_mikan"

"""
tatapopo   osa_(osaosa)  kyouya_(mukuro238)
note55885  takeashiro
burenbo
fuyuki030
kanzaki_hiro
racchi.
roriwanko
fukunoki_tokuwa
hakuishi_aoi
child_(isoliya)
kachiyori
nedia_(nedia_region)
kinugasa_yuuichi
soushou_nin
ochiai_miyabi
"""


IMAGES_URLS_FIELD = "pic_url"
# 设置图片下载后的存储路径，放到工程目录下images文件夹
# 获取当前目录绝对路径
project_dir = os.path.abspath(os.path.dirname(__file__))
# 获取images存储路径
IMAGES_STORE = os.path.join(project_dir, 'images')
DB_path = os.path.join(project_dir, 'tools')
# 设定处理图片的最小高度，宽度
IMAGES_MIN_HEIGHT = 100
IMAGES_MIN_WIDTH = 100
