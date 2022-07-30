# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from twisted.web.html import output


def process_salary(value):
    value = value.replace(' ', '')
    try:
        value = int(value)
    except:
        pass
    return value

class CastparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    salary = scrapy.Field(input_processor=MapCompose(process_salary), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    _id = scrapy.Field()
    photos = scrapy.Field()
