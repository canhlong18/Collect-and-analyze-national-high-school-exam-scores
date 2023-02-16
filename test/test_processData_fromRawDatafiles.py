import csv

# write header to .csv files
with open("test_cleanData.csv", encoding="utf8", mode="w", newline='') as fileCSV:
	header = ["SBD", "Toán", "Ngữ Văn", "Ngoại Ngữ", "Vật Lý", "Hóa Học", "Sinh Học", "Lịch Sử", "Địa Lý", "GDCD"]
	writer = csv.writer(fileCSV)
	writer.writerow(header)

file = open("test_rawData_ThaiBinh_2020.txt", "r")

datas = file.read().split("\n")

for data in datas:

	# remove unneccessary characters
	data = data.replace("[", "")
	data = data.replace("]", "")
	data = data.replace(" ", "")
	data = data.replace("''", "-1")
	data = data.replace("'", "")

	# make data become a list
	data = data.split(",")

	# delete unneccessary column
	neccessaryRows = []
	for i in range(len(data)):
		if i in [2,4,5,6,7,8,9,11,12,13]:
			neccessaryRows.append(data[i])
	data = neccessaryRows

	# write data to .csv file
	with open("test_cleanData.csv", "a", encoding='utf8', newline='') as fileCSV:
		writer = csv.writer(fileCSV)
		writer.writerow(data)

