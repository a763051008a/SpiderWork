# -*- coding: utf-8 -*-
import scrapy
from spiderXiangqing.items import xiangqingItem
from scrapy import Request
import time
import random
import json
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings

class LagouSpider(scrapy.Spider):
    name = 'xiangqing'
    allowed_domains = ['lagou.com']
    path = 'C:\\Users\Administrator\PycharmProjects\My_test\\newlagou\\newlagou\\web_list.json'
    file = open(path)
    data = json.load(file)
    list = []
    for i in data:
        list.append(i['job_web'])
    start_urls = list  # 这里是我们开始爬取的网站
    # 不使用cookie，注释 Request的 ,headers=self.headers, cookies=self.cookies, meta=self.meta
    meta = settings['META']
    cookies = settings['COOKIES']
    headers = settings['DEFAULT_REQUEST_HEADERS']

    def start_requests(self):
        for url in self.start_urls:
            r = Request(url, callback=self.parse, dont_filter=True,headers=self.headers, cookies=self.cookies)
            yield r

    def parse(self, response):
        item = xiangqingItem()
        job_title = response.xpath('/ html / body / div[4] / div / div[1] / div / span/text()').extract()
        job_money = response.xpath('/html/body/div[4]/div/div[1]/dd/p[1]/span[1]/text()').extract()
        job_location = response.xpath('/html/body/div[4]/div/div[1]/dd/p[1]/span[2]/text()').extract()
        job_experience = response.xpath('/html/body/div[4]/div/div[1]/dd/p[1]/span[3]/text()').extract()
        job_education = response.xpath('/html/body/div[4]/div/div[1]/dd/p[1]/span[4]/text()').extract()
        job_worktype = response.xpath('/html/body/div[4]/div/div[1]/dd/p[1]/span[5]/text()').extract()
        #获取JD
        divs = response.xpath('//*[@id = "job_detail"]/dd[2]/div')
        job_descriptions = divs.xpath('./p/text()').extract()
        job_description = ''
        for i in job_descriptions:
            job_description += i
            job_description += '\n'

        job_title = job_title[0] if len(job_title) > 0 else '无数据'
        job_money = job_money[0] if len(job_money) > 0 else '无数据'
        job_location = job_location[0] if len(job_location) > 0 else '无数据'
        job_experience = job_experience[0] if len(job_experience) > 0 else '无数据'
        job_education = job_education[0] if len(job_education) > 0 else '无数据'
        job_worktype = job_worktype[0] if len(job_worktype) > 0 else '无数据'
        job_description = job_description if len(job_description) > 0 else '无数据'


        item['job_title'] = job_title.strip()
        item['job_money'] = job_money.strip()
        item['job_location'] = job_location.strip()
        item['job_experience'] = job_experience.strip()
        item['job_education'] = job_education.strip()
        item['job_worktype'] = job_worktype.strip()
        item['job_description'] = job_description.strip()

        yield item
