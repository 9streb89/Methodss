import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint

url = 'https://dubna.hh.ru'
params = {'page': '0'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
session = requests.Session()
response = session.get(url + '/search/vacancy?text=Data+enginer&from=suggest_post&salary=&clusters=true&ored_clusters=true&enable_snippets=true', params=params, headers=headers)

dom = BeautifulSoup(response.text, 'html.parser')

last_page = dom.find('span', {'data-qa': 'pager-page-wrapper-32-31'}).text

vacance_list = []

for i in range(int(last_page)):
    print(f'scrapping page {i}')
    params['page'] = i
    response = session.get(url + '/search/vacancy?text=Data+enginer&from=suggest_post&salary=&clusters=true&ored_clusters=true&enable_snippets=true', params=params, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    vacance = dom.find_all('div', {'class': 'vacancy-serp-item'})
    for article in vacance:
        vacance_data = {}
        name = article.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
        vacance_name = article.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text
        href = name.get('href')
        website = url
        vacancy_wage = article.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

        if not vacancy_wage:
            vacancy_wage = 0
        else:
            vacancy_wage = article.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'}).text
            vacancy_wage = vacancy_wage.replace("\u202f", "")
            # """навыков и времени не хватает для разделения на три поля"""

        vacance_data['name'] = vacance_name
        vacance_data['href'] = href
        vacance_data['website'] = website
        vacance_data['vacancy_wage'] = vacancy_wage

        vacance_list.append(vacance_data)

pprint(vacance_list)
print(len(vacance_list))
