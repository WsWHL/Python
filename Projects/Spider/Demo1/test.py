#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import cookielib

url = 'http://www.baidu.com'

print '————————————第一种方法——————————————'
response1 = urllib2.urlopen(url)
print '状态码：', response1.getcode()
print '长度：', len(response1.read())

# 模拟浏览器头部信息进行访问
print '————————————第二种方法——————————————'
request = urllib2.Request(url)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3023.0 Safari/537.36'
request.add_header('User-Agent', user_agent)
response2 = urllib2.urlopen(request)
print '状态码：', response2.getcode()
print '长度：', len(response2.read())

# 给urllib2添加cookie会话增强型访问
print '————————————第三种方法——————————————'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print '状态码：', response3.getcode()
print '长度：', len(response3.read())
print 'Cookie:', cj
print '内容：', response3.read()
