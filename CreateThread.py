#Method 1:
from threading import Thread #1. import Thread class
import time
def test():
	print("---test---") #2. define a thrad worker
	time.sleep(1)

for x in range(5):
	t = Thread(target=test) #3. Create a Thread instance
	t.start() #4. start thread

#Method 2:
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

# Mutex:
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