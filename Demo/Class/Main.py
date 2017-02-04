#! /usr/bin/python
# -*- coding:UTF-8 -*-

#python对象

class Student:
	stuCount = 0

	def __init__(self,id,name,sex,age):
		self.id = id
		self.name = name
		self.sex = sex
		self.age = age
		self.stuCount += 1

	def showStudent(self):
		print('编号：',self.id,'，姓名：',self.name,'，性别：',self.sex,'，年龄：',self.age)

	def displayCount(self):
		print('总共学生人数：',self.stuCount)


#创建实例对象
stu1 = Student(1,'whl','man',22)
stu1.displayCount()
stu1.showStudent()


#访问限制，内部属性不被外部访问，内部属性前加两个下划线"__"即可防止外部访问
class User(object):

	def __init__(self,id,name):
		self.__id = id
		self.__name = name

	def showUser(self):
		print('编号:%s\n姓名:%s' % (self.__id,self.__name))

	def getName(self):
		print(self.__name)

	def setName(self,name):
		self.__name = name

user = User(3,'wanghailin')
user.getName()
user.setName('王海林')
user.showUser()
