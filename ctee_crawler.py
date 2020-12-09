import time

class ctee_news:
    def __init__(self, title, time_string, url):
        self.title = title
        self.time = time.strptime(time_string, "%m/%d %H:%M")
        self.url = url