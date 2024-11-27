numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers_list = list(even_numbers)
squared_even_numbers = map(lambda x: x ** 2, even_numbers_list)
squared_even_numbers_list = list(squared_even_numbers)
print("Even numbers:", even_numbers_list)  # Shows the list of even numbers
print("Squared even numbers:", squared_even_numbers_list)
