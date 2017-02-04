#! /usr/bin/ven python
# -*- coding:UTF-8 -*-

import os

#打开文件
file = open('test.txt','a+')
print('文件名：',file.name)
print('是否已关闭：',file.closed)
print('访问模式：',file.mode)
#print('尾末是否强制加空格：',file.softspace)

#闲文件中写入内容
info = '使用Python IO向文本文件中写入内容！\n'
num = 0
while num < 100 :
	num += 1
	file.write('第' + str(num) + '次写入文本：' + info)

#读取文件内容
content = file.read()
print(content)

#查找当前位置
position = file.tell()
print('当前文件位置：',position)

#包指针再次定位到文件的开头
position = file.seek(100,0)	#第一个参数表示偏移量，第二个参数表示读取的起始位置
txt = file.read(50)
print('当前文件位置：',file.tell())
print('重新读取字符串：',txt)

#关闭文件
file.close()


#使用内置的os模块操作文件
#1.重命名
#os.rename('test.txt','remark.txt')
#2.删除文件
#os.remove('test.txt')

#使用内置os模块创建文件夹
os.mkdir('新建文件夹')

#将当前目录设置成"新建文件夹"
os.chdir('新建文件夹')

#显示当前工作目录
print('当前工作目录：',os.getcwd())

#删除目录
os.chdir('../')
print('当前工作目录：',os.getcwd())
os.rmdir('新建文件夹')