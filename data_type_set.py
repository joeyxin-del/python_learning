#set---集合 无序不重复元素集

set1 = set([1,2,3,4,5,6])
print(set1)
set2 = set([6,7,8,9])
print(set2)

set3 = set1 & set2;#交集
set4 = set1 | set2;#并集
set5 = set1 - set2;#差集
set6 = set2 - set1;#差集

print(set3)
print(set4)
print(set5)
print(set6)