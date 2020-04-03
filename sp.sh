#!/bin/bash

echo "k开始爬取！" &
scrapy crawl "k" &
echo "d开始爬取！" &
scrapy crawl "d" &
echo "g开始爬取！" &
scrapy crawl "g" &
echo "y开始爬取！" &
scrapy crawl "y" &
wait
