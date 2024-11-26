my_set = {1, 2, 3}
print("Initial set:", my_set)  # Output will be: {1, 2, 3}
my_set.add(4)
print("Set after adding 4:", my_set)  # Output will be: {1, 2, 3, 4}
my_set.add(2)
print("Set after trying to add 2 again:", my_set)
my_set.remove(3)
print("Set after removing 3:", my_set)  # Output will be: {1, 2, 4}
my_set.discard(5)
print("Set after discarding 5 (which is not in the set):",
      my_set)  # Output will still be: {1, 2, 4}
my_set.clear()
print("Set after clearing all elements:", my_set)  # Output will be: set()
another_set = {3, 4, 5, 6}
print("Another set:", another_set)  # Output will be: {3, 4, 5, 6}
union_set = my_set | another_set  # Or you could use my_set.union(another_set)
print("Union of my_set and another_set:", union_set)
intersection_set = my_set & another_set
print("Intersection of my_set and another_set:",
      intersection_set)  # Output will be: {4}
difference_set = my_set - another_set
print("Difference between my_set and another_set:",
      difference_set)  # Output will be: {1, 2}
symmetric_diff_set = my_set ^ another_set
print("Symmetric difference between my_set and another_set:",
      symmetric_diff_set)  # Output will be: {1, 2, 5, 6}
