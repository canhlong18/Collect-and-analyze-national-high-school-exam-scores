from bs4 import BeautifulSoup
import requests

url = 'https://diemthi.baogiaothong.vn/search-thpt?sbd=01000030'

source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())

body = soup.find('body')
table = body.find('table', class_='table table-bordered')

result = table.thead.text

print(result)
# sbd does not exist
# if table == None:
# 	continue

# result = result.split('\n')