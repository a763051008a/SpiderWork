# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewlagouItem(scrapy.Item):
    job_web = scrapy.Field()
    pass

class xiangqingItem(scrapy.Item):
    job_title = scrapy.Field()
    job_money = scrapy.Field()
    job_location = scrapy.Field()
    job_experience = scrapy.Field()
    job_education = scrapy.Field()
    job_worktype = scrapy.Field()
    job_description = scrapy.Field()
    pass