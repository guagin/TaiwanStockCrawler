import time

import requests
from bs4 import BeautifulSoup

from ctee_crawler import ctee_news

response = requests.get("https://ctee.com.tw/livenews/aj/page/1")

soup = BeautifulSoup(response.text, "html.parser")

result = soup.find_all(class_="now-title")

a = {x.contents[3] for x in result }

b = [ x.get_text().strip().split('|') for x in a ]

c = { ctee_news(x[0],x[1].strip(), '') for x in b }

sorted(c, key=lambda s: s.key )

for x in c:
    print(x.title, x.time.tm_year, x.time.tm_mon, x.time.tm_mday,  x.time.tm_hour, x.time.tm_min)
