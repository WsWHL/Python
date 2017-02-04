#! /usr/bin/python
# -*- coding:utf-8 -*-

#使用for循环打印九九乘法表
print('如下是九九乘法表：')
row = 1
while row <= 9:
	column = 1
	row_str = ''
	while column <= row:
		row_str += str(column)+' x '+str(row)+'='+str(column * row)+'  '
		column += 1
		pass
	print(row_str)
	row += 1
	pass

#内置函数len()返回列表长度,range()返回一个序列的数
arrays = ['张三','test','sb',25,True,89.5567]
#使用for循环打印数组的每一个值
for item in arrays:
	print(item)
pass

for index in range(len(arrays)):
	print('索引：',index,'值：',arrays[index])
pass