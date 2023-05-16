from resume import Resume
import os
directory = os.listdir("resumes")
pathList = []
for filePath in directory:
    pathList.append(filePath)

for path in pathList[0]:
    resume = Resume(f"resumes/{filePath}")
    print(resume.wordFreqs)