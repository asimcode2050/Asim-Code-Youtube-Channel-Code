my_tuple = (10, "Hello", 3.14, True)
first_item = my_tuple[0]
last_item = my_tuple[-1]  # Negative indexing starts from the end of the tuple.
subset_of_tuple = my_tuple[1:3]
contains_hello = "Hello" in my_tuple
for item in my_tuple:  # Loops through the tuple and prints each element
    print(item)  # Prints each item in the tuple. Output will be: 10, Hello, 3.14, True
index_of_hello = my_tuple.index("Hello")
count_of_hello = my_tuple.count("Hello")
length_of_tuple = len(my_tuple)
another_tuple = (5, "World")
combined_tuple = my_tuple + another_tuple
repeated_tuple = my_tuple * 2  # Repeats the elements of my_tuple twice.
print("First item:", first_item)  # This will print: First item: 10
print("Last item:", last_item)  # This will print: Last item: True
print("Subset of tuple:", subset_of_tuple)
print("Contains 'Hello':", contains_hello)
print("Index of 'Hello':", index_of_hello)
print("Count of 'Hello':", count_of_hello)
print("Length of tuple:", length_of_tuple)
print("Combined tuple:", combined_tuple)
print("Repeated tuple:", repeated_tuple)
