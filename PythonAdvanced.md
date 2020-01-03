# Python Advanced

## 1. DeepCopy and ShallowCopy
### Shallow Copy: copy the reference
```python
a = [11,22,33]
b=a
id(a) == id(b)
```
### Deep Copy -- copy moudule deepcopy(item)
```python
import copy
c = copy.deepcopy(a)
id(a) != id(c)
```
+ **deepcopy() is recursive copy**:
```python
a = [11,22,33]
b = [44,55,66]
c = [a,b]
e = copy.deepcopy(c)
id(c[0]) != id(e[0])
```

## 2. Class Property -- used on private attribute
```python
class Test(object):
    def __init__(self):
        super(Test, self).__init__()
        self.__num = 100 #1
 
    @property
    def num(self): #2
        return self.__num
 
    @num.setter
    def setNum(self, num): #3
        self.__num = num
 
    @num.getter
    def getNum(self): #4
        return self.__num

t = Test()
t.num =200 #5
print(t.num)
```

## 3. Python Dynamic
### a. Dynamically add attribute to a class:
+ add public attribute:
```python
p1 = Persion("laowang", 65)
p1.sex = 100
p2 = Persion("xiaoming", 18)
print ([])
```
+ add class attribute:  
`Person.num = 100`

### b. Dynamically add method to a class:
+ add public method:
```python
def run(self):
	pass
P.run = type.MehodType(run, P) #type 是默认创建 metaclass 的方法
```
+ add class method:
```python
@classmethod
def testClass(cls):
	pass
Person.testClass = testClass
```
+ add static method:
```python
@staticmethod
def testClass2(cls):
	pass
Person.testClass2 = testClass2
```

### c. Check bound result:`dir(P)`

### d. __slots__ -- forbid a class being modified dynamically.
States the attributes belongs to class. Class with __slots__ cannot add or delete any attributes.
```python
class Person(object)
	__slots__ = ("name", "age")
```
+ Benefits:
    1. faster attribute access.
    2. space savings in memory.

The space savings is from storing value references in slots instead of __dict__.

## 4. Generator
List Comprehension `a = [x*2 for x in range(1000000)]` will return the whole list and occupy a lot of system resources. This may be finnally killed  by kernel.

### a. What is generator?
It is a function that can return the value of during every iteration.
When return a value, generator will remember the execution postion.
It will also remember the values of local variables.

### b. Create Generator by List Comprehensions
```python
G = (x*2 for x in range(5)) #chang [] to ()
G
<generator object <genexpr> at 0x7f626c132db0>

next(G)
```
Generator stores the algorithm. Calling next(G) will return the value of next item. If there's no more element, system will throw StopIterator exception.   

We can use for loop to print out all values.
```
for x in G:
	print(x)
```

### c. Create Generator by functions

斐波拉契数列（Fibonacci）1, 1, 2, 3, 5, 8, 13, ......

List Comprehension cannot achieve this, but it can be easily implemented by functions:
```python
def createNum():
	'''create fibonacci number'''
	a, b = 0, 1
	for i in range(5):
		print(b)
		a, b = b, a+b

createNum()
```

Use `yield b` to replace `print(b)`, then the function became a generator. 
```python
def createNum():
	listNum = []
	a, b = 0, 1
	for i in range(5):
		yield b #function get suspended and return value b
		a, b = b, a+b
a = createNum() #return generarot object
'''
next(a)
1
next(a)
1
next(a)
2

for n in a:
	print(n)
'''
#Generate a list:
mylist = [x for x in a]
print(mylist)
```
**Note: Once the generator's point reaches to the end, the next items will return None.**

### d. send(para):
```python
def test():
    i = 0
    while i < 5:
        temp = yield i  #temp is waiting for the agrument from send()
        print(temp)
        i +=1

t = test()
print(next(t)) #when the program readed to yield i, function suspend and return value of i.
#0

print(next(t)) #function continue, temp=None -> print(temp) -> i+=1 -> while i<5 -> suspend at yield and return i again. 
#None
#1

print(t.send("haha")) #use send to pass argument to temp.
#haha
#3
```

### e. Generator Usage --  tasks coroutine(协同) on server
```python
def test1():
	while True:
		print("--1--")
		yield None

def test2():
	while True:
		print("--2--")
		yield None

t1 = test1()
t2 = test2()
while True:
	next(t1)
	next(t2)
```

## 6. Iterator -- Focus on concept
An object that can be called by next() and return an item.

### a. Iterable Object:
If an object can be used in for loop, we can this object is iterable.

Iterable objects in Python:
+ list, tuple, set, dict, str
+ generator

### b. Check if an object is iterable
```python
from collections import Iterable
isinstance([], Iterable)
```

### c. iter(object) -- transfer a list to an iterator
By default, list,set,dict, etc. are not iterator because they cannot be called by next().

iter(object) can transfer a list(etc.) to an iterator.

## 7. Closure (闭包)
### a. Fucntion name is the reference of function object
```python
def test():
    print("----1----")
b = test
print(test)
print(b)
id(b)
id(test)
```
### b. Closure
A function defines another function and return this function's reference.
```python
def test1(number):
    def test_in(number_in):
        return number + number_in
    return test_in

ret = test1(100) # ret is the reference of function test_in(number_in)
ret2 = ret(200) 
print(ret2) ==> 300
```

### c. Usage: ML and math
```python
def test(a, b):
    def test_in(x):
        return a*x+b
    return test_in

line1 = test(1,1) #==> modify the origenal test(a,b) object
line1(0)
line2 = test(10,4) #==> 开辟一个新的空间存储函数对象
line2(0)
```

## 8. Decorator -- 把一个函数当做参数的闭包
### a. Principal: Use Closure technology to expand a function
```python
def w1(func): # pass function as paramenter.
    def inner():
        print("verifying....")
        func()
    return inner

def f1():
    print("----f1----")

f1 = w1(f1)
f1()
```
### b. Define a decorator:
```python
def w1(func): # pass function as paramenter.
    def inner():
        print("verifying....")
        func()
    return inner

@w1  #==> equals to f1 = w1(f1)
def f1():
    print("----f1----")

f1()
```
### c. A function with two decorators
```python
def makeBold(fn):
    def wrapped():
        print("----1---")
        return "<b>" + fn() + "</b>"
    return wrapped

def makeItalic(fn):
    def italiced():
        print("----2---")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold    #==> 2. test3=makeBold(test3)=makeBold(makeItalic(test3))
@makeItalic  #==> 1. test3=makeItalic(test3)
def test3():
    print("----3---")
    return "hello world-3"

print(test3())
#<b><i>hello-world-3</i></b>
```

### d. Expand a function with parameters
```python
def func(functionName):
	def func_in(a, b): 
		functionName(a, b)
	return func_in

@func
def test(a, b):
	print("----test a=%d, b=%d-----" %(a,b))

test(1, 2)
```
### e. General decorator
```python
def func(functionName):
	def func_in(*args, **kwargs): 
		print("记录日志")
		ret = functionName(*args, **kwargs)
		retrun ret
	return func_in

@func #test = func(test)
def test(a, b):
	print("----test a=%d, b=%d-----" %(a,b))

```

## 9. NameSpace
```python
a=100 #The namespace of a is current file.

import test
test.func1() #The namespace of func1() is test.py

from test2 import func2 # func2 is imported to current file's namespace

def test3(a,b):
	print (a) # The namespace of a is function test3
	print(b)
```
### globals, locals
+ globals() ==> dict, 所有全局变量 key-value paris
+ locals() ==> dict, 所有的局部变量 key-value paris

## 10. PDB -- python debug
```
python3 -m pdb test1.py

l : list code 找 "->" 表示当前行
n(next): 向下执行一行
c: continue 继续执行代码
b 7: 在第 7 行添加断点
clear 7: 删除第 7 行断点
p a: 打印变量 a的值
a(args): 打印所有形参（parameter）数据
s(step) 进入到一个函数
q(quit) 退出
```
## 11. map(func, list1[,list2,..]) -> list
```python
# map function needs one parameter
map(lambda x: x*x, [1, 2, 3])

# map function needs two parameters
map(lambda x,y: x+y, [1,2,3], [4,5,6])
```

## 12. Garbage Collection
### a. small integer object pool
整数在程序中的使用非常广泛，Python为了优化速度，使用了小整数对象池， 避免为整数频繁申请和销毁内存空间。 
Python 对小整数的定义是 [-5, 257) 这些整数对象是提前建立好的，不会被 垃圾回收。在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象. 
同理，单个字母也是这样的。

### b. intern 
Every string without any whitespaces shares the same memory space.
让他只占用一个”HelloWorld”所 占的内存空间。靠引用计数去维护何时释放。 
单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0， 则销毁 
字符串(含有空格)，不可修改，没开启intern机制，不共用对象，引用 计数为0，销毁

### c.GC
python采用的是引用计数机制为主，标记-清除(Ruby用"地球停转垃圾回收大法" )和分代收集(call gc.collect())两种机制为辅的策略