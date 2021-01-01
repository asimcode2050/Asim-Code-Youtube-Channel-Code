import scrabble
vowels = "aeiou"
def has_vowels(w):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True

for word in scrabble.wordList:
    if has_vowels(word):
        print(word)