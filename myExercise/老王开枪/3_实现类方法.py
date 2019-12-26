class Person(object):
	"""docstring for Person"""
	def __init__(self, name, hp):
		super(Person, self).__init__()
		self.name = name
		self.hp = hp

	def installBullet(self,charger,bullet):
		if not charger.addBullet(bullet):
			print("弹夹已满, 不能继续添加.")
			return False
		else:
			return True

	def installCharger(self, gun, charger):
		if not gun.addCharger(charger):
			print("无法更换, 已有弹夹.")
			return False
		else:
			return True

	def shot(self, gun, enemy):
		print("%s用%s开枪打%s!" %(self.name,gun.model,enemy.name))
		bullet = gun.shot()
		if bullet:
			bullet.injure(enemy)

	def __str__(self):
		return "%s剩余血量: %d" %(self.name, self.hp)

class Gun(object):
	"""docstring for Gun"""
	def __init__(self, model):
		super(Gun, self).__init__()
		self.model = model
		self.charger = None

	def addCharger(self, charger):
		if not self.charger:
			self.charger = charger
			return True
		else:
			return False

	def __str__(self):
		if self.charger:
			return "枪的信息: %s, %s" %(self.model, self.charger)
		else:
			return "枪的信息: %s, 没有安装弹夹" %(self.model)

	def shot(self):
		if self.charger:
			if len(self.charger.bullets) > 0:
				return self.charger.bullets.pop()
			else:
				print("子弹用尽,请更换弹夹")
				return None
				
		else:
			print("无法开枪,没有弹夹.")
			return None
		
class Charger(object):
	"""docstring for Chager"""
	def __init__(self, capacity):
		super(Charger, self).__init__()
		self.capacity = capacity
		self.bullets = []

	def addBullet(self, bullet):
		if len(self.bullets) <= self.capacity:
			self.bullets.append(bullet)
			return True
		else:
			return False

	def __str__(self):
		return "弹夹信息: 子弹个数 %d/%d" %(len(self.bullets), self.capacity)

class Bullet(object):
	"""docstring for Bullet"""
	def __init__(self, harm):
		super(Bullet, self).__init__()
		self.harm = harm
	
	def injure(self, enemy):
		if enemy.hp > 0:
			enemy.hp -= self.harm
			print(enemy)
		else:
			print("%s 已死,切勿鞭尸" %(enemy.name))

def main():
	'''用来控制整个程序的流程'''
	#1. 创建一个人 -- 老王对象
	laowang = Person("老王", 100)

	#2. 创建一把枪 -- 枪对象
	ak47 = Gun("AK47")

	#3. 创建一个弹夹 -- 弹夹对象
	charger = Charger(20)

	#4. 创建一些子弹 -- 子弹对象
	bullet = Bullet(10)

	#5. 创建一个敌人 -- 敌人对象
	enemy = Person("敌人", 100)

	#6. 老王用子弹填满弹夹

	laowang.installBullet(charger,bullet)
	
	#7. 给枪安装弹夹
	laowang.installCharger(ak47, charger)

	#print(ak47.charger)
	#print(ak47)

	#8. 老王开枪怼敌人
	laowang.shot(ak47,enemy)

if __name__ == '__main__':
	main()