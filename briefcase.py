from typing import List
import os
from document import Document
from match import Match
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

    def frequency_top_n(self, query: List[str], number_to_return: int):
        self.query = [item.lower() for item in query]
        for resume in self.resumes:
            score = 0
            for word in query:
                if word in resume.frequencies:
                    frequency = resume.frequencies[word]
                    score += frequency
            resume.frequency_score = score
        return sorted(self.resumes, key = lambda resume: resume.frequency_score, reverse = True)[: number_to_return]

    def proportion_top_n(self, job_description: str, number_to_return: int):
        for resume in self.resumes:
           resume.proportion_score = resume.proportion_match(job_description)
        return sorted(self.resumes, key=lambda resume: resume.proportion_score, reverse = True)[: number_to_return]

    def greedy_proportion_matches(self):
        matches = []
        for job in self.jobs:
            resume = self.proportion_top_n(job_description=job.corpus, number_to_return=1)[0]
            match = Match(job, resume)
            score = resume.proportion_score
            matches.append(f"Match = {(Match(job, resume))}, proportion_match = {score}")
        return matches

