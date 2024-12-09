'''
pip install spacy

Download the en_core_web_sm model: After installing spaCy, you need to download the specific model that spaCy uses for processing English text. 
To do this, run the following command in your terminal or command prompt:

python -m spacy download en_core_web_sm

'''
import spacy
nlp = spacy.load('en_core_web_sm')
sentence = "The quick brown fox jumped over the lazy dog."
doc = nlp(sentence)
for noun_phrase in doc.noun_chunks:
    print(noun_phrase.text)
