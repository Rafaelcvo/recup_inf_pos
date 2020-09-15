import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['amazom.com.br']
    start_urls = ['http://amazom.com.br/']

    def parse(self, response):
        pass
