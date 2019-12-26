#Use Set to remove the duplicated items in a list
a = [11, 22, 33, 11]
print(a)
b = set(a)
a = list(b)
print(a)

#Use set to remove duplicated words in a string
s = "hello hello hello hello hello hello how are you"
print(s)
words = s.split(" ")
c = set(words)
l = list(c)
s = " ".join(l)
print(s)

'''
(base) Yes-MacBook-Pro:Desktop Henry$ python test.py 
[11, 22, 33, 11]
[33, 11, 22]
hello hello hello hello hello hello how are you
you are how hello
'''

'''
WHILE PRESERVING ORDER
Use a set to keep track of which elements you’ve seen
At the same time, populate the new list by a list comprehension
'''

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
#Note that this relies on the fact that set.add() returns None.