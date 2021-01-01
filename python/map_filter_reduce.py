from functools import reduce
print(list(map(lambda i:i**2, range(10))))
list(map(print,range(10),range(5),range(10)))
evens = filter(lambda num: num %2 ==0,range(10))
print(f"Even numbers: {list(evens)}")
print(reduce(lambda x,y: x+y,[4,4]))