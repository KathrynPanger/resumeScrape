import re

def words(text: str):
    text = text.lower()
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    textList = re.split('; |, |\*|\n| ', text)
    return textList

def frequencies(wordList):
    frequencies = {}
    for word in wordList:
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    return frequencies