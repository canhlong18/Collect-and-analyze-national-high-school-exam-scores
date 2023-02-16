import csv
# open file data
file = open("29-NgheAn_rawData2021.csv", "r", encoding= "utf8")
# read all line of file data
data = file.read().split('\n')
# remove the least empty line.
data.pop()

with open("29-NgheAn_Data.csv", encoding="utf8", mode="w", newline='') as fileCSV:
	header = ["SBD", "Toan", "Ngu Van", "Ngoai Ngu", "Vat Ly", "Hoa Hoc", "Sinh Hoc", "Lich Su", "Đia Ly", "GDCD"]
	writer = csv.writer(fileCSV)
	writer.writerow(header)

for i in range(len(data)):
	data[i] = data[i].split(",")

	# make list of sbd
	sbd = data[i][0]
	data_processed = [str(sbd)]

	# make list of scores
	scores_list = data[i][1:]
	# check and write student's scores to list data_processed
	for subject in ["Toán", "Ngữ văn", "Ngoại ngữ", "Vật lý", "Hóa học", "Sinh học", "Lịch sử", "Địa lý", "Giáo dục công dân"]:
		if subject in scores_list:
			data_processed.append(str(float(scores_list[scores_list.index(subject) + 1])))
		else:
			data_processed.append("-1")
	# print(data_processed)
	
	with open("29-NgheAn_Data.csv", mode="a", encoding='utf8', newline='') as fileCSV:
		writer = csv.writer(fileCSV)
		writer.writerow(data_processed)

