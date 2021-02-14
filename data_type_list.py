name = ['小明','小王','小李']

print(name[0])
print(name[1])
print(name[2])
print('name的长度=', len(name))

name.append('小贤')

print(name[3])
print('name的长度=', len(name))
del name[0]

print(name[0])

print('name的长度=', len(name))