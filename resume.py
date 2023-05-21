from typing import List
import PyPDF2
import re
from pdfquery import PDFQuery
from helper import words, frequencies

class Resume():
    def __init__(self, path: str):
        self.path = path
        self.pdf = PDFQuery(path)
        self.pdf.load()
        self.text_elements = self.pdf.pq('LTTextLineHorizontal')
        self.corpus = ""

        # Extract the corpus from the elements
        for t in self.text_elements:
            self.corpus += f" {t.text}"

        self.words = words(self.corpus)
        self.uniqueWords = set(self.words)
        self.frequencies = frequencies(self.words)
