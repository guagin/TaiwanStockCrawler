from news.ctee_crawler import ctee_crawler

ctee_crawler_1 = ctee_crawler()

for x in ctee_crawler_1.news :
    print(x.title, x.time.tm_year, x.time.tm_mon, x.time.tm_mday, x.time.tm_hour, x.time.tm_min,x.time.tm_sec)
