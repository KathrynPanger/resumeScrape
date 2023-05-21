import re
from stop_words import get_stop_words

def words(text: str):
    text = text.lower()
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    wordList = re.split('; |, |\*|\n| ', text)
    wordList = [word for word in wordList if word not in get_stop_words('en')]
    return wordList

def frequencies(wordList):
    frequencies = {}
    for word in wordList:
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    return frequencies