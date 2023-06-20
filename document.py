from typing import List
import PyPDF2
import re
import uuid
from pdfquery import PDFQuery
from helper import words, frequencies
import re



class Document():
    def __init__(self, path: str):
        self.path = path
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

    # def frequency_match(self, word_list: List[str]):
    #     score = 0
    #     for word in word_list:
    #         if word in self.frequencies:
    #             frequency = self.frequencies[word]
    #             score += frequency
    #     return score

    # def one_hot(self, comparison_vector: List[str]):
    #     one_hot_map = []
    #     for word in self.corpus:
    #         # Append a 1 in the words place if the word is in the comparison text
    #         one_hot_map.append(int(word in comparison_vector))
    #
    # def proportion_match(self, job_description:str):
    #     cv = CountVectorizer()
    #     count_matrix = cv.fit_transform(self.corpus, job_description)
    #     proportion_match = cosine_similarity(count_matrix)[0][1]
    #     return proportion_match


    def __repr__(self):
        return (f"Document(path = {self.path}, id = {self.id})")


