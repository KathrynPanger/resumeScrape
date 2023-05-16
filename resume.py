from typing import List
import PyPDF2

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

        words = self.corpus.split(" ")
        for word in words:
            if word not in self.wordFreqs:
                self.wordFreqs[word] = 1
            else:
                self.wordFreqs[word] += 1

