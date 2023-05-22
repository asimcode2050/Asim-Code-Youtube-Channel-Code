while True:
    value = input("Please enter a number [ q to quit]: ")
    if value == 'q':
        break
    user_number = int(value)
    if user_number % 2 == 0:
        continue
    print(user_number,"squared is",user_number*user_number)

