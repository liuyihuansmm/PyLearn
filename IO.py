# -*- coding: utf-8 -*-

#=================IO编程================
#1.open
#2.read
#3.close
#4.r 、w、 rb
'''
f = open('E:/Py_workspace/hello.py','r')
print f.read(1000)
f.close()

with open('E:/Py_workspace/IO.py','r') as fio:
    print(fio.read())
'''
'''
import os,os.path

#print os.environ

print os.path.abspath('.')

#os.mkdir('atest')
#os.rmdir('test')

print os.path.split(r'E:\Py_workspace\hello.py')
print os.path.splitext(r'E:\Py_workspace\hello.py')

#os.rename('test.txt','test.py')
#os.remove('test.py')

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
'''
#序列化：内存里的对象持久化到硬盘里
#反序列化：....

import pickle,json
'''
d = dict(name='lyh',age=23)

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

fn = open('dump.txt','rb')
d = pickle.load(fn)
fn.close()
print d

f1 = open('dump1.txt','wb')
json.dump(d,f1)
f1.close()

fn1 = open('dump1.txt','rb')
d2 = json.load(fn1)
fn1.close()
print d2
'''
class Student(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

def stu2dict(stu):
    return{"name":stu.name,"age":stu.age,"sex":stu.sex}

s = Student('lyh',23,'m')

print json.dumps(s,default=stu2dict)

print json.dumps(s,default=lambda obj:obj.__dict__)