# Python System Programming -- Multitasking

## 1. Process
Process is the running program, it will cost system's resource like CPU, memory, disk, etc.
+ It must have a main process and may have some child process.
+ The main process will not wait until its children processes are done.
+ There no executing order between main process and child processes.

## 2. Create a process
```python
#1. import multiprocessing module
from multiprocessing import Process
import time

#2. Defin task function
def test():
	while True:
		print("----test----")
		time.sleep(1)

#3. Create a Process instance and pass task as parameter trager
p = Process(target=test)

#4. Start the process.
p.start()
```
Using `Process` to create a process will exit when child processes get finished.
`p.join(timeout)` ==> main process will suspend and continue after child processes get finished
`p.run()` ==> start process
`p.terminate()` ==> terminate the process immediately

## 3. Override run() of class Process
```python
# 1. import multiprocessing module
from multiprocessing import Process
import time

# 2. Define a subclass of Process
class MyNewProcess(Process):
	"""docstring for MyNewProcess"""
	def __init__(self, arg):
		super(MyNewProcess, self).__init__()
		self.arg = arg

	#3. Overwrite the run() function
	def run(self):
		while True:
			print("---test----")
			time.sleep(1)

#4. Create your class instance and call run function.
p = MyNewProcess()
p.run()
```

## 4. os.getpid() and os.getppid()

## 5. Process Pool
```python
from multiprocessing import Pool

#1. Define task function
def worker(msg):
	print("%s working" %msg)
	return msg

#2. Define a process pool with maximum process number.
#Note: The thread pool must be defined after the function.
pool = Pool(3) 

#3. Add tasks to process pool
# Note: If the number for tasks exceeds pool's max number, the pool wil execute the max number of processe. The process not statred will start after some proecesses are finished. 
p1 = pool.apply_async(worker, ("hello",))
#pool.apply(worker, ("hello",)) #阻塞的方式添加任务，会等待上一个任务结束后再执行。 几乎不用！

#4. Close the process pool, and no more tasks can be added into it.
pool.close() 

#5. Wait until subprocess get finished.
pool.join()

#6. Get the result of child process.
print(p1.get())
```

## 6. Process Communication -- Queue
```python
from multiprocessing import Queue
queue = Queue(3) #initialize a queue with size 3
queue.put("msg1") #put message
msg = queue.get(True) #get message
queue.empty()
queue.full()
```

**Producer and consumer decouple design**
```python
from multiprocessing import Process, Queue
import os, time, random

def write(q):
	'''send msg to queue'''
	for value in ['A','B','C']:
		print("Put %s in queue" %value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	'''get message from the queue'''
	while True:
		if not q.empty():
			value = q.get(True)
			print("Get %s from queue." %value)
			time.sleep(random.random())
		else:
			break

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.join()
```
## 7. Communition betwen processes in a Process Pool
```python
from multiprocessing import (Manager, Pool, Queue)
q = Manager().Queue()
```

## 8. Thread
+ Tread is used to execute Process. It is the unit of system sheduling.
+ Prcess occupies system resource, but thread doesn't. Threads share the resources of a process.
+ A process can have one(main thread) or more than one threads.

## 9. Create a thead -- threading module
```python
from threading import Thread #1. import Thread class
import time
def test():
	print("---test---") #2. define a thrad worker
	time.sleep(1)

for x in range(5):
	t = Thread(target=test) #3. Create a Thread instance
	t.start() #4. start thread
```

## 10. Inherit Thread class to overwrite run() function
```python
from threading import Thread
import time

class MyThread(Thread):
	def run(self):
		for i in xrange(1,3):
			time.sleep(1)
			msg = "I'm " + self.name + ' @ ' + str(i) #name stores current thead's name, defined in Thread
			print(msg)
	
	if __name__ == '__main__':
		myThread = MyThread()
		myThread.start()
```

## 11. Synchronize -- Mutex(互斥锁)
+ Classs Lock: from threading import Lock
+ Create lock: mutex = Lock(L)
+ Add lock: mutex.acquire(timeout=-1)
+ Release lock: mutex.release()
+ **Add mutext lock will make the program from multitasking back to one task mode, so the acquire() and release() functions shoule be the smaller the better.**

