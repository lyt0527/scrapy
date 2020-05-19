# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AikaItem(scrapy.Item):
    # define the fields for your item here like:
    comment_num = scrapy.Field()
    read_num = scrapy.Field()
    up_num = scrapy.Field()
    zhuanfa = scrapy.Field()
    url = scrapy.Field()
    MonitorName = scrapy.Field()
