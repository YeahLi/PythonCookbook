#test if an instance can use if is in
class User(object):
	"""docstring for User"""
	def __init__(self, name):
		super(User, self).__init__()
		self.name = name

user1 = User("haha")
user2 = User("heihei")

l = [user1, user2]

user3 = User("heihei")

print("user %s with id %d" %(user2.name,id(user2)))
print("user %s with id %d" %(user3.name,id(user3)))

if user3 in l:
	print("user %s with id %d is in the list" %(user3.name,id(user3)))
else:
	print("user %s with id %d is NOT in the list" %(user3.name, id(user3)))

'''
Result: in only checks the reference or numbers or strings

user heihei with id 4353266704
user heihei with id 4353266768
user heihei with id 4353266768 is NOT in the list
'''