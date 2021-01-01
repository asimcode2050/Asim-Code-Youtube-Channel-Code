import difflib
dictionary = {'hello', 'about','amount',
'world','any'}
def spell_suggest(phrase):
    changes = 0
    words = phrase.split()
    for x , w in enumerate(words):
        if w not in dictionary:
            changes +=1
            matches = difflib.get_close_matches(w,dictionary)
            if matches:
                words[x] = matches[0]
    return changes, ' '.join(words)
print(spell_suggest('hello wold'))