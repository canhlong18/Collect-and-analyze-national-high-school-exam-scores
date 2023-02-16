from bs4 import BeautifulSoup
import requests
import csv

with open('test_scrape(vietnamnet.vn).csv', mode="w", encoding='utf8', newline='') as test_fileCSV:
		header = ["SBD", "Toán", "Ngữ Văn", "Ngoại Ngữ", "Vật Lý", "Hóa Học", "Sinh Học", "Lịch Sử", "Địa Lý", "GDCD"]
		writer = csv.writer(test_fileCSV)
		writer.writerow(header)
# file = open('test_scrape(vietnamnet.vn).txt', mode='w', encoding='utf8')

start = 1000001
end = 1000050

for sbd in range(start, end):

	# get source code of the web
	url = "https://vietnamnet.vn/vn/giao-duc/tra-cuu-diem-thi-thpt/?y=2019&sbd=0" + str(sbd)
	source = requests.get(url)
	soup = BeautifulSoup(source.text,'lxml')

	# find score
	body = soup.find('body')
	table = body.find('table', class_='table thpt hidden-xs')

	# if data don't have sbd
	if table == None:
		continue

	result = table.tbody.tr

	# find all tag name "<td>" which have scores
	score = result.find_all('td')

	# clean up data by deleting tags (only choose text)
	for s in range(len(score)):
		score[s] = score[s].text

		# if subject have no score, write "-1"
		if score[s] == "":
			score[s] = "-1"

	# delete maNN( N1, N2, etc) 
	maNN = []
	for j in range(len(score[2])):
		if score[2][j] == ":":
			end = j
			maNN.append(score[2][:end+1])

	for ma in maNN:
		score[2] = score[2].replace(ma, "")

	# writing to cln_Data variable to write to .csv file
	sbd_str = "0" + str(sbd)
	cln_Data = [sbd_str]
	for i in range(len(score)):
		data = score[i]
		# data = data.text
		cln_Data.append(data)

	# file.write(str(cln_Data) + "\n")

	with open('test_scrape(vietnamnet.vn).csv', mode='a', encoding='utf8', newline='') as test_fileCSV:
		writer = csv.writer(test_fileCSV)
		writer.writerow(cln_Data)
