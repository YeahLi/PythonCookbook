# Python System Programming -- Multitasking

## 1. Process
Process is the running program, it will cost system's resource like CPU, memory, disk, etc.
+ It must have a main process and may have some child process.
+ The main process will not wait until its children processes are done.
+ There no executing order between main process and child processes.

## 2. Create a process
```python
from multiprocessing import Process
import time

def test():
	while True:
		print("----test----")
		time.sleep(1)
	
p = Process(target=test)
p.start()
```
Using `Process` to create a process will exit when child processes get finished.
`p.join(timeout)` ==> main process will suspend and continue after child processes get finished
`p.run()` ==> start process
`p.terminate()` ==> terminate the process immediately

## 3. Override run() of class Process
```python
from multiprocessing import Process
import time

class MyNewProcess(Process):
	"""docstring for MyNewProcess"""
	def __init__(self, arg):
		super(MyNewProcess, self).__init__()
		self.arg = arg

	def run(self):
		while True:
			print("---test----")
			time.sleep(1)

p = MyNewProcess()
p.run()
```

## 4. os.getpid() and os.getppid()

## 5. Process Pool
```python
from multiprocessing import Pool

def worker(msg):
	print("%s working" %msg)

#The thread pool must be defined after the function.
pool = Pool(3) #定义一个进程池，maximum number of child processes are 3， 必须在函数后面定义
pool.apply_async(worker, ("hello",)) #向进程池中添加任务
							#注意： 如果添加的任务数量超过了进程池中进程的个数，那么不会导致添加不进去
							#添加到进程池中的任务，如果还没被执行的话，那么此时 他们会等待进程池中的进程完成一个任务之后，会自动的去用刚刚的那个进程 完成当前的新任务
apply_async().get() 方法可以得到进程函数的返回值。

pool.close() #关闭进程池，相当于不能够再次添加新任务了
pool.join() #主进程创建/添加任务后，主进程不会等待进程池中的任务执行完成后才结束， 而是当主进程的任务做完之后立马结束。

主进程一般用来等待，，，，真正的任务都在子进程中执行

pool.apply(worker, ("hello",)) #阻塞的方式添加任务，会等待上一个任务结束后再执行。 几乎不用！
```