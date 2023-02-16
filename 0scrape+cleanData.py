from bs4 import BeautifulSoup
import requests
import csv

# write header to .csv file
with open("cleanData_02-HCM_2020.csv", encoding="utf8", mode="w", newline='') as fileCSV:
	header = ["SBD", "Toán", "Ngữ Văn", "Ngoại Ngữ", "Vật Lý", "Hóa Học", "Sinh Học", "Lịch Sử", "Địa Lý", "GDCD"]
	writer = csv.writer(fileCSV)
	writer.writerow(header)

start = 2000001
end = 2074719

for sbd in range(start,end):
	url = 'http://diemthi.24h.com.vn/?v_page=1&v_sbd=0'+str(sbd)+'&v_ten=&v_cum_thi=02'		#put your link

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
	neccessaryColumn = []
	for i in range(len(result)):
		if i in [2,4,5,6,7,8,9,11,12,13]:
			neccessaryColumn.append(result[i])
	result = neccessaryColumn

	# Replace '' by -1
	for i in range(len(result)):
		if result[i] == "":
			result[i] = "-1"

	# write data to .csv file
	with open("cleanData_02-HCM_2020.csv", mode="a", encoding='utf8', newline='') as fileCSV:
		writer = csv.writer(fileCSV)
		writer.writerow(result)

