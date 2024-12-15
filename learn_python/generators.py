def count_up_to(limit):
    count = 1  # 'count' is a local variable initialized to 1.
    while count <= limit:
        yield count
        count += 1


counter = count_up_to(5)
for number in counter:
    print(number)
