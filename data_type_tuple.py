#tuple 元组，和list非常相似 
#但是 tuple 一旦初始化就不能修改。
#他没有append(),insert()这样的方法

tuple1 = (1,2,3,123.456,'xin','新')

print(tuple1)

#修改tuple----内嵌list

list1 =['小明','小李']
tuple2 = (1,2,3,list1)

print(tuple2)

list1[0]='LiMing'
print(tuple2)