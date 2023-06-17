from typing import List

import os
from resume import Resume

class Briefcase():
    def __init__(self, directory:str):
        self.directory = directory
        self.paths = [f"{directory}/{file}" for file in os.listdir(directory) if file.split(".")[-1] == "pdf"]
        self.resumes = [Resume(path) for path in self.paths]

    def frequency_match(self, query: List[str], number_to_return: int):
        self.query = [item.lower() for item in query]
        for resume in self.resumes:
            frequency_score = resume.frequency_score(query)
            resume.frequency_score = frequency_score
        return sorted(self.resumes, key = lambda resume: resume.frequency_score)[: number_to_return]

