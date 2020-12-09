import requests
from bs4 import BeautifulSoup

response = requests.get("https://ctee.com.tw/livenews")

soup = BeautifulSoup(response.text, "html.parser")

result = soup.find_all(class_="now-title")

print(result)

a = {x.select_one("a") for x in result }

print(a)