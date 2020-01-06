#Method 1:
from multiprocessing import Process

def test():
	while True:
		print("----test----")
		time.sleep(1)
	
p = Process(target=test)
p.start()

Process()

#Method 2:
from multiprocessing import Process
import time
class MyNewProcess(Process):
    """docstring for MyNewProcess"""
    def __init__(self):
        super(MyNewProcess, self).__init__()

    def run(self):
        while True:
            print("-----1-----")
            time.sleep(1)
        pass

p = MyNewProcess()
p.run()

#Method 3:
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

# Callback function:
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