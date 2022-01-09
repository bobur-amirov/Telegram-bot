from uzwords import words
from difflib import get_close_matches


def check_words(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replase('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replase('х','ҳ')
        matches.update(get_close_matches(word, words))

    return {'available':available, 'matches':matches}