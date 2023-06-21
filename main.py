from document import Document
import os
from briefcase import Briefcase

# GOAL
# Given a folder of resumes and a list of keywords, copy a subset of x resumes to a second folder with ranked filenames
# Create a text file describing the rankings and stats of the x resumes, and the reasoning behind their selection

# Task 1: rank resume objects
searchList = ["sQl", "python", "van", "degree"]

# # resume has function version
# briefcase = Briefcase("resumes", jobs_directory="jobs")
# for resume in briefcase.resumes:
#     score = resume.frequency_match(briefcase.jobs[0].words)
#     print(resume, score)


# briefcase has function version
# #print(briefcase.frequency_match(searchList, 4))
# winners = briefcase.proportion_match(briefcase.jobs[0].corpus, 5)
# for resume in winners:
#     print(resume, resume.proportion_match)


#print(repr(weirdResume.corpus))
#print(normalResume.corpus)


briefcase = Briefcase(resumes_directory="resumes", jobs_directory="jobs")
matches = briefcase.greedy_proportion_matches()
print(matches)

