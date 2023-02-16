from bs4 import BeautifulSoup
import requests

url = 'http://diemthi.laodong.vn/tra-cuu-diem-thi-thpt-xem-diem-thi-dai-hoc-2020.html?sbd=01000088'
source = requests.get(url)

soup = BeautifulSoup(source.text, 'lxml')

# print(soup)
body = soup.find('body')
detail = body.find('div', class_='detail-score-panel')
print(detail)