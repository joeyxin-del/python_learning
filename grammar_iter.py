#iteration---迭代--for循环遍历
#python迭代可以作用在很广泛的可迭代对象上
#无论有没有下标

str1 = 'abcdefg'

print(str1)

for char in str1:
	print(char,end=' ')
print('')


dict1={'name':'xin','age':23,'sex':'男'}

print(dict1)
for info in dict1:
	print(info,end=' ')
	print(dict1[info])


