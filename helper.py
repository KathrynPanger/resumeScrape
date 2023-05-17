import re

def to_list(text: str):
    #make all words lower case
    text = text.lower()
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    textList = re.split('; |, |\*|\n| ', text)
    return textList