#! /usr/bin/python
# -*- coding:UTF-8 -*-

# 1、函数
def mySum(num1,num2):
	'自定义求和函数'
	result = num1 + num2
	return result

print(mySum(23,45))

# 2、按值传递参数和按引用传递参数
arrays = ['name','sex','age',25,True]

def changeme(param):
	print('列表初始值为：',param)
	param.append(['45.23','sb',False])
	print('方法体内改变后的列表值为：',param)
	return

changeme(arrays)
print('\n方法体外列表值为：',arrays)
print('列表属于引用类型，传递列表时实际传递的是引用地址，因此方法内改变后，原列表的值也会改变')


# 3、关键字参数，方法会根据名字自动匹配指定的值
def keyword(name,age,sex = '男'):
	print('\n你输入的值为：\nname=',name,',age=',age,'sex=',sex)
	return

#按参数顺序调用
keyword('wanghailin',21,'男')
#按关键字调用，方法会根据名字自动匹配对应的值
keyword(age = 18,name = 'lily',sex = '女')
#缺省值不给时自动取默认值
keyword('make',28)

# 4、不定长参数
def free(number,*variable):	#加*号的变量会存放所有未命名的变量参数
	'不固定长参数的方法'
	print('编号为：',number)
	for item in variable:
		print(item)
		pass
	pass
	return

free(5)
free(3,'test',True,25)

# 5、匿名函数
result = lambda arg1,arg2,arg3:arg1 + arg2 + arg3
outstr = lambda str1:print('参数的值为：',str1)

print('使用匿名函数求和：',result(23,45.897,36.456))
outstr('采用匿名函数打印文本！')