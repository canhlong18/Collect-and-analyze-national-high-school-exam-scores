import csv

file = open("BacLieu.txt", mode='r', encoding='utf8')

#read one row
datas = file.read().split("\n")

with open('cleanData_01-HaNoi_2017.csv', mode='a', encoding='utf8', newline='') as fileCSV:
	header = ["SBD", "Toán", "Ngữ Văn", "Ngoại Ngữ", "Vật Lý", "Hóa Học", "Sinh Học", "Lịch Sử", "Địa Lý", "GDCD", "KHTN", "KHXH"]
	writer = csv.writer(fileCSV)
	writer.writerow(header)

for data in datas:
	
	data = data.replace("\t", "   ")
	data = data.replace("KHXH: ", "KHXH:   ")
	data = data.replace("KHTN: ", "KHTN:   ")
	data = data.replace(":", "")

	data = data.split("   ")
	sbd = data[0]

	scores = [str(sbd)]

	for subj in ["Toán", "Ngữ văn", "Tiếng Anh", "Vật lí", "Hóa học", "Sinh học", "Lịch sử", "Địa lí", "GDCD", "KHTN", "KHXH"]:
		if subj in data:
			scores.append(str(float(data[data.index(subj) + 1])))
		else:
			scores.append("-1")

	with open('cleanData_01-HaNoi_2017.csv', mode='a', encoding='utf8', newline='') as fileCSV:
		writer = csv.writer(fileCSV)
		writer.writerow(scores)

		