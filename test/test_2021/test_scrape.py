from bs4 import BeautifulSoup
import requests
import csv

file = open("test_data2021.txt", "w", encoding='utf8')

start = 0
end = 10
for stt in range(start,end):

	url = "https://diemthi.vnexpress.net/index/detail/id/" + str(6603249 + stt)

	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')
	# print(soup.prettify())      

	body = soup.find('body')
	table = body.find('div', class_='o-detail-thisinh')
	score_table = table.tbody

	Sobaodanh = table.find_all('strong')
	score = score_table.find_all('td')

	result = str(Sobaodanh + score)


	result = result.replace("[", "")
	result = result.replace("]", "")
	result = result.replace("\t", "")
	result = result.replace("\n", "")
	result = result.replace(", ", ",")
	
	tags = []
	for i in range(len(result)):
		if result[i] == "<":
			begin = i
		if result[i] == ">":
			end = i
			tags.append(result[begin:end + 1])

	for tag in tags:
		result = result.replace(tag, "")

	file.write(str(result) + "\n")

