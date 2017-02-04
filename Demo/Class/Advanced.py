#! /usr/bin/nev python
# -*-coding:UTF-8-*-
from types import MethodType

# ---------------1、“__slots__”限制实例属性和方法-----------------
# 使用__slots__限制实例属性
class Student(object):
	"没有采用限制实例属性的对象"
	pass

stu = Student()
stu.name = 'WangHailin'	#给实例绑定了一个name属性
print(stu.name)

#给实例绑定一个方法
def set_age(self,age):
	self.age = age
stu.set_age = MethodType(set_age,stu)
stu.set_age(22)
print(stu.age)

#为了让所有实例都能使用方法，可以给class绑定方法，给一个实例绑定的方法或属性对其他实例无效
def set_sex(self,sex):
	self.sex = sex
Student.set_sex = set_sex
temp = Student()
temp.set_sex('女')
print(temp.sex)
stu.set_sex('男')
print(stu.sex)

# 现在实例的属性和方法
class Test(object):
	"采用显示实例属性的对象"
	__slots__ = ('id','name')

t = Test()
t.id = 123
t.name = 'test'
print('id:',t.id,',name:',t.name)

# --------------2、“property”检查参数----------------
class User(object):
	"用户信息的对象"
	def get_age(self):
		return self.age

	def set_age(self,value):
		if not isinstance(value,int):
			raise ValueError('年龄只能为数字！')
		if value < 0 or value > 100:
			raise ValueError('年龄必须在0~100之间！')
		self.age = value

u = User()
u.set_age(24)
print(u.age)

# 内置装饰器proprty可以将方法变成属性
class Number(object):
	"测试内置装饰器"

	@property
	def birth(self):
		return self._birthday

	@birth.setter
	def birth(self,value):
		self._birthday = value

	@birth.deleter
	def birth(self):
		del self._birthday

num = Number()
num.birth = '1994-12-26'
print(num.birth)

# property原型
class Prototype(object):
	"""测试proprty原型的使用
	property函数原型为property(fget=None,fset=None,fdel=None,doc=None)
	"""

	def get_string(self):
		return self.__str

	def set_string(self,value):
		self.__str = value

	def del_string(self):
		del self.__str

	str = property(get_string,set_string,del_string,'set str proerty')


p = Prototype()
p.set_string = '测试'
print(p.get_string)
