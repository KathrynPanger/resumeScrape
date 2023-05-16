import re

def clean_text(text: str):
    #make all words lower case
    text = text.lower()
    # remove new line character
    text = text.replace("\n", "")
    # remove non-alphanumeric characters
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return text