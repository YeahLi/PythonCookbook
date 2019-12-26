import sys

print(sys.argv)

name = sys.argv[1]

print("Welcome %s" %name)

'''
Usage: 
python pass_args.py henry
>> ['pass_args.py', 'henry']
>> Welcome henry
'''