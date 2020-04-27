# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    company = scrapy.Field()
    company_logo = scrapy.Field()
    sponsor = scrapy.Field()
    sponsor_logo = scrapy.Field()
