from typing import List
import os
from document import Document
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import itertools


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

    def proportion_top_n(self, job_description: str, resume_list: List[Document], number_to_return: int):
        for resume in self.resumes:
           resume.proportion_score = resume.proportion_match(job_description)
        return sorted(self.resumes, key=lambda resume: resume.proportion_score, reverse = True)[: number_to_return]


    def greedy_proportion_matches(self):
        matched_jobs = {}
        jobs = self.jobs
        resumes = self.resumes
        for i in range(len(resumes)-1):
            job_number = i%(len(jobs))
            if i <= len(jobs):
                matched_jobs[jobs[job_number]] = []
            resume = self.proportion_top_n(job_description=jobs[job_number].corpus, resume_list=resumes, number_to_return=1)[0]
            matched_jobs[jobs[job_number]].append(resume)
            resumes.remove(resume)
        return matched_jobs
