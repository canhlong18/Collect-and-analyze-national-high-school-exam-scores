from bs4 import BeautifulSoup
import requests

url = 'https://diemthi.vnexpress.net/#area=2&college=0&q=01000030'

source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())

body = soup.find('body')
div = body.find('div', class_='container')

# result = table.thead.text

print(div)
# sbd does not exist
# if table == None:
# 	continue

# result = result.split('\n')