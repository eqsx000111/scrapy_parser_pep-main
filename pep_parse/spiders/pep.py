import scrapy

from constants import ALLOWED_DOMAINS, PEP_SPIDER_NAME, START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse_pep(self, response):
        for link in response.css('td a[href*="pep-"]::attr(href)').getall():
            yield response.follow(link, callback=self.parse_detail)

    def parse_detail(self, response):
        yield PepParseItem(
            number=response.css('h1.page-title::text').get().split(' – ')[0],
            name=response.css('h1.page-title::text').get().split(' – ')[1],
            status=response.css('abbr::text').get()
        )
