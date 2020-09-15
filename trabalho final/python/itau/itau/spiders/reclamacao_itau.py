import scrapy


class ReclamacaoItauSpider(scrapy.Spider):
    name = 'reclamacao_itau'
    allowed_domains = ['www.reclameaqui.com.br']
    start_urls = ['https://www.reclameaqui.com.br']

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('Url is :{}'.format(url))
