from bs4 import BeautifulSoup
import requests
import csv

file = open("test_data2021.txt", "w", encoding='utf8')

url = "https://diemthi.vnexpress.net/index/detail/id/6996076"

source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())      

body = soup.find('body')

# find the info of students
thisinh_info = body.find('div', class_='o-detail-thisinh')
Sobaodanh = thisinh_info.h2.find_all('strong')

# find the score of students
score_table = thisinh_info.find('table', class_= 'e-table')
score = score_table.tbody.find_all('td')

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

# result = result.split(",")

file.write(str(result) + "\n")