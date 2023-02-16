from bs4 import BeautifulSoup
import requests
import csv

with open("test.csv", mode="w", encoding='utf8', newline='') as test_fileCSV:
		header = ["SBD", "Toán", "Ngữ Văn", "Vật Lý", "Hóa Học", "Sinh Học", "Lịch Sử", "Địa Lý", "GDCD", "Ngoại Ngữ", "Mã NN"]
		writer = csv.writer(test_fileCSV)
		writer.writerow(header)
# file = open('test.txt', encoding='utf8', mode='w')

start = 4000001
end = 4000104

for sbd in range(start, end):

	url = "https://congluan.vn/diemthi?sbd=0" + str(sbd)
	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')
	# print(soup.prettify())

	body = soup.find('body')
	div = body.find('div', class_='mar2per pkg')

	table = div.find('table')
	if table == None:
		continue

	# find all <tr> tag and index neccessary tag (score tag)
	tr = table.find_all('tr')
	result = tr[1].text
	result = result.split("\n")

	# remove unneccessary Cols
	neccessaryCols = []
	for i in range(len(result)):
		if i in [1,2,3,4,5,6,7,8,9,10,11]:
			neccessaryCols.append(result[i])
	result = neccessaryCols
	# print(result)

	# relpace '' and 0 by '-1'
	for i in range(len(result)):
		if result[i] == "":
			result[i] = "-1"

	for i in range(len(result)):
		if result[i] == "0":
			result[i] = "-1"

	# file.write(str(result) + "\n")

	with open("test.csv", "a", encoding='utf8', newline='') as test_fileCSV:
		writer = csv.writer(test_fileCSV)
		writer.writerow(result)

