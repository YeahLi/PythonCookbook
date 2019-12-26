#global variables
users = []
user_db = "user_db.data"

#def fucntions
def printMenu():
	'''Print the menu'''
	print("Name Management System")
	print("1: Add a new name")
	print("2: Delete a name")
	print("3: Modify a name")
	print("4: Search a name")
	print("5: Show all users")
	print("0: Exit")

def saveToFile(file, content):
	'''try:
		f = open(file, "w")
		f.write(content)
	except Exception as e:
		raise e
	finally:
		f.close()'''
	with open(file, "w") as f:
		f.write(content)


def addNewUser():
	'''Add user to users list'''
	global users
	global user_db

	new_name = input("Please input new user\'s name:")
	new_email = input("Please input new user\'s email:")
	new_phone = input("Please input new user\'s phone number:")
	new_company = input("Please input new user\'s company:")

	#Define a new dictionary variable
	new_user = {}
	new_user['name'] = new_name
	new_user['email'] = new_email
	new_user['phone'] = new_phone
	new_user['company'] = new_company
	users.append(new_user)
	#print(new_user)
	saveToFile(user_db, str(users))

def printUserInfo(user):
	'''Print a user's information '''
	print("%s: %s, %s, %s" %(user['name'], user['email'], user['phone'], user['company']))

def findUser():
	'''Find the user information by username'''
	global users

	find_name = input("Please input search user\'s name:")
	find_results = []
	for user in users:
		if find_name == user['name']:
			find_results.append(user)
		pass
	if not find_results:
		print("Cannot find the user with name %s" %find_name)
	else:
		print("search result:")
		for user in find_results:
			printUserInfo(user)

def loadUserDB():
	global user_db
	global users
	
	try:
		with open(user_db,"r") as f:
			users = eval(f.read())
	except FileNotFoundError:
		pass
	except Exception as e:
		raise e
	

def main():
	print("Loading users....")
	loadUserDB()
	print("Loading users finished.")
	while True:
		#1. print menu
		printMenu()
		#2. Input menu choose number
		num_str = input("Please input function number:")
		#Check if input is a number.
		if not num_str.isdigit():
			print("Invalid input! The function number must be a number.")
			continue
		else:
			num = int(num_str)

		#3. execute user's choice
		if num == 1:
			addNewUser()
		elif num == 2:
			pass
		elif num == 3:
			pass
		elif num == 4:
			findUser()
		elif num == 5:
			for user in users:
				printUserInfo(user)

		elif num == 0:
			break
			pass
		else:
			print("Your input is invalid, please input again.")

if __name__ == '__main__':
	main()