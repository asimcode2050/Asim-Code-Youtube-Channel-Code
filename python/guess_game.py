import random
rand_value = random.randint(0,100)

while True:
    choice = input('Please enter your guess:')
    try:
        choice = int(choice)
        if choice == rand_value:
            print('You guessed correctly!')
            break
        elif choice > rand_value:
            print('Lower')
        else:
            print('Higher.')
    except ValueError:
        print('Please enter valid choice.')