```python
from threading import Thread, Lock
import time

g_num = 0 #shared global resource
mutex = Lock() #Create a mutex lock instance. By default, it is unlocked.

def test1():
	global g_num
	for i in range(100000):
		#If the mutex is locked, the other threads will be blocked here until they get access to use the lock.
		mutex.acquire()
		g_num += 1
		mutex.release() #release the lock and notify other blocked threads.
	print("---test1---g_num=%d" %g_num)

def test2():
	global g_num
	for i in range(100000):
		mutex.acquire()
		g_num += 1
		mutex.release()
	print("---test2---g_num=%d" %g_num)

t1 = Thread(target=test1)
t2 = Thread(target=test2)
t1.start()
t2.start()
```

## 12. Deadlock

### How to avoid deadlock?
	+ Add timeout when add lock: `mutex.acquire(timeout=5)`
	+ Use banker's algorithm -- avoid deadlock

### Example of deadlock:
```python
from threading import Thread, Lock

num_1 = 100
num_2 = 100

mutex1 = Lock()
mutex2 = Lock()

def test1():
	global num_1
	global num_2
	
	mutex1.acquire()
	num_1 += 1
	mutex2.acquire()
	num_2 += 2
	mutex2.release()
	mutex1.release()

def test2():
	global num_1
	global num_2
	
	mutex2.acquire()
	num_2 += 1
	mutex1.acquire()
	num_1 += 2
	mutex1.release()
	mutex2.release()
```
## 13. Producer and Consumer Mode --  decouple & message queue
	应用: 处理数据生成不匹配的方式 例如爬虫.
		 不同主机上的相同程序通讯可以用 message queue 或者 一个文件.
```python
#encoding=utf-8
from threading import Thread
import time

#python2中
#from Queue import Queue

#python3中
from queue import Queue

class Producer(Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 100: #低于 100 开始生产
                for i in range(100):
                    count = count +1
                    msg = '生成产品'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100: #高于 100 开始消费
                for i in range(3):
                    msg = self.name + '消费了 '+queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    queue = Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))
        
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
```

## 14 Synchronize and Asynchronize of a process
### Concept:
    + 同步就是协同步调， 按预定的先后次序进行运行 -- 堵塞
    + 异步不需要等，可以做其他东西，当收到通知时再执行 -- 非堵塞

### Synchronize garantee the program was excuted in order.

### Asynchronize CallBack(异步回调)
	Callback的理解：主进程正在做某件事情，突然来了一件更需要立刻去做的事情.
```python
from multiprocessing import Pool
import time, os

def test():
	print("Process pid=%d, ppid=%d" %(os.getpid(), os.getppid()))
	for x in range(3):
		print("---%d---" %(x))
		time.sleep(1)
	return "hahahaha" #provide result as parameter to the callback funciton test2()

def test2(args): #define callback function
	print("---callback func -- pid = %d" %os.getpid())
	print("---callback func--args=%s" %args)

pool = Pool(3)
pool.apply_async(test,callback=test2)

print("----Mian Process-pid=%d----"%os.getpid())

pool.close()
pool.join() #waiting child process get finished.
```

## 15. threading.local(): specify the global variable cannot be shared among threads.
```python
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread-B')
t1.start()
t2.start()
``` 

#16. GIL (线程锁) -- 了解而已
Python里的多线程是假的,python线程共用一个 cpu core. 因此Python 中进程的效率比线程高得多.
	
解决 GIL 问题, 可以让python 启动 C 代码线程:
```python
from ctypes import *
from threading import Thread

#加载动态库
lib = cdll.LoadLibrary("./libdeadloop.so")

#创建一个子线程，让其执行ｃ语言编写的函数，此函数是一个死循环
t = Thread(target=lib.DeadLoop)
t.start()

#主线程，也调用ｃ语言编写的那个死循环函数
#lib.DeadLoop()

while True:
	pass
```