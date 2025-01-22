import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple is looking at buying U.K. startup for $1 billion. Elon Musk, CEO of SpaceX, supports the deal."
doc = nlp(text)
print("Named Entities, Phrases, and Concepts:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

for ent in doc.ents:
    print(f"Entity: {ent.text} is of type {ent.label_}")

