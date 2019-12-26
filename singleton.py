class Tool(object):
	"""Singleton Example"""
	singleton = None
	name = None

	def __new__(cls):
		if not cls.singleton:
			cls.singleton = object.__new__(cls)
		return cls.singleton

	def __init__(self, name):
		if not Tool.name:
			Tool.name = name

a = Tool()
print(id(a))

b = Tool()
print(id(b))
