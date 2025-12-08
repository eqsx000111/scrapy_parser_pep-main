import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_SPIDER_NAME, ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    name = PEP_SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse_pep(self, response):
        for link in response.css('td a[href*="pep-"]::attr(href)').getall():
            yield response.follow(link, callback=self.parse_detail)

    def parse_detail(self, response):
        number, name = response.css(
            'h1.page-title::text'
        ).get().split(' – ', maxsplit=1)
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css('abbr::text').get()
        )
