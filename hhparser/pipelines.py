# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class HhparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancies2507

    def process_item(self, item, spider):
        item['salary'] = self.process_salary(item['salary'])
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

    def process_salary(self, salary):
        salary_min = None
        salary_max = None
        salary_currency = None
        salary_a = ''.join(salary)
        salary_all_list = salary_a.replace('\xa0', '')
        salary_all_list = salary_all_list.split()

        if salary_all_list[0] == 'от' and salary_all_list[2] == 'до':
            salary_min = int(salary_all_list[1])
            salary_max = int(salary_all_list[3])
            salary_currency = salary_all_list[4]
        elif salary_all_list[0] == 'от':
            salary_min = int(salary_all_list[1])
            salary_max = None
            salary_currency = salary_all_list[2]
        elif salary_all_list[0] == 'до':
            salary_min = None
            salary_max = int(salary_all_list[1])
            salary_currency = salary_all_list[2]
        elif salary_all_list[0] == 'з/п':
            salary_min = None
            salary_max = None
            salary_currency = None

        result = {'min': salary_min,
                  'max': salary_max,
                  'currency': salary_currency}

        return result
