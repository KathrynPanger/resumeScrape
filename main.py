from resume import Resume
import os

#GOAL
# Given a folder of resumes and a list of keywords, copy a subset of x resumes to a second folder with ranked filenames
# Create a text file describing the rankings and stats of the x resumes, and the reasoning behind their selection

directory = os.listdir("resumes")
pathList = []
for filePath in directory:
    pathList.append(filePath)

for path in pathList[0]:
    resume = Resume(f"resumes/{filePath}")
    print(resume.wordFreqs)