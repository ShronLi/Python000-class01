# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    level = scrapy.Field()
    mid = scrapy.Field()
    rank = scrapy.Field()
    views = scrapy.Field()
    imagelink = scrapy.Field()

