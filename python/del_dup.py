InList = [2,3,4,2,4,1,8,9,8]
OutList = [item for item in InList if InList.count(item) ==1]
print(OutList)