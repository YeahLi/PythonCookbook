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
        self.__num = 100
 
    @property
    def num(self):
        return self.__num
 
    @num.setter
    def setNum(self, num):
        self.__num = num
 
    @num.getter
    def getNum(self):
        return self.__num

t = Test()
t.num =200
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
P.run = type.MehodType(run, P) #MetaClass 
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
### d. __slots__ 
Specify the attributes belongs to class. Class with __slots__ cannot add or delete any attributes.
```python
class Person(object)
	__slots__ = ("name", "age")
```
+ Benefits:
    1. faster attribute access.
    2. space savings in memory.

The space savings is from storing value references in slots instead of __dict__.

## 4. Generator
`a = [x*2 for x in range(1000000)]` will return the whole list, which occupies a lot of system resources and will be finnally killed  by kernel.

### a. What is generator?
⽣成器是这样⼀个函数，它记住上⼀次返回时在函数体中的位置。对⽣成器
函数的第⼆次（或第 n 次）调⽤跳转⾄该函数中间，⽽上次调⽤的所有局部
变量都保持不变。
⽣成器不仅“记住”了它数据状态；⽣成器还“记住”了它在流控制构造（在命令
式编程中，这种构造不只是数据值）中的位置。
⽣成器e的特点：
1. 节约内存
2. 迭代到下⼀次的调⽤时，所使⽤的参数都是第⼀次所保留下的，即是
说，在整个所有函数调⽤的参数都是第⼀次所调⽤时保留的，⽽不是新
创建的

### b. Create Generator 1:
```python
G = (x*2 for x in range(5))
G
<generator object <genexpr> at 0x7f626c132db0>

next(G)
```
如果要⼀个⼀个打印出来，可以通过 next() 函数获得⽣成器的下⼀个返回值:
```
for x in G:
	print(x)
```

### c. Create Generator 2:
斐波拉契数列（Fibonacci）1, 1, 2, 3, 5, 8, 13, ......
用列表生成式写不出来，但是用函数却很容易。
```python
def createNum():
	listNum = []
	listNum.append(a)
	a, b = 0, 1
	for i in range(5):
		listNum.append(b)
		print(b)
		a, b = b, a+b
	return listNum
createNum()
```
上面的函数出现yield就成了Generator:
```python
def createNum():
	listNum = []
	listNum.append(a)
	a, b = 0, 1
	for i in range(5):
		yield b #函数暂停，然后返回b的值
		a, b = b, a+b
a = createNum() #返回生成器对象
next(a)
1
next(a)
1
next(a)
2
for n in a:
	print(n)
#生成列表
[x for x in a]
```

### d. send(para):
```python
def test():
    i = 0
    while i < 5:
        temp = yield i  #temp 在这里等着传入的值，可以用send()传入
        print(temp)
        i +=1

t = test()
print(next(t)) #执行到yield时，函数暂停返回 i
#0

print(next(t)) #函数继续，打印temp，然后回到while进行判断，再执行到yield暂停， 返回 i
#None
#1

print(t.send("haha"))
#haha
#3
```

### e. Multitasking -- coroutine used for server
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

## 6. Iterator