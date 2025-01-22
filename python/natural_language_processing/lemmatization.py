import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
lemmatizer = WordNetLemmatizer()
sentence = "The striped cats are running faster than the striped cat."
words = nltk.word_tokenize(sentence)
print("Words:", words)  # Prints the list of words.
''' ['The', 'striped', 'cats', 'are', 'running', 'faster', 'than', 'the', 'striped', 'cat'] '''
def get_pos_tag(word):
    tag = nltk.pos_tag([word])[0][1]

    if tag.startswith('NN'):
        return wordnet.NOUN  # Return WordNet's constant for noun.
    elif tag.startswith('VB'):
        return wordnet.VERB  # Return WordNet's constant for verb.
    elif tag.startswith('JJ'):
        return wordnet.ADJ
    else:
        return wordnet.NOUN

lemmatized_words = [
    lemmatizer.lemmatize(word, get_pos_tag(word))
    for word in words
]
print("Lemmatized Words:", lemmatized_words)
