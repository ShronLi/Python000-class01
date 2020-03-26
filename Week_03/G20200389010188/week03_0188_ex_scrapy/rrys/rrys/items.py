# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RrysItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title      = scrapy.Field()   #电影名字
    rank       = scrapy.Field()   #电影排名
    category   = scrapy.Field()   #电影分类
    url        = scrapy.Field()   #电影详细页面URL
    image_urls = scrapy.Field()   #电影封面图片URL
    images     = scrapy.Field()   #电影封面图片下载结果
    image_link = scrapy.Field()   #电影封面图片存储地址
    classify   = scrapy.Field()   #电影分级
    browse     = scrapy.Field()   #电影页面浏览次数
