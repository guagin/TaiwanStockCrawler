import requests
from bs4 import BeautifulSoup

from news.ctee_news import ctee_news

class ctee_crawler:

    def __init__(self):
        response = requests.get("https://ctee.com.tw/livenews/aj/page/1")
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find_all(class_="now-title")
        lines = {x.contents[3] for x in result}

        splitLines = [x.get_text().strip().split('|') for x in lines]
        titleAndDate = {ctee_news(x[0], x[1].strip(), '') for x in splitLines}
        self.news = sorted(titleAndDate, key=lambda s: s.key, reverse=True)




