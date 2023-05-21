from typing import List
import PyPDF2
import re
import uuid
from pdfquery import PDFQuery
from helper import words, frequencies
import re

class Resume():
    def __init__(self, path: str):
        self.path = path
        self.name = path.split("/")[1]
        self.id = str(uuid.uuid4())[:8]
        self.pdf = PDFQuery(path)
        self.pdf.load()
        self.text_elements = self.pdf.pq('LTTextLineHorizontal')
        self.corpus = ""

        # Extract the corpus from the elements
        self.corpus = self.corpus.join(t.text for t in self.text_elements)


        # Get list of words, removing stopwords
        self.words = words(self.corpus)
        self.unique_words = set(self.words)

        # Get remaining word frequencies
        self.frequencies = frequencies(self.words)


    def frequency_score(self, wordList: List[str]):
        score = 0
        for word in wordList:
            if word in self.frequencies:
                frequency = self.frequencies[word]
                score += frequency
        return score

    def __repr__(self):
        return (f"Resume(name = {self.name}, id = {self.id})")