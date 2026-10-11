#program to build a student result analyzer
#find total marks, average marks, highest marks and number of passing students pass marks=40
analyzemarks=(35,72,80,45,90,30)
totalmarks=sum(analyzemarks)
averagemarks=totalmarks/len(analyzemarks) if len(analyzemarks)>0 else 0
highestmarks=max(analyzemarks)
passingstudents=len([marks for marks in analyzemarks if marks>=40])

print("Total Marks:",totalmarks)
print("Average Marks:",averagemarks)
print("Highest Marks:",highestmarks)
print("Passing Students are:",passingstudents)