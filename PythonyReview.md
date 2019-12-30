# Python Knowledge Review
## 1. Python versions
#### How to check python runtime envirionment version?
sys.verion_info[0] shows the python major version:
```python
def is_python2():
	import sys
	print("You can use Python Future module to write Python version compatiable code.")
	if sys.version_info[0] < 3:
	    print("You are using Python2")
	    return True
	else:
		print("You are using Python3")
		return False
```

## 2. Input and Print
### Input:
`name = input("please input your name:")` < 1 + 4
###### Python 3
num = "1 + 4" ==> just a string
###### Python 2
num = 5 ==> Python 2 will treat your input as python code.
In python 2, you should use raw_input()

### Print:
`print("My name is %s and I am %d years old" %("Henry Li", 30))` ==> no comma before %

## 3. Variable Types
Number: int, long, float, complex ==> immutable  
Boolean: True, False  
String: "aaaa" ==> immutable  
Tuple: (1,2) ==> immutable  
List: [1,2,3]  
Dictionary: {"key1":value1, "key2":value2}  
Set: {1, 2, 3, 1, 1,1} -> {1, 2, 3}  
None  

+ #### Get a variable's type: isinstance(var, type)
```python
i = 1
f = 1.5
s = "I am learning Python 3.6"
l = [1,2,3]
print(isinstance(i,int))
print(isinstance(f,float))
print(isinstance(s,str))
print(isinstance(l,list))
```
+ #### Type Convert: str(18), int("18")
As input function will return a string, you must check the string content before converting it. 
##### Example: Check if input type is int:
```python
num_str = input("Please input function number:")
#Check if input is a number.
if not num_str.isdigit():
	print("Invalid input! The function number must be a number.")
else:
	num = int(num_str)
```
##### Example: Check if input type is float:
```python
str = raw_input("please input the number:")
try:
    f = float(str)
exception ValueError:
    print("Your input is not a number.")
```
##### Expand: Check string content:
```python
str.isalnum() #all characters are numbers or letters
str.isalpha() #all characters are letters
str.isdigit() #all characters are numbers ==> int, long
str.islower() #所有字符都是小写
str.isupper() #所有字符都是大写
str.istitle() #所有单词都是首字母大写，像标题
str.isspace() #所有字符都是空白字符、\t、\n、\r
```
+ #### Check if a variable is None or empty
```python
#check if an object is empty
def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True
```
If the object is string, you can first strip it `string.strip()`

## 3. Operators:
+ "H"*10 ==> 'HHHHHHHHHH'
+ 5 // 2 ==> 2
+ 5 % 2 ==> 1
+ 2 ** 10 ==> 1024 

## 4. String
### a. Common Uasge: 
+ `str(num), len(name), "lao"+"wang", "====%d==="%(num), "="*5`
+ Index: name[2]
+ Slice: str[3:9:2] ==> [start, end, step_length]  
Example: Reverse a string:  
`name[-1::-1]` or `name[::-1]`

### b. Functions: `mystr="  hello world itcast and itcastxxxcpp   "`
+ **mystr.find("world")** ==> -1 means not found.
+ **mystr.replace("world", "WORLD")**
+ **str_list=mystr.split(" ")**  
 **mystr.split()** ==> 1. delete all white space 2. return a list wihtout whitespaces, which can be used to count the words in a string.  
mystr.splitlines() ==> split string into lines.  
+ mystr.capitalize() and mystr.title()
+ mystr.endwith(".txt") ==> Used for check uploading file format.
+ **mystr.lower()** and mystr.upper()
+ **mystr.strip()**, mystr.lstrip(), and mystr.rstrip()
+ **" ".join(["My", "name", "is", "Henry"])** ==> "My name is Henry"
+ **mystr.partition("itcast")** ==> ("  hello world", "itcast", " and itcastxxxcpp   ")

