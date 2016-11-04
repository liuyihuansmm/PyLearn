# -*- coding: utf-8 -*-
#注释
"""======================基础=============================="""
"""
name = raw_input('please enter your name:')
print 'hello,',name

if 1>0:
	print 'hehe'
else:
	print 'fuck'

print r'http:\\\\www.baidu.com'

print '''百日依山尽，
黄河入海流。
欲穷千里目，
更上一层楼。'''

print True,False

print 10/3.0
print 10//3.0

print 10%3

a = b'刘一寰'
print a

print '增长率为: %.2f %%' % 3.1415926
"""

""" ===========================List和Tuple===================="""
"""Tuple的不变是指其指向不变，如果指向不变但是指向的内容变了看起来也就变了"""
"""
classmate = ['mike','bob','ellas']
print len(classmate)
print classmate[2]
classmate.append('Adam')
print classmate
classmate.insert(1,'lyh')
print classmate

classes = ('Java','C++',['Python','PHP'])
print classes
classes[2][0] = 'Oralce'
print classes
"""

"""=========================if else=========================="""
"""
sage = raw_input('please enter your age:')
age = int(sage)
if age<18:
    print '青少年'
elif age>=18 && age<30:
    print '年轻人'
elif age>=30 and age<60:
    print '中年人'
else :
    print '老年人'
"""

"""=======================dict和set========================="""
"""dict 键值对 key-value,key 必须为不可变(整数和字符串)"""
"""
d = {'Mike':90,'Able':87,'lyh':100}
print d['lyh']
if ('shm' in d) == False:
    d['shm'] = 150
print d
"""
"""
#()里面的[]为可变因此不能加入set
set1 = set((1,2,3,4,[3,2,1]))
#()里面全是整数，不可变所以可以
set2 = set((1,2,3,4,3,2,1)
set2.add(5)
set2.remove(2)
set1 & set2 交集
set1 | set2 并集
print set1
"""

"""==============================函数============================"""
"""函数的返回实际是一个Tuple"""
"""
def my_abs(num1):
    if num1>0:
        return num1
    else:
        return -num1
snum = raw_input('please enter a number:')
num = float(snum)
my_abs(num)
print num
"""
"""=============================函数的参数======================="""
"""
1.位置参数:依次序传入 pow(x,n)
2.默认参数:pow(x,n=2),pow(5)相当于pow(5,2)
           必选参数一定在前
           默认参数必须指向不可变对象，否则调用时候，默认参数会"变
3.可变参数：参数个数可变，*args，调用时自动组装成Tuple
4.关键参数：**kw,自动组装成dict
5.命名关键字参数:只允许传指定关键字参数
"""

"""===========================递归函数=========================="""
"""
def fact(n):
    if n==1:
        return 1
    else :
        return n*fact(n-1) #栈溢出

snum = raw_input('please enter a number:')
num = int(snum)
print fact(num)

#优化

def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
snum2 = raw_input('请输入一个整数:')
num2 = int(snum2)
print fact(num2)


#汉诺塔问题
def move(n,a,b,c):
    if n==1:
        print a+'-->'+c
    else:
        #先把n-1从A开始移到B
        move(n-1,a,c,b)
        #把最后一个直接从A移动到C
        print a+'-->'+c
        #再把n-1从b移动到C
        move(n-1,b,a,c)

move(3,'A','B','C')
"""

"""=========================高级特性===================="""
"""
#切片slice
L = list(range(10))
print L[-2:]
print L
print L[:10:3]
print (0,1,2,3,4,5)[::2]
print 'ilovesmm'[:5:2]
"""

"""
#迭代
dic = {'JAVA':'60%','Python':'50%','C++':'10%','Oracle':'40%'}
for d in dic:
    print d
for v in dic.values():
    print v
for i in dic.items():
    print i
"""
#迭代类型 collections模块的Iterable类型判断，只有该类型才能for遍历
"""
from collections import Iterable
print isinstance(123,Iterable)
print isinstance((),Iterable)

for i,value in enumerate(['a','b','c','d']):
    print i,value
"""
"""=======================列表生成式=========================="""    
"""
L = [x*x for x in range(10)]
print L

import os
print [d for d in os.listdir('.')]

L = [s.lower() for s in ['ScYy',18] if isinstance(s,str)]
print L
"""
#生成器:generator 是一种算法,当你要用的时候算出该值返回，而List是提前把'结果'准备好的。
"""
g = (s.upper() for s in['abc','hh',12] if isinstance(s,str))
print next(g)
print next(g)

def taiangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
n = 0
for t in taiangles():
    print t
    n+=1
    if n==10:
        break
"""

"""=========================迭代器======================="""
#Iterable:可迭代对象，List Tuple str dict set generator
#Iterator:迭代器 可以被next()函数调用不断返回下一个值的对象，如generator
#可以通过iter()函数把List Tuple str dict set变成Iterator

"""========================函数式编程======================="""

"""========================Map && Reduce===================="""
'''
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print map(char2num,'1314')
'''
'''
L = ['adam', 'LISA', 'barT']
def normalname(s):
    return s[0].upper()+s[1:].lower()
print map(normalname,L)

L2 = range(1,5)
def pord(x,y):
    return x*y
print reduce(pord,L2)

#字符串转浮点1231415

snumber = '123.1415'
def s2float(s):
    n = s.find(".")
    s = s.replace(".","")
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))/10.0**(len(s)-n)

def s2float2(s):
    return reduce(lambda x,y:x*10.0+y,map(lambda x:{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[x],s.replace(".","")))/10.0**(len(s)-s.find(".")-1)
print s2float2(snumber)
'''
'''
#filter:筛选所有素数
#首先偶数除2意外以外都不是素数，所以构造的时候，可以直接生成从3开始的奇数
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

#这里注意返回值，是返回的一个匿名函数，返回的是函数！
def _not_divisible(n):
    return lambda x:x%n!=0

#素数生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''

"""=============================sorted()=========================="""
"""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sort_by_name(li):  
    return li[0]

print sorted(L,key=sort_by_name,reverse=True)
"""
"""
def f(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax+n
        return ax
    return sum

f1=f(1,2,3,4,5)()
f2=f(1,2,3,4,5)()

print f1 == f2

def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count1()
print f1(),f2(),f3()

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()
"""

'''==================================匿名函数==========================='''

'''==================================装饰器============================='''
#1:函数都有__name__属性

'''
def log(func):
    def wapper(*args,**kw):
        print 'lyh'
        return func(*args,**kw)
    return wapper

@log
def now():
    print '2016-10-17'

now()
print now.__name__
'''
'''
class Person(object):
    __slots__ = ('__name','__age')

    def __init__(self,name,age):
        self.__name = name
        self.__age  = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

p1 = Person('lyh',23)
print p1.name,p1.age
p1.name = 'mike'
print p1.name
p1.age = 18
print p1.age
'''

#===========================================定制类===================
#__str()__相当于java中的toString()
'''
class Person(object):
    __slots__ = ('__name','__age')

    def __init__(self,name,age):
        self.__name = name
        self.__age  = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return 'Person object (name:%s,age:%d)' % (self.__name,self.__age)
p1 = Person('lyh',23)
print p1
p1.name = 'smm'
print p1
'''

#================枚举类,2.7没有这个概念=======================
'''
from enum import Enum

Month =  Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print Month.Jan
'''

#==========================元类===============================
'''
def fn(self):
    print 'Hello World'

Hello = type('Hello',(object,),dict(hello=fn))

h = Hello()
h.hello()

def f(n):
    try:
        #if n==0:
            #raise('DivisionByZero')
        return 10/n
    except ZeroDivisionError as e:
        print e
    finally:
        print 'END'

#print f(0)
print f(1)
'''
