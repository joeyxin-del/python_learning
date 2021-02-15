class Class1():
	var1 = 100
	var2 = 0.1
	var3 = 'asdf'


	def fun1(self):
		print('我是fun1')
		print('var1=',self.var1)

	def fun2(self):
		print('我是fun2')
		print('var2=',self.var2)
	
	def fun3(self):
		print('我是fun3')
		print('var3=',self.var3)

A = Class1()#实例化

A.fun1()
A.fun2()
A.fun3()