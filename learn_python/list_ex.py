fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits[1] = 'grape'
fruits.insert(2, 'kiwi')
fruits.remove('apple')
removed_fruit = fruits.pop()
index_of_grape = fruits.index('grape')
is_kiwi_present = 'kiwi' in fruits
fruits.sort()
print("Current list of fruits:", fruits)
print("Removed fruit:", removed_fruit)
print("Index of grape:", index_of_grape)
print("Is kiwi in the list?", is_kiwi_present)
