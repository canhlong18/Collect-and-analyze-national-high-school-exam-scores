# read file
with open("cleanData_01-HaNoi_2020.csv", encoding='utf8') as barchart1:
	data = barchart1.read().split("\n")

# Make list of score and subjects
header = data[0]
score_Of_Students = data[1:]

# remove empty row in the end of list
score_Of_Students.pop()

total_Students = len(score_Of_Students)

#split header, make list of subjects and split score of each students
header = header.split(",")
subjects = header[1:]

for i in range(len(score_Of_Students)):
	score_Of_Students[i] = score_Of_Students[i].split(",")

#make list of number students who take 1,2,3,4,5,... exams
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0]

for std in score_Of_Students:
	count = 0
	for i in range(9):
		if std[i+1] != "-1":
			count += 1
	# if count == 0:
	# 	print(std)

	num_of_exam_taken[count] += 1

print(num_of_exam_taken)

#plot pie chart
#example:	https://pythonspot.com/matplotlib-pie-chart/
#			https://matplotlib.org/stable/gallery/color/named_colors.html
#			https://www.rapidtables.com/tools/pie-chart.html

import matplotlib.pyplot as plt

labels = ['0 Môn', '1 Môn', '2 Môn', '3 Môn', '4 Môn', '5 Môn',
			 '6 Môn', '7 Môn', '8 Môn', '9 Môn']
sizes = num_of_exam_taken
colors = ['yellowgreen', 'gold', 'lightskyblue', 'crimson', 'tan', 
			'lightcoral', 'cyan', 'plum', 'lime', 'peru']

plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)

plt.legend(labels, loc="best")
plt.axis('equal')
plt.tight_layout()

plt.show()