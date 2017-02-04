#! /usr/bin/python
# -*- coding:UTF-8 -*-

#继承

class Animal(object):

	def __init__(self,name,sex,age,color):
		self.name = name
		self.sex = sex
		self.age = age
		self.color = color

	def run(self):
		print('Animal is runing...')

	def showAnimal(self):
		print('名字：%s,性别：%s,年龄：%s,毛色：%s' % (self.name,self.sex,self.age,self.color))


class Dog(Animal):

	def run(self):
		print('Dog is runing...')


class Cat(Animal):

	def run(self):
		print('Cat is runing...')


dog = Dog('金毛','雄性','7年','金色')
dog.run()
dog.showAnimal()
cat = Cat('小花','雌性','3岁','白色')
cat.run()
cat.showAnimal()

#判断某个变量是否是某种类型
print(isinstance(dog,list),' ',isinstance(dog,Animal),' ',isinstance(dog,Dog))

print('测试%s' % 5)
print('测试'+ str(5))
