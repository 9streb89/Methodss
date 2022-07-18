# from lxml import html
# import requests
# from pprint import pprint
# from pymongo import MongoClient
# from pymongo import errors
#
# url = 'https://lenta.ru'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
# session = requests.Session()
# response = session.get(url, headers=header)
# dom = html.fromstring(response.text)
#
# news = []
# items = dom.xpath("//a[contains(@class, 'topnews')]")
# for item in items[0:13]:
#     one_news = {}
#     title_time = item.xpath(".//div[contains(@class, 'card-')]//text()")
#     link = item.xpath(".//div[contains(@class, 'card-')]/../@href")
#     link_2 = url + link[0]
#
#     one_news['website'] = url
#     one_news['link'] = link_2
#     one_news['title'] = title_time[0]
#     one_news['time'] = title_time[1]
#
#     news.append(one_news)
#
# pprint(news)
#
# client = MongoClient('127.0.0.1', 27017)
#
# db = client['news1807']
# news1807 = db.news1807
#
#
# for item in news:
#     news1807.insert_one(item)
#
#
# for item in news1807.find({}):
#     pprint(item)