## 5. List
x = [1,2,3,4,5,6]
+ len(x)
+ **Slicing**:  
x[:3] ==> [1, 2, 3] from index 0 to index 2
x[3:] ==> [4, 5, 6] from from index 3 to the end
x[-2:] ==> [5, 6] the last two items 
+ Add elements: x.extend(list), x.append(item or list), x.insert(index, item)
```python
a = [11, 22, 33, 44]
b = [55,66]
a.extend(b)
print(a)
[11, 22, 33, 44, 55, 66]  
################
a.append(b)
print(a)
[11, 22, 33, 44, [55, 66]]
```
+ Remove elements: item=x.pop(), x.remove(item), del x[index]
+ Modify element: x[5] = 8
+ Search:  
a. Whether the list contains the element.
```python
if 7 in l:
	print("7 is in list")
else:
	print("7 is not in list")
```
```python
try:
	l.index(7) #return the first matched index. If not found, raise ValueError exception.
except ValueError e:
	print e
```
b. Search list and get the matched indices
```python
def find_with_list(myList, target):
	inds = []
	for i in range(len(myList)):
		if myList[i] == target:
			inds += i,
	return inds
```
or
```python
indices = [i for i, x in enumerate(aList) if x == 7]
print(indices)
```
+ Multidemision Array:
```python
y = [10, 11, 12]
listOfLists = [x, y] #=> Define two deminsion array
[[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12]]
#
y[1] #=> get the value of an element in a list
11
```
+ **Sort**: x.sort(), x.sort(reverse=True)
+ Generate a number list: `[i for i in range(10,18)]`
```python
range(10,18)
>> [10, 11, 12, 13, 14, 15, 16, 17] #python2
>> range(10, 18) #python3
#
a = [i for i in range(10,18)]
>> [10, 11, 12, 13, 14, 15, 16, 17]
#
b = [i for i in range(10,18) if i%2 == 0]
>> [10, 12, 14, 16]
#
c = [(i,j) for i in range(3) for j in range(2)]
>> [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

## 6. Tuple
`x = (1,2,3)`
+ len(x) => 3
+ x[2] => 6
+ listOfTuples = [x, y] => [(1, 2, 3), (4, 5, 6)]
+ Unpackage:  
`age, income = "32, 120000".split(',')`  
`a, b = (b, a)` ==> Swap a and b

## 7. Dictionary -- a map or hash table
dic = {"key1":value1, "key2":value2, ... }
+ len(dic) ==> number of key-value pairs
+ Add and Modify: `dic['name'] = "Henry Li"`
+ Delete: del dic['name']
+ Search:  
```python
if dic.get('momo'):
    print("no momo key")
else:
    print(dic['momo'])
```
+ l=dic.keys() and l=dic.values()
+ dic.items() => return list of (key,value) tuples
```python
for key,value in user.items():
    print(key)
    print(value)
```
+ Sort dictionary list by key:
```python
users = [{"name":"laowang", "age": 60},{"name":"xiaoming", "age": 10},{"name":"banzhang", "age": 20}]
users.sort(key=lambda x:x['age'])
print(users) 
[{'name': 'xiaoming', 'age': 10}, {'name': 'banzhang', 'age': 20}, {'name': 'laowang', 'age': 60}]
```

## 8. Set -- no deplicate element
a = {11, 22, 33}  
**Note: Set cannot preserve items order.**
#### a. Remove duplicated items in a list
```python
#Use Set to remove the duplicated items in a list
a = [11, 22, 33, 11]
b = set(a)
a = list(b)
>> [33, 11, 22]
```

#### b. Remove duplicated words in a string
```python
#Use set to remove duplicated words in a string
s = "hello hello hello hello hello hello how are you"
words = s.split(" ")
c = set(words)
l = list(c)
s = " ".join(l)
"you are how hello"
```

#### c. Preserving Order
```python
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
#Note that this relies on the fact that set.add() returns None.
```

## 9. If Condition -- no switch in python
If operations: ==, !=, is, is not, and, or, not
```python
if 1 is 3:
    print("How did that happen?")
elif 1 > 3:
    print("Yikes")
else:
    print("All is well with the world")
```

## 10. While loop
```python
x = 0
while (x < 10):
  print(x)
  x += 1
```

## 11. For loop -- designed for handling elements in a list.
```python
for x in range(10):
  if (x is 1):
    continue
  if (x > 5):
    break
  print(x)
```

## 12. Functions
```python
def SquareIt(x):
  return x * x
```
### a. function as a parameter
```python
#pass function as parameter
def DoSomething(f,x):
  return f(x)
print(DoSomething(Square, 3))
``` 
### b. Lambda function -- desinged simple functions.
`lambda <parameters> : <return expression>`  
**lambda function is a simple function without name.**
```python
def test1(a, b):
    return a+b
result1 = test1(11,22)
```
equals:
```python
test2 = lambda a,b:a+b
result2 = test2(11,22)
```
Pass Lambda function as a parameter:
```python
print(DoSomething(lambda x: x * x, 3))
```
### c. Multiple return values -- Return result is a tuple
`return a, b, c` ==> called package
`a,b,c = getValues()` ==> called unpackage

### d. Global Variable
+ Globle variable name beginning with "g_". e.g. g_a
+ Must defined before calling functions. Best practice is to define before defining the functions.
+ To use it in a function, **always** use tag `global` to announce when use them.

### e. Function Comment
Every function needs a comment """xxxxxxx""", so that you can use help(func) method to get the description:
```python
def test():
	"""Description"""
	print("This is a test.")
help(test)
```

### f. Optional Parameters (缺省参数) -- c=33
+ 1). Must put at the tail of parameter list.
+ 2). Comes with a default value.
```python
def test(a, b =22, c=33):
    result = a + b + c
    print("result=%d" %result)
test(11) #=> a=11
test(11,33) #=> a=11, b=33, c=33
test(11, c=44) #=> a=11, b=22. c=44
``` 

### g. Flexiable Parameters (不定长参数) -- \*args, \*\*kwargs
```python
def sum_nums(a, b, c=33, *args, **kwargs):
    print(c)
	print(args)
	print(kwargs)
sum_nums(11,22,66,44,55,task=99,done=89)
```
Result:
```
11
22
66
(44, 55) => 没有名字的放到*args
{'task': 99, 'done': 89} => 有名字的放到*kwargs
```

### h. Package and Unpackage:
```python
A = (44, 55, 66)
B = {"task":99, "done":89}
sum_nums(11, 22, 33, *A, **B)
```

### i. Recursive
```python
def factorial(n):
    '''n! = n * (n-1) * (n-2) * .... * 1'''
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#Result:
factorial(5)
120
```

### j. Convert a string to a fuction -- eval()
```python
func_new = input("请输入一个匿名函数:")
func_new = eval(func_new)
num = test(11,22,func_new)
print(num)
```

## 13. Python Reference
1. In python, a variable is just a lable pointing to an address in memory.
2. The variable doesn't store data.
3. When changing a variable's value:
+ if the variable is mutable, modify the memory.
+ if the variable is inmutable, store the changed value in a new memory space and make variable point to it.
4. a+=a and a = a + a:
```python
a=[100]
id(a)#4443567680
a+=a
id(a)#4443567680
```
```python
a=[100]
id(a) #4442522880
a= a + a
id(a) #4443567680 point to the space where storing[100,100]
```

## 14. Exception
```python
try:
    open("myFile.txt")
except (NameError,FileNotFoundError) as e:
    print(e)
except Exception as e:
    raise #Will always catch any exception
else: 
    print("Will be executed when there's no exception")
finally: #都会被执行
    print("Will always be executed")
```

## 15. Pass parameters to Python program -- sys.argv
```python
'''
Usage: 
python pass_args.py henry
>> ['pass_args.py', 'henry']
>> Welcome henry
'''
import sys
print(sys.argv)
name = sys.argv[1] # 0->program file, 1->first parameter, ....  
print("Welcome %s" %name)
```

## 16. File Operation
#### a. Open a file: `f = open(filepath, mode)` "r", "w+", "a", "rb"  
#### b. Close a file: `f.close`
#### More elegant way:
```python
with open('path/to/file.txt', "r") as fp:
    # do stuff with fp
```
#### c. Read a file:
+ 1) f.read()  ==> read all content and return a string
+ 2) f.read(1) ==> read one byte
+ 3) f.readlines(hint) ==> return a list containing each line's content
+ 4) f.readline(hint) ==> return one line
Example:
```python
filepath = "README.md"
newFilepath = "copy_test.txt"
try:
	with open(filepath, "r") as large_file:
		with open(newFilepath, "w") as new_file:
			#Read data from a large file and write it into a new file
			while True :
				content = large_file.read(1024)
				if len(content)==0:
					break
				new_file.write(content)
except Exception as e:
	raise e
```

#### d. Write content: `f.write("ssssss\n")`
#### e. f.seek(move_steps, start_point)
+ f.seek(0,0) ==> return to the beginning
+ f.tell() ==> return current position

#### f. Other operations
+ Rename:
```python
import os
os.rename("file_org.txt", "file_rename.txt")
```
+ Remove:
```python
os.remove("myfile.txt")
```
+ Create Director:
```python
os.mkdir("path")
```
+ Remove Directory
```python
os.rmdir("path")
```
+ list files under a directory
```python
os.listdir("./")
```
+ Change Directory
```python
os.changedir("../")
```

## 17. Python OOP
### a. Default methods: `__new__(cls)`,`__init__(self,...)`,`__str__(self)`,`__del__(self)`
### b. Public attributes and methods: `self.attr=xxx` and `def foo(self):`
### c. Private attributes and methods: `self.__age=0` and `def __sendMsg():`
### d. Class attributes and methods: `num = 0` and `@classmethod def add_num(cls):`
### e. Static method: `@staticmethod def printMenu():`
### f. Class reference: self, super(), cls
## Example:
```python
class Animal(object):
    """docstring for Animal"""

    def __init__(self, spicy, name, age):
        super(Animal, self).__init__()
        #define public attributes
        self.spicy = spicy 
        self.name = name
        #define private attributes
        self.__age = age

    def __str__(self):
        return ("%s is a %s" %(self.name,self.spicy))

    def __del__(self):
        print("----%s is dead----" %(self.name))

    #private method
    def __sendMsg(self):
        print("%s is saying hello to you" %self.name)

    #public methods 
    def bark(self):
        print("%s is barking" %self.name)
        #call private method
        self.__sendMsg()

    def drink(self):
        print("%s is drinking" %self.name)

    def getAge(self):
        return self.__age

class Cat(Animal):
    """docstring for Cat"""
    # Define class attribute
    instance_num = 0

    def __init__(self, name, age):
        super(Cat, self).__init__("cat", name, age)
        #Use class attribute
        Cat.instance_num += 1

    def __str__(self):
        return super().__str__()

    def __del__(self):
        super().__del__()

    # Define class attribute
    @classmethod
    def add_num(cls):
        cls.instance_num += 1

    def catch(self):
        print("%s can catch mouse." %self.name)

class Dog(Animal):
    """docstring for Dog"""
    def __init__(self, name, age):
        super(Dog, self).__init__("dog", name, age)
    
    # Overwrite parent method 
    def bark(self):
        print("%s is barking loudly." %self.name)
        
    def bark_parent(self):
        super().bark()

    # Define a static method
    @staticmethod
    def test():
        print("show how to define a static method")

# Create a cat instance and a dog instance.
cat = Cat("miaomiao", 3)
dog = Dog("wangwang", 4)

# Test __str__(self) method
print(cat)

#Visit public attributes
print(cat.name)

#Call public method
cat.bark()

#Visit class attribute
print(Cat.instance_num)
print(cat.instance_num)

# Call class method
Cat.add_num()
cat.add_num()
print(Cat.instance_num)

# Test __del__(self) method
del cat

# Create an animal instance
animal = Animal("animal","animal",0)
animal = dog
animal.bark()

# call static method
animal.test()
```

## 18. Singleton
```python
class Tool(object):
    """Singleton Example"""
    singleton = None
    name = None
 
    def __new__(cls):
        if not cls.singleton:
            cls.singleton = object.__new__(cls)
        return cls.singleton
 
    def __init__(self, name):
        if not Tool.name:
            Tool.name = name
 
a = Tool()
print(id(a))
 
b = Tool()
print(id(b))
b = Tool()
print(id(b))
```