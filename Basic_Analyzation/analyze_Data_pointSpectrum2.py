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


# make list of point spectrum - group2 (literature, Physics, Chemistry, Biology, History, Geography, Civic Education).
pointSpectrum_group2 = [0]
zeroo = 0
for i in range(40):
	zeroo = zeroo + 0.25
	pointSpectrum_group2.append(round(zeroo, 2))

# replace 1.0, 2.0, .... 10.0 by 1, 2, ..., 10
replace_this = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
by_this = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(pointSpectrum_group2)):
	for j in range(len(replace_this)):
		if pointSpectrum_group2[i] == replace_this[j]:
			pointSpectrum_group2[i] = by_this[j]

# make list (value = 0) of number of students in each point level
num_students_each_point_level_group2 = [0]
for i in range(40):
	num_students_each_point_level_group2.append(0)

print(len(score_Of_Students), "\n")

# caculate: list of number of students in each point level
# for std in score_Of_Students:
# 	std[2] = float(std[2])
# 	for i in range(len(pointSpectrum_group2)):

# 		if std[2] == pointSpectrum_group2[i]:
# 			std[2] = pointSpectrum_group2[i]

# 		if std[2] != pointSpectrum_group2[i] and std[2] < pointSpectrum_group2[i] and std[2] > pointSpectrum_group2[i-1]:
# 			x = std[2] - pointSpectrum_group2[i-1]
# 			y = pointSpectrum_group2[i] - std[2]

# 			if x > y:
# 				std[2] = pointSpectrum_group2[i]
# 			if x < y:
# 				std[2] = pointSpectrum_group2[i-1]

# 	std[2] = str(std[2])

for std in score_Of_Students:
	for i in range(len(pointSpectrum_group2)):
		if std[9] == str(pointSpectrum_group2[i]):
			num_students_each_point_level_group2[i] += 1

print(num_students_each_point_level_group2, "\n")
print(len(num_students_each_point_level_group2), "\n")
print(sum(num_students_each_point_level_group2), "\n")


# # PLOT CHART
import matplotlib.pyplot as plot_BC; plot_BC.rcdefaults()
import numpy as np

figure, axis = plot_BC.subplots()

# arange NUMBER of subjects into Ox (horizontal axis) (/y-pos)
Ox = np.arange(len(pointSpectrum_group2))

# set limit of vertical axis (Oy)
axis.set_ylim(0,5500)

# plot the line chart
# plot_BC.plot(Ox, num_students_each_point_level_group2, color= 'b')

#plot the barchart using 2 lists
pl = plot_BC.bar(Ox, num_students_each_point_level_group2, 
	width=0.6, align='center', alpha=1, color= 'navajowhite')

for s in [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]:
	pl[s].set_color('orange')

plot_BC.xticks(Ox, pointSpectrum_group2, rotation= 90, fontsize= 8)	# set horizontal category NAME by subjects


# make label and title of barchart
plot_BC.xlabel('ĐIỂM THI')
plot_BC.ylabel('SỐ LƯỢNG THÍ SINH')
plot_BC.title('PHỔ ĐIỂM MÔN GDCD TP HÀ NỘI')

## Make number of students labels.
rects = axis.patches

for rect, label_num in zip(rects, num_students_each_point_level_group2):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 40, label_num,
    	ha= 'center', va= 'bottom', rotation= 90, color= 'k', fontsize= 8, alpha= 1)
    
plot_BC.show()

