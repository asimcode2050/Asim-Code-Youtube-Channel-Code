from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['a'])  # Outputs 1, found in dict1
print(chain['b'])
print(chain['c'])  # Outputs 4, found in dict2 (because dict1 doesn't have 'c')
chain['a'] = 10
print(dict1['a'])
chain['d'] = 5
print(dict1)
chain2 = ChainMap(dict1, dict2)
print(chain2['d'])  # Outputs 5, found in dict1 now
dict3 = {'e': 6}
chain3 = ChainMap(dict1, dict2, dict3)
print(chain3['e'])  # Outputs 6, found in dict3
