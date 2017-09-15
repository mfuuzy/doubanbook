# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()  # 书名
    year = Field()  # 出版日期
    score = Field()  # 豆瓣分数
    author = Field()  # 作者
    press = Field()  # 出版社
    ISBN = Field() #ISBN