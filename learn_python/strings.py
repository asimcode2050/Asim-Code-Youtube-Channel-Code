sentence = "The quick brown fox jumps over the lazy dog"
length_of_sentence = len(sentence)
print(f"The length of the sentence is {length_of_sentence}")
first_character = sentence[0]
print(f"The first character of the sentence is '{first_character}'")
substring = sentence[:3]
print(f"A substring of the sentence: '{substring}'")
index_of_word = sentence.find("fox")
print(f"The word 'fox' starts at index {index_of_word}")
modified_sentence = sentence.replace(
    "lazy", "sleepy")  # Replaces "lazy" with "sleepy"
print(f"Modified sentence: {modified_sentence}")
uppercase_sentence = sentence.upper()
print(f"Uppercase version of the sentence: {uppercase_sentence}")
lowercase_sentence = sentence.lower()
print(f"Lowercase version of the sentence: {lowercase_sentence}")
count_o = sentence.count("o")  # Count the occurrences of the letter 'o'
print(f"The letter 'o' appears {count_o} times in the sentence.")
starts_with_the = sentence.startswith("The")
ends_with_dog = sentence.endswith("dog")
print(f"Does the sentence start with 'The'? {starts_with_the}")
print(f"Does the sentence end with 'dog'? {ends_with_dog}")
