from typing import List
import PyPDF2
from helper import clean_text

class Resume():
    def __init__(self, path: str):
        self.path = path
        self.pdfFileObj = open(f'{path}', 'rb')
        self.pdfReader = PyPDF2.PdfReader(self.pdfFileObj)
        self.pageCount = len(self.pdfReader.pages)
        self.corpus = ""
        self.wordFreqs = {}

        for i in range(self.pageCount):
            page = self.pdfReader.pages[i]
            text = page.extract_text()
            self.corpus += text

        # Clean the corpus in preparation for finding word frequencies
        # i.e. remove special characters, make lower case, then convert to list of words
        words = clean_text(self.corpus).split(" ")

        for word in words:
            if word not in self.wordFreqs:
                self.wordFreqs[word] = 1
            else:
                self.wordFreqs[word] += 1

        self.pdfFileObj.close()
