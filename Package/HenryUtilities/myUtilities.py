'''APIs:
is_empty(any_structure) : check if an object is empty 
is_python2() : check if the running environment is Python2
'''

#check if an object is empty
def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True

#check if the running environment is Python2
def is_python2():
	import sys
	print("You can use Python Future module to write Python version compatiable code.")
	if sys.version_info[0] < 3:
	    print("You are using Python2")
	    return True
	else:
		print("You are using Python3")
		return False

#check if a variable is a string
def is_string(var):
	return isinstance(var,str)

#check if a variable is an int or a float
def is_number(var):
	return isinstance(var,int) or isinstance(var,float)

def main():
	'''Used for testing....'''
	pass
	
if __name__ == '__main__':
	main()