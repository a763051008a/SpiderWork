# -*- coding: utf-8 -*-
import scrapy
from newlagou.items import NewlagouItem
from scrapy import FormRequest
import time
import random
import json
from scrapy.crawler import CrawlerProcess

class LagouSpider(scrapy.Spider):
    name = 'zhaopingye'
    allowed_domains = ['lagou.com']
    start_urls = [
        'https://www.lagou.com/zhaopin/shangyeshjufenxi/{}/?filterOption=3'.format(i) for i in range(17,31)
    ]  # 这里是我们开始爬取的网站
    def parse(self, response):
        item = NewlagouItem()
        divs = response.xpath('//*[@id="s_position_list"]/ul/li/div[1]')
        #//*[@id="s_position_list"]/ul
        # // *[ @ id = "s_position_list"] / ul / li[1] / div[1]
        #//*[@id="s_position_list"]/ul/li[1]/div[1]
        # // *[ @ id = "s_position_list"] / ul / li[2] / div[1]
        for div in divs:
            # 可以获得对应招聘页的超链接
            job_web = div.xpath('./div[1]/div[1]/a/@href').extract()

            job_web = job_web[0] if len(job_web) > 0 else '无数据'

            item['job_web'] = job_web.strip()

            yield item
