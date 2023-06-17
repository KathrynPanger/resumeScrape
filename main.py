from resume import Resume
import os
from briefcase import Briefcase

# GOAL
# Given a folder of resumes and a list of keywords, copy a subset of x resumes to a second folder with ranked filenames
# Create a text file describing the rankings and stats of the x resumes, and the reasoning behind their selection

# Task 1: rank resume objects
searchList = ["sQl", "python", "van", "degree"]

briefcase = Briefcase("resumes")
print(briefcase.frequency_match(searchList, 4))


#rint(repr(weirdResume.corpus))
#sprint(normalResume.corpus)
