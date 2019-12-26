Create a package:
	1. Create a package directory called HenryUtilities
	2. Create a file named as __init__.py: HenryUtilities/__init__.py
	3. vi __init__.py
		__all__ = ["myUtilities"] ==> 用于规定能使用的模块
		from . import myUtilities ==> import 之后可以使用 HenryUtilities.myUtilities.is_number()
	4. Create a testing file:
		import HenryUtilities
		HenryUtilities.myUtilities.is_number()

Release a package

	1. touch setup.py
	2. vi setup.py
	from distutils.core import setup
	 
	setup(name="HenryUtilities", version="1.0", description="My own module to quickly use some common functions in development.", author="Henry Li", py_modules=['HenryUtilities.myUtilities'])
	
	3. python setup.py build	

	4. python setup.py sdist ==> 生成压缩包 

	5. Install: 
	tar -xzvf HenryUtilities-1.0.tar.gz
	sudo python setup.py install
