def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(3)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
