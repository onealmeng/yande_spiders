#!/bin/bash
echo "开始爬取！"
name=$1
if [ "${name}" == "all" ]
then
   echo "三站爬取"
   scrapy crawl "y"
   scrapy crawl "k"
   scrapy crawl "d"
   scrapy crawl "g"
else
  scrapy crawl "${name}"
fi
