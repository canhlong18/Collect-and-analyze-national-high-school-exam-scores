# read file
with open("cleanData_04-DaNang_2020.csv", encoding='utf8') as barchart1:
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

print(len(score_Of_Students), "\n")

# make list of point spectrum (math + english).
pointSpectrum_math_english = [0]
zeroo = 0
for i in range(50):
	zeroo = zeroo + 0.2
	pointSpectrum_math_english.append(round(zeroo, 1))

# replace 1.0, 2.0, .... 10.0 by 1, 2, ..., 10
replace_this = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
by_this = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(pointSpectrum_math_english)):
	for j in range(len(replace_this)):
		if pointSpectrum_math_english[i] == replace_this[j]:
			pointSpectrum_math_english[i] = by_this[j]

# make list (value = 0) of number of students in each point level
num_students_each_point_level = [0]
for i in range(50):
	num_students_each_point_level.append(0)

# caculate: list of number of students in each point level
for std in score_Of_Students:
	for i in range(len(pointSpectrum_math_english)):
		if std[3] == str(pointSpectrum_math_english[i]):
			num_students_each_point_level[i] += 1

print(num_students_each_point_level, "\n")
print(len(num_students_each_point_level), "\n")
print(sum(num_students_each_point_level))
# # PLOT CHART
import matplotlib.pyplot as plot_BC; plot_BC.rcdefaults()
import numpy as np

figure, axis = plot_BC.subplots()

# arange NUMBER of subjects into Ox (horizontal axis) (/y-pos)
Ox = np.arange(len(pointSpectrum_math_english))

# set limit of vertical axis (Oy)
axis.set_ylim(0,5000)

# plot the line chart
# plot_BC.plot(Ox, num_students_each_point_level, color= 'b')

#plot the barchart using 2 lists
pl = plot_BC.bar(Ox, num_students_each_point_level, 
	width=0.6, align='center', alpha=1, color= 'navajowhite')

for s in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]:
	pl[s].set_color('orange')

plot_BC.xticks(Ox, pointSpectrum_math_english, rotation= 90, fontsize= 8)	# set horizontal category NAME by subjects


# make label and title of barchart
plot_BC.xlabel('ĐIỂM THI')
plot_BC.ylabel('SỐ LƯỢNG THÍ SINH')
plot_BC.title('PHỔ ĐIỂM MÔN NGOẠI NGỮ TP HÀ NỘI')

## Make number of students labels.
rects = axis.patches

for rect, label_num in zip(rects, num_students_each_point_level):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 40, label_num,
    	ha= 'center', va= 'bottom', rotation= 90, color= 'k', fontsize= 8, alpha= 1)
    
plot_BC.show()
