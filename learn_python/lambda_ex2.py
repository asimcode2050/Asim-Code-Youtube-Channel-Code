'''
 lambda x: x * 2 

  '''
def double(x): return x * 2
result1 = double(5)  # `result1` will store the value of 5 * 2, which is 10.
result2 = double(10)  # `result2` will store the value of 10 * 2, which is 20.
print("Result for 5:", result1)  # Output: "Result for 5: 10"
print("Result for 10:", result2)  # Output: "Result for 10: 20"
numbers = [1, 2, 3, 4, 5]
''' `lambda x: x * 2` to `map` '''
doubled_numbers = map(lambda x: x * 2, numbers)
doubled_numbers_list = list(doubled_numbers)
'''  `lambda x: x * 2` '''
print("Doubled numbers:", doubled_numbers_list)
