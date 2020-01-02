'''
1. Define copy size per time.
2. Generate a process pool
3. Define a copy function, copy 2M.
4. start processes to execute the copy function
'''
from multiprocessing import Pool
import time

process_num=5
copy_unit=20
pos=0


def test(file_path, new_file_path,pos):
	try:
		with open(file_path, "r") as file:
			file.seek(pos,0)
			content = file.read(copy_unit)
			print("----read from %d ----" %pos)
			if not content:
				return True	
			with open(new_file_path,"a") as new_file:
				new_file.seek(pos,0)
				new_file.write(content)
				print("----write to %d ----" %file.tell())
				return False
	except Exception as e:
		raise e

pool = Pool(process_num) #Pool must put after function

while True: 
	#print(pos)
	ret = pool.apply_async(test,("./test.py", "./test_new.py", pos)).get()
	if ret:
		break
	pos+=copy_unit
	time.sleep(1)

pool.close()
pool.join()