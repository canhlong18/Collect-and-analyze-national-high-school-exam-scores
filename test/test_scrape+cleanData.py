from bs4 import BeautifulSoup
import requests
import csv

# write header to CSV
with open("test_cleanData.csv", encoding="utf8", mode="w", newline='') as fileCSV:
	header = ["SBD", "Toán", "Ngữ Văn", "Ngoại Ngữ", "Vật Lý", "Hóa Học", "Sinh Học", "Lịch Sử", "Địa Lý", "GDCD"]
	writer = csv.writer(fileCSV)
	writer.writerow(header)

start = 11000001
end = 11000033

for sbd in range(start,end):
	url = 'http://diemthi.24h.com.vn/?v_page=1&v_sbd='+str(sbd)+'&v_ten=&v_cum_thi=11'		#put your link

	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')
	# print(soup.prettify())

	body = soup.find('body')
	table = body.find('table', class_='tblTestScore mgBt20')
	
	# sbd does not exist
	if table == None:
		continue

	result = table.tbody.tr.text
	result = result.split('\n')

	# delete unneccessary column
	neccessaryRows = []
	for i in range(len(result)):
		if i in [2,4,5,6,7,8,9,11,12,13,]:
			neccessaryRows.append(result[i])
	result = neccessaryRows

	# Replace '' by -1
	for i in range(len(result)):
		if result[i] == "":
			result[i] = "-1"

	# invert data from list to str and remove "[", "]", "''", " "
	# result = str(result)
	# result = result.replace("[", "")
	# result = result.replace("]", "")
	# result = result.replace("'", "")
	# result = result.replace(" ", "")
	# for i in range(len(result)):
	# 	file.write(result[i] + ",")

	# file.write("\n")

	# write data to .csv file
	with open("test_cleanData.csv", "a", encoding='utf8', newline='') as fileCSV:
		writer = csv.writer(fileCSV)
		writer.writerow(result)

