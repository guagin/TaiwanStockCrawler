import time

class ctee_news:
    def __init__(self, title, time_string, url):
        self.title = title
        year = str(time.localtime().tm_year)
        self.time = time.strptime(year+"/"+time_string, "%Y/%m/%d %H:%M")
        self.url = url
        self.key = time.mktime(self.time)

