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

#make list of number students who not take exams
not_Take_Exam = [0,0,0,0,0,0,0,0,0]

for score in score_Of_Students:
	for i in range(1,10):
		if score[i] == "-1":
			not_Take_Exam[i-1] += 1

# caculate not take exam percentage
not_Take_Exam_Percent = [0,0,0,0,0,0,0,0,0]

for i in range(0,9):
	not_Take_Exam_Percent[i] = round(100 * not_Take_Exam[i]/ total_Students, 2)

# Plot barchart
# https://pythonspot.com/matplotlib-bar-chart/
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
# https://www.programiz.com/python-programming/methods/built-in/zip

import matplotlib.pyplot as plot_BC; plot_BC.rcdefaults()
import numpy as np

figure, axis = plot_BC.subplots()

# arange NUMBER of subjects into Ox (horizontal axis) (/y-pos)
Ox = np.arange(len(subjects))

# set limit of vertical axis (Oy)
axis.set_ylim(0,100)

#plot the barchart using 2 lists
plot_BC.bar(Ox, not_Take_Exam_Percent, align='center', alpha=1)
plot_BC.xticks(Ox, subjects)	# set horizontal category NAME by subjects

# make label and title of barchart
plot_BC.xlabel('MÔN THI')
plot_BC.ylabel('TỶ LỆ (%)')
plot_BC.title('Số Lượng Thí Sinh Không Đăng Ký Thi/ Bỏ Thi')

## Make some labels.
rects = axis.patches
# number of students label
for rect, label_num in zip(rects, not_Take_Exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, label_num,
    	ha= 'center', va= 'bottom')
    
# percentage label
labels_percent = []
for i in range(len(not_Take_Exam_Percent)):
	labels_percent.append(str(not_Take_Exam_Percent[i]) + "%")

for rect, label_percent in zip(rects, labels_percent):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label_percent,
    	ha= 'center', va= 'bottom', fontsize= 8, color= 'g')

plot_BC.show()