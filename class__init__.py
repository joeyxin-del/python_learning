class class1():
	def __init__(self):
		print('实例化成功')

	def __del__(self):
		print('实例化销毁了')


A=class1()
del A