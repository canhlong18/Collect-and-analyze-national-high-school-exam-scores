from bs4 import BeautifulSoup
import requests

# start = 26000001
# end = 26000004

file = open("test_rawData_ThaiBinh_2020.txt", "w")

for sbd in range(start,end):
	url = 'http://diemthi.24h.com.vn/?v_page=1&v_sbd='+str(sbd)+'&v_ten=&v_cum_thi=26'		#put your link

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

	file.write(str(result) + "\n")