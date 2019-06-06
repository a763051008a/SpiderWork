# -*- coding: utf-8 -*-
import random, base64


class ProxyMiddleware(object):
    #代理IP列表
    proxyList = [
        '110.52.235.243:9999',
        '123.233.153.151:8118'
        ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr