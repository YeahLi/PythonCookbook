class Tool(object):
	"""Singleton Example"""
	singleton = None

	def __new__(cls):
		if not cls.singleton:
			cls.singleton = object.__new__(cls)
		return cls.singleton

a = Tool()
print(id(a))

b = Tool()
print(id(b))
