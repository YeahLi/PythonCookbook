#Remember: DON'T use None

#1. Check a string is empty
string = "   "
if not string.strip():
    print ("Empty String!")

#2. Check a list is empty

#In Python, empty list object evaluates to false. Hence following conditional statement can be used to check if list is empty.
a=[] # Empty lists evaluate to False
if not a:
    print ("list is empty")
else:
    print ("list is not empty")

#You can also use len() function. It returns number of elements in a sequence. If len() returns zero, the list is empty
if len(a)==0:
    print ("list is empty")
else:
    print ("list is not empty")

#3. Check a dictionary is empty
dic = {}
if not dic:
	print ("dictionary is empty")
else:
	print ("dictionary is not empty")

#4. Check a instance
dog = None
if not dog:
    print("dog is None or empty")
else:
    print("dog is not None")

#Summary:
def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True
