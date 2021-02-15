'''
但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含 1000 万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？

这样就不必创建完整的 list，从而节省大量的空间。
在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。
并在下一次执行 next()方法时从当前位置继续运行。
'''

#生成器的创建
gen=(x*x for x in range(5))
print(gen)
for num in gen:
	print(num, end=' ')
print('')

#以函数的形式实现生成器

def fibon(n):
	a=b=1
	for i in range(n):
		yield a
		a, b=b,a+b

for x in fibon(10):
	print(x,end =' ')
print()


def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()
print( next( o ) )
print( next( o ) )
print( next( o ) )