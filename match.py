from document import Document


class Match():
    def __init__(self, job: Document, resume: Document):
        self.job = job
        self.resume = resume

    def __repr__(self):
        return f"Match(Job:{self.job.path}, Resume:{self.resume.path})"
