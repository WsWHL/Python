#! /usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import re

url = 'Http://www.baidu.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3023.0 Safari/537.36'
request = urllib2.Request(url)
request.add_header('User-Agent', user_agent)
response = urllib2.urlopen(request)

print '状态码：', response.getcode()
print '-------------使用bs4解析获取到的网页内容--------------'

soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
print '获取文档中所有链接：'
links = soup.find_all('a')
for item in links:
    print item.name, item['href'], item.get_text()

# 使用正则匹配一个元素
home = soup.find_all('a', href=re.compile('(http|https):.*com'))
for item in home:
    print item['href'], item.get_text()
