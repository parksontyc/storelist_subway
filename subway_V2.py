import requests
from bs4 import BeautifulSoup
import time
import csv

store_no = []
store_name = []
store_address = []
store_tel =[]


for i in range(0, 14):
	base_url = "http://www.twsubway.com.tw/GoWeb2/include/index.php?pageNum_content01="+str(i)+"&totalRows_content01=132&Page=2&Cate01=&Cate02=&Cate03="

	res = requests.get(base_url, timeout=5)
	base_html = res.text
	soup = BeautifulSoup(base_html.replace('\n', "").strip(), "html.parser")

	items = soup.find_all('tbody')

	for item in items:
		for num in item.find_all('tr'):
			store_no.append(num.find("", {"class":"store-num"}).text)
			store_name.append(num.find("", {"class":"store-name"}).text.strip())
			store_address.append(num.find("", {"class":"store-where"}).text)
			store_tel.append(num.find("", {"class":"store-phone"}).text)
			print(store_no, store_name, store_address, store_tel)



with open('shop_list_subway.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市編號', '門市名稱', '門市地址', '門市電話']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_no[n])
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        newrow.append(store_tel[n])
        csvwriter.writerow(newrow)

		

	
	




