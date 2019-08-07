# -*- coding: utf-8 -*-
import scrapy


class CollegeSpider(scrapy.Spider):
    name = 'college'
    allowed_domains = ['https://www.sports-reference.com/cbb/']
    start_urls = ['http://https://www.sports-reference.com/cbb//']

    def parse(self, response):
        pass
