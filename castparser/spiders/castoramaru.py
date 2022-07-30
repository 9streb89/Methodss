import scrapy
from scrapy.http import HtmlResponse
from castparser.items import CastparserItem
from scrapy.loader import ItemLoader


class CastoramaruSpider(scrapy.Spider):
    name = 'castoramaru'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/catalogsearch/result/?q=%D1%81%D0%BC%D0%B5%D1%81%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&bm_tip_produkta=%D0%A1%D0%BC%D0%B5%D1%81%D0%B8%D1%82%D0%B5%D0%BB%D1%8C+%D0%B4%D0%BB%D1%8F+%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B9']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class = 'next i-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='product-card__img-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.object_parse)

    def object_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=CastparserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('salary', "//span[@class='price']//text()")
        loader.add_xpath('photos', "//ul[@class='swiper-wrapper']//li/img/@data-src")
        loader.add_value('url', response.url)
        yield loader.load_item()


        # name = response.xpath("//h1/text()").get()
        # salary = response.xpath("//span[@class='price']//text()").get()
        # url = response.url
        # photos = response.xpath("//ul[@class='swiper-wrapper']//li/img/@data-src").getall()
        # yield CastparserItem(name=name, salary=salary, url=url, photos=photos)
