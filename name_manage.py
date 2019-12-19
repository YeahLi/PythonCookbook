#名字管理系统 ==> 用于对 list 的练习

#Define globe variables
names = [] #Define an empty name list.

def printMenu():
	print("="*50)
	print("Name Management System")
	print("1: Add a new name")
	print("2: Delete a name")
	print("3: Modify a name")
	print("4: Search a name")
	print("0: Exit")
	print("="*50)

while True:
	#1. 打印功能提示
	printMenu()
	#2. 获取功能选择
	num_str = input("Please input function number:")
	
	#Check if input is a number.
	if not num_str.isdigit():
		print("Invalid input! The function number must be a number.")
		continue
	else:
		num = int(num_str)
		
	#3. 根据用户的选择，执行相应的功能
	if num == 1:
		new_name = input("Please input the new name:")
		names.append(new_name)
		pass
	elif num == 2:
		del_name = input("Pleae input the name to be deleted:")
		names.remove(del_name)
		pass
	elif num == 3:
		modify_name = input("Please input the name to be modified")
		isFind = False
		i = 0
		for name in names:
			if name == modify_name:
				replaced_name = input("Please input the new name:")
				names[i]=replaced_name
				isFind = True
				print(names)
				pass
			i+=1
		if not isFind:
			print("The name %s is not in system" %(modify_name))
			pass

	elif num == 4:
		find_name = input("Please input the name to find:")
		if find_name in names:
			print("%s is in names" %(find_name))
		else:
			print("%s not in names" %(find_name))
		pass
	elif num == 0:
		break;
	else:
		print("Your input is invalid, please input again.")


