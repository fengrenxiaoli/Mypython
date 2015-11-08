#!/usr/bin/env pyhont
#-*- coding:utf-8 -*-

name="whole global name"
class Person(object):
	"""docstring for Person"""
	name="class global name"
	def __init__(self, newPersonname):
		name=newPersonname#class global name
		#self.name=newPersonname
		#crifan
		print('local automatic value,name=%s'%name)#crifan
	def sayYourname(self):
		print('My name is %s'%(self.name))
		print('name within class Person is actually the global name:%s'%(name))
		print('only access Person\'s name via Person.name=%s'%(Person.name))
	
def selfAndInitDemo():
	personinstance=Person('crifan')
	personinstance.sayYourname()
	print('whole global name is %s'%name)

if __name__ == '__main__':
	selfAndInitDemo()
