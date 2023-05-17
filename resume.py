from typing import List
import PyPDF2
import re

class Resume():
    def __init__(self, path: str):
        self.path = path
        self.pdfFileObj = open(f'{path}', 'rb')
        self.pdfReader = PyPDF2.PdfReader(self.pdfFileObj)
        self.pageCount = len(self.pdfReader.pages)
        self.corpus = ""
        self.wordList = []
        self.wordFreqs = {}
        self.searchScores = {}

        for i in range(self.pageCount):
            page = self.pdfReader.pages[i]
            text = page.extract_text()
            self.corpus += f" {text}"

        # Convert corpus to list of unique words, cleaned of special characters
        words = self.corpus.lower()
        words = re.sub(r'[^A-Za-z0-9 ]+', ' ', words)
        words = re.split('; |, |\*|\n| |/|\t|  ',words)
        #words = words.split(" ")
        self.wordList = [item for item in set(words)]

        # Get word frequencies
        for word in words:
            if word not in self.wordFreqs:
                self.wordFreqs[word] = 1
            else:
                self.wordFreqs[word] += 1

        self.pdfFileObj.close()

    @property
    def searchScores(self):
        return self.searchScores

    @searchScores.setter
    def searchScores(self, searchList: list[str]):
        scores = {}
        for item in searchList:
            item = item.lower()
            if item not in scores:
                pass