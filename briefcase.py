from typing import List
import os
from resume import Resume

class Briefcase():
    def __init__(self, directory:str):
        self.directory = directory
        self.paths = [f"{directory}/{path}" for path in os.listdir(directory) if path.split(".")[1] == "pdf"]
        self.resumes = [Resume(path) for path in self.paths]

