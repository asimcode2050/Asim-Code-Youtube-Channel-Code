from collections import namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point coordinates: x={p.x}, y={p.y}")
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(f"Deque after modifications: {dq}")
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter = Counter(items)
print(f"Item counts: {counter}")
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(f"OrderedDict: {ordered_dict}")
default_dict = defaultdict(int)
default_dict['apple'] += 1
default_dict['banana'] += 2  # Same for 'banana'
print(f"DefaultDict: {default_dict}")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = ChainMap(dict1, dict2)
print(f"ChainMap: {chain_map}")
print(f"Value for 'b': {chain_map['b']}")
