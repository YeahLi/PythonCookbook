class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

class Gun(object):
	"""docstring for Gun"""
	def __init__(self, model):
		super(Gun, self).__init__()
		self.model = model
		
class Charger(object):
	"""docstring for Chager"""
	def __init__(self, capacity):
		super(Chager, self).__init__()
		self.capacity = capacity


class Bullet(object):
	"""docstring for Bullet"""
	def __init__(self, harm):
		super(Bullet, self).__init__()
		self.harm = harm

def main():
	'''用来控制整个程序的流程'''
	#1. 创建一个人 -- 老王对象
	laowang = Person("老王")

	#2. 创建一把枪 -- 枪对象
	ak47 = Gun("AK47")

	#3. 创建一个弹夹 -- 弹夹对象
	charger = Chager(20)

	#4. 创建一些子弹 -- 子弹对象
    bullet = Bullet(10)

	#5. 创建一个敌人 -- 敌人对象
	enemy = Person("敌人")

	#6. 老王用子弹填满弹夹
	#7. 给枪安装弹夹
	#8. 开枪怼敌人

if __name__ == '__main__':
	main()