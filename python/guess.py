import random
game_continue = 'true'
secret_number = int(random.randrange(0,100))
#print(secret_number)
while game_continue == 'true':
    guess = int(input('Please Guess a number.'))
    if guess > secret_number:
        print('Your guess is too high, please try again.')
    elif guess < secret_number:
        print('Your guess is too low, please try again.')
    elif guess == secret_number:
        print("You Win!")
        game_continue='false'
