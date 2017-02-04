#! /usr/bin/python
# -*- coding:utf-8 -*-

import time	#引入time模块
import calendar


#有关日期和时间
ticks = time.time(); 	#当前时间戳
print('当前时间戳：',ticks)

#获取本地时间
localtime = time.localtime(time.time());
print('\n本地时间为：',localtime)

#格式化时间
str_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print('\n当前时间为：' + str_time)

#将格式时间字符串转换成时间戳
f_ticks = time.mktime(time.strptime(str_time,'%Y-%m-%d %H:%M:%S'))
print('\n时间戳为：',f_ticks)

#获取某月日历
cal = calendar.month(2017,2)
print('以下是2017年2月份的日历：')
print(cal)