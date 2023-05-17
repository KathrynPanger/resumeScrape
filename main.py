from resume import Resume
import os

# GOAL
# Given a folder of resumes and a list of keywords, copy a subset of x resumes to a second folder with ranked filenames
# Create a text file describing the rankings and stats of the x resumes, and the reasoning behind their selection

directory = os.listdir("resumes")
pathList = []
for filePath in directory:
    pathList.append(filePath)

# print(pathList[1])
# for path in pathList:
#     try:
#         print(path)
#         resume = Resume(f'resumes/{path}')
#         print(resume.wordFreqs)
#     except:
#         print("skip")

weirdResume = Resume("resumes/FernandoBecerra_Resume.pdf")
normalResume = Resume("resumes/bear-jordan-resume.pdf")
print(weirdResume.wordFreqs)
print(normalResume.wordFreqs)
