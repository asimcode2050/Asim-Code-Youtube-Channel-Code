list1= [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = ['6','7','8','9','10']
print([(i,j) for i, j in zip(list1,list2)])

print([(i,j,k) for i,j,k in zip(list1,list2,list3)])
