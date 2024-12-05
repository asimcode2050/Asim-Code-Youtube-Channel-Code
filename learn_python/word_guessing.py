import random
word_list = ['python', 'java', 'ruby', 'javascript',
             'html', 'css', 'django', 'flask', 'react']


def choose_word():
    return random.choice(word_list)


def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    guessed = False
    print("Welcome to the Word Guessing Game!")
    print("You have to guess the word, one letter at a time.")
    print("The word has", len(word), "letters.")
    while attempts > 0 and not guessed:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue  # Skip to the next loop iteration and ask the player for a valid input
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue  # Skip this guess and move on to the next loop iteration
        guessed_letters.append(guess)
        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! The letter '{guess}' is not in the word.")
        if all(letter in guessed_letters for letter in word):
            guessed = True
    if guessed:
        print(f"\nCongratulations! You guessed the word: {
              word}")  # If guessed, show congratulations
    else:
        print(f"\nSorry, you're out of attempts! The word was: {
              word}")  # If not guessed, reveal the word


if __name__ == "__main__":
    play_game()
