# -*- coding: utf-8 -*-
from scrapy.selector import Selector
# from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.spiders import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from book.items import DoubanItem

class BookSpider(CrawlSpider):
    name="doubanbook"
    allowed_domains=["book.douban.com"]
    # start_urls=["https://movie.douban.com/top250?start=0&filter="]
    start_urls=["https://book.douban.com/top250"]
    rules=[
        Rule(LinkExtractor(allow=(r'https://book.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'https://book.douban.com/subject/\d+')),callback="parse_item"),
    ]

    def parse_item(self,response):
        # sel=Selector(response)
        item=DoubanItem()
        item['name']= response.xpath('//span[@property="v:itemreviewed"]/text()').extract()
        item['year']= response.xpath('//div[@id="info"]/text()').re('.*-.*')
        item['score']= response.xpath('//strong/text()').extract()
        item['author']= response.xpath('//div[@id="info"]/a[1]/text()').extract()
        # item['press']= response.xpath('//div[@id="info"]/text()').extract()[4]
        item['ISBN']= response.xpath('//div[@id="info"]/text()[last()-1]').extract()
        return item