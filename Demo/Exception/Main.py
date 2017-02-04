#! /usr/bin/python
# -*- coding:UTF-8 -*-

#异常处理代码块，测试异常的方法
def exceptionFun(mode):
	try:
		file = open('test.txt',mode)
		file.write('这是一个异常测试文件！\n')
	except Exception as e:
		print(e)	#打印出异常信息
	else:
		print('文本信息写入成功！')
	finally:
		print('操作完成！')	#无论如何都会执行的代码
	return

#文件不存在，执行写入操作，将执行异常部分代码
exceptionFun('r+')

#文件不存在则创建，执行写入操作，无异常报错
exceptionFun('a+')

