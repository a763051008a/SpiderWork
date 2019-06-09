# -*- coding: utf-8 -*-

# Scrapy settings for spiderXiangqing project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiderXiangqing'

SPIDER_MODULES = ['spiderXiangqing.spiders']
NEWSPIDER_MODULE = 'spiderXiangqing.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiderXiangqing (+http://www.yourdomain.com)'

# Obey robots.txt rules
# Scrapy 默认是遵守爬虫准则的，即ROBOTSTXT_OBEY = True,如果遵守爬虫准则的，是不能用Scrapy来爬取的，这时需要把ROBOSTSXT_OBEY=False,也就是不遵守它的规则，一般我们都是不遵守他的规则。
ROBOTSTXT_OBEY = False

# 禁止被重定向
REDIRECT_ENABLED = False
HTTPERROR_ALLOWED_CODES = [301,302]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32


# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置延迟3秒,操作太快容易遭遇反爬虫
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#启用cookies
# Disable cookies (enabled by default)
COOKIES_ENABLED =  True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#修改默认请求头
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie':'_ga=GA1.2.1087409312.1559180285; user_trace_token=20190530093806-92d9de9f-827b-11e9-a83d-525400f775ce; LGUID=20190530093806-92d9e221-827b-11e9-a83d-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=57; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216b070829eb540-048e0ee56d9e25-e353165-1327104-16b070829ec54d%22%2C%22%24device_id%22%3A%2216b070829eb540-048e0ee56d9e25-e353165-1327104-16b070829ec54d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2274.0.3729.169%22%7D%7D; LG_LOGIN_USER_ID=fe04709f767102e06debba7c648692ca9bf3cc1071cec9f0; gate_login_token=6dfc2cf13bf76509069657688ddc7245930d7cdceab4d440; _gat=1; LGSID=20190604132904-aaac6484-8689-11e9-a1d2-5254005c3644; PRE_UTM=m_cf_cpc_360_pc; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fcommunal.html%3Futm_source%3Dm_cf_cpc_360_pc%26m_kw%3D360_cpc_sh_e110f9_a67efc_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%25E4%25BC%2581%25E4%25B8%259A; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1559530119,1559530130,1559530139,1559626145; _putrc=4FC2C74136FBF075; JSESSIONID=ABAAABAAAFCAAEG4D060A2A5CC682C4575DC121391EB6E9; login=true; unick=%E7%A8%8B%E6%B5%A9; X_HTTP_TOKEN=e0f5e5ce992f54ee84162695517b375414c2622aa6; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1559626150; LGRID=20190604132909-ad83bb14-8689-11e9-a9a6-525400f775ce; _gid=GA1.2.1729039935.1559626150',
   # 'Referer': 'https://www.lagou.com/',
    'Host': 'www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4482.400 QQBrowser/9.7.13001.400'
}
MY_USER_AGENT = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
]
HEADERS = {
	'Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
}
META = {
	'dont_redirect': True,
	'handle_httpstatus_list': [301, 302]
}
cookie = {
'ga': 'GA1.2.1087409312.1559180285', 'user_trace_token': '20190530093806-92d9de9f-827b-11e9-a83d-525400f775ce', 'LGUID': '20190530093806-92d9e221-827b-11e9-a83d-525400f775ce', 'index_location_city': '%E4%B8%8A%E6%B5%B7', 'LG_HAS_LOGIN': '1', 'showExpriedIndex': '1', 'showExpriedCompanyHome': '1', 'showExpriedMyPublish': '1', 'hasDeliver': '57', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2216b070829eb540-048e0ee56d9e25-e353165-1327104-16b070829ec54d%22%2C%22%24device_id%22%3A%2216b070829eb540-048e0ee56d9e25-e353165-1327104-16b070829ec54d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2274.0.3729.169%22%7D%7D', 'LG_LOGIN_USER_ID': 'fe04709f767102e06debba7c648692ca9bf3cc1071cec9f0', 'gate_login_token': '6dfc2cf13bf76509069657688ddc7245930d7cdceab4d440', 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1559530139,1559626145,1559626672,1560075871', '_gat': '1', 'LGSID': '20190609182434-c67381e1-8aa0-11e9-a228-5254005c3644', 'PRE_UTM': 'm_cf_cpc_baidu_pc', 'PRE_HOST': 'www.baidu.com', 'PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.af0000aF4eAvq9HI8laC210IEDaGEtmT7VtH3pX9Z-j89JWe2JCAUM3UnDbvx3JDq0WlNxJM20J_rQgsUSW82HR2w2qoln35fED-_5JXYdnAK_F9SfuchJcYBNQsvRpH1agVGkFDKJVqYj26-xybZRrPR2BLCPFFXpltqbBxvkYX5OhnTJ1QfnDJfFX7lTVB0HMeukrPyLQSZt_zos.DY_NR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6kssw_YyuVZ5E6CpXyPvap7QAM-9dt_rrZ-EukmrgZjdYtEUsng_3_ZQjW94ml8NPIIhExzsq-LAS1-C_lMm72s1f_I-hOmC0.U1Yk0ZDqUA7MULR0TA-W5H00Ijd_myIEIfKGUHYznjf0u1dEugK1n0KdpHdBmy-bIfKspyfqn6KWpyfqPj030AdY5HDsnHIxnH0krNtznjmzg1DsnWPxn1msnfKopHYs0ZFY5Hfkn0K-pyfqnWmdnWwxnHfdr7tznHDzPdtkrjRdrNtzrHD1PNtzrHc1r7tzrjRkr7tzrH04r7tzrHD1rNtzrj61P-tzrjR3PNtzrH0Ln6KBpHYznjwxnHR30AdW5H6knHb3n16YnNtknj0kg1cznWbdnjcznHNxnNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1Qy4J0A-bm1dcy6KYIgnqnHfdrjnLPjDsnHTYrjDzP1DLrHD0ThNkIjYkPHmsnjTdrjTsrjf30ZPGujd9Phw9PWPhuW0suj-bnjbd0AP1UHYYwWwjwHFjfbckwbmYfR7A0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc100mLFW5Hcdnj0L%26word%3Dlagou%26ck%3D1215.5.58.314.558.301.558.151%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26us%3D1.0.1.0.1.302.0%26bc%3D110101', 'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsalary.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sh_e110f9_c4d3b0_lagou', '_putrc': '4FC2C74136FBF075', 'JSESSIONID': 'ABAAABAAADEAAFI0C4A7E2B980A2AC3DB3013581A626645', 'login': 'true', 'unick': '%E7%A8%8B%E6%B5%A9', '_gid': 'GA1.2.849074541.1560075887', 'X_HTTP_TOKEN': 'e0f5e5ce992f54ee06957006517b375414c2622aa6', 'LGRID': '20190609182601-fa6fd4ad-8aa0-11e9-aa9a-525400f775ce', 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1560075959'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spiderXiangqing.middlewares.SpiderxiangqingSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'spiderXiangqing.middlewares.MyUserAgentMiddleware': None,
    'spiderXiangqing.rotate_useragent.RotateUserAgentMiddleware' :400

}
# 'spiderXiangqing.proxymiddlewares.ProxyMiddleware': 100,

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spiderXiangqing.pipelines.SpiderxiangqingPipeline': 300,
#}
MEDIA_ALLOW_REDIRECTS =True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
