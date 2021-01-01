import itertools
p = itertools.product(('A','B','C'),repeat=2)
#print(list(p))
p2 = itertools.permutations(('A','B','C'),2)
#print(list(p2))
p3 = itertools.combinations(('A','B','C'),2)
print(list(p3))
