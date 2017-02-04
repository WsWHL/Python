#! /usr/bin/python
# -*- coding:UTF-8 -*-

#列表：List
list1 = ['test','name',250,True,'none',0.258854]
print(list1)
#读取第三个元素
print(list1[2])
#采用切片读取第2-5的元素
print(list1[1:5])
#更新，添加（append）一个元素
list1.append([1,'add'])
print(list1)
#删除一个元素
list1.remove('name')
print(list1)


#元组：元组的元素不能修改，使用小括号
tup1 = ('name',True,25,3.14)
print('\n',tup1)
print(tup1[2])
#修改元组
tup2 = ('test','update',False)
tup1 += tup2
print(tup1)
#删除元组
del tup2
#复制元组
tup1 *= 3
print(tup1)
#循环读取元组
for item in tup1:
	print(item)
	pass
#列表转元组
test = [12,'make','lily',True]
print(tuple(test))


#字典
dic = [{'name':'whl','age':25,'sex':'男'},{'name':'lily','age':18,'sex':'女'}]
print(dic[0])
print(dic[1]['name'])
#删除字典元素
del dic[0]['name']
print(dic[0])
#获取所有的键与值
print('第二个字典的所有键：',dic[1].keys())
print('第二个字典的所有值：',dic[1].values())