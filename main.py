import requests
from bs4 import BeautifulSoup

response = requests.get("https://ctee.com.tw/livenews")

soup = BeautifulSoup(response.text, "html.parser")

result = soup.find_all(class_="now-title")



a = {x.contents[3] for x in result }

for x in a:
    print(x.get_text())
