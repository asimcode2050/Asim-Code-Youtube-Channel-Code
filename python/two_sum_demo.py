def two_sum(arr,target):
    dic ={}
    for i , num in enumerate(arr):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None

num = [2,7,11,15]
target = 18
print(two_sum(num,target))