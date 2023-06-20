from typing import List
import os
from document import Document
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Briefcase():
    def __init__(self, resumes_directory:str, jobs_directory:str = None):
        self.resumes_directory = resumes_directory
        self.resume_paths = [f"{resumes_directory}/{file}" for file in os.listdir(resumes_directory) if file.split(".")[-1] == "pdf"]
        self.resumes = [Document(path) for path in self.resume_paths]
        if jobs_directory:
            self.job_paths = [f"{jobs_directory}/{file}" for file in os.listdir(jobs_directory) if
                                 file.split(".")[-1] == "pdf"]
            self.jobs = [Document(path) for path in self.job_paths]

    def frequency_match(self, query: List[str], number_to_return: int):
        self.query = [item.lower() for item in query]
        for resume in self.resumes:
            score = 0
            for word in query:
                if word in resume.frequencies:
                    frequency = resume.frequencies[word]
                    score += frequency
            resume.frequency_score = score
        return sorted(self.resumes, key = lambda resume: resume.frequency_score, reverse = True)[: number_to_return]

    def proportion_match(self, job_description: str, number_to_return: int):
        for resume in self.resumes:
            cv = CountVectorizer()
            count_matrix = cv.fit_transform([resume.corpus, job_description])
            proportion_match = cosine_similarity(count_matrix)[0][1]
            resume.proportion_match = proportion_match
        return sorted(self.resumes, key=lambda resume: resume.proportion_match, reverse = True)[: number_to_return]

