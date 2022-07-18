# import re
# import requests
# from pymongo import MongoClient
# from pymongo import errors
# from bs4 import BeautifulSoup
# from pprint import pprint
#
#
# url = 'https://dubna.hh.ru'
# params = {'page': '0'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
# session = requests.Session()
# response = session.get(url + '/search/vacancy?text=Data+enginer&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true', params=params, headers=headers)
#
# dom = BeautifulSoup(response.text, 'html.parser')
#
# last_page = dom.find('span', {'data-qa': 'pager-page-wrapper-78-77'}).text
#
# vacancy_list = []
#
# for i in range(int(last_page)):
#     print(f'scrapping page {i}')
#     params['page'] = i
#     response = session.get(url + '/search/vacancy?text=Data+enginer&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=20&no_magic=true&L_save_area=true', params=params, headers=headers)
#     dom = BeautifulSoup(response.text, 'html.parser')
#     vacancy = dom.find_all('div', {'class': 'serp-item'})
#     for article in vacancy:
#         vacancy_data = {}
#         name = article.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
#         vacancy_name = article.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text
#         href = name.get('href')
#         website = url
#         vacancy_wage = article.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
#
#         vacancy_data['_id'] = int(re.sub('[^0-9]', '', href))
#         vacancy_data['name'] = vacancy_name
#         vacancy_data['href'] = href
#         vacancy_data['website'] = website
#
#         if vacancy_wage:
#             vacancy_wage_text = vacancy_wage.text
#             vacancy_wage_list = vacancy_wage_text.split(' ')
#             if vacancy_wage_list[0] == 'от':
#                 vacancy_wage_list[1] = vacancy_wage_list[1].replace('\u202f', '')
#                 vacancy_data['min_wage'] = int(vacancy_wage_list[1])
#                 vacancy_data['max_wage'] = None
#                 vacancy_data['currency'] = vacancy_wage_list[2]
#             elif vacancy_wage_list[0] == 'до':
#                 vacancy_wage_list[1] = vacancy_wage_list[1].replace('\u202f', '')
#                 vacancy_data['min_wage'] = None
#                 vacancy_data['max_wage'] = int(vacancy_wage_list[1])
#                 vacancy_data['currency'] = vacancy_wage_list[2]
#             elif vacancy_wage_list[1] == '–':
#                 vacancy_wage_list[0] = vacancy_wage_list[0].replace('\u202f', '')
#                 vacancy_wage_list[2] = vacancy_wage_list[2].replace('\u202f', '')
#                 vacancy_data['min_wage'] = int(vacancy_wage_list[0])
#                 vacancy_data['max_wage'] = int(vacancy_wage_list[2])
#                 vacancy_data['currency'] = vacancy_wage_list[3]
#
#         vacancy_list.append(vacancy_data)
#
# pprint(vacancy_list)
# pprint(len(vacancy_list))
#
#
# client = MongoClient('127.0.0.1', 27017)
#
# db = client['pars_hh_1707']
# vacancy_hh = db.vacancy_hh
#
#
# for item in vacancy_list:
#     try:
#         vacancy_hh.insert_one(item)
#     except errors.DuplicateKeyError:
#         print(f"Вакансия с таким ID = {item['_id']} уже есть")
#
# for item in vacancy_hh.find({}):
#     pprint(item)
#
#
# """2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой
# суммы (необходимо анализировать оба поля зарплаты). То есть цифра вводится одна, а запрос проверяет оба поля"""
#
#
# for item in vacancy_hh.find({'currency': 'руб.'}):
#     if item in vacancy_hh.find({'$or': [{'max_wage': {'$gt': 100000}}, {'min_wage': {'$gt': 100000}}]}):
#         pprint(item)

# client.close()
