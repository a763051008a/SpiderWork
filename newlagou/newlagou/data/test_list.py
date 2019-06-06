import redis
import urllib.request
from bs4 import BeautifulSoup
import requests

r = redis.Redis(host='127.0.0.1', port=6379)
proxys = []
for d in range(1, 3):  # 采集1到2页
    scrapeUrl = 'http://www.xicidaili.com/nn/%d/' % d
    req = urllib.request.Request(scrapeUrl)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = urllib.request.urlopen(req)
    html = response.read()

    bsObj = BeautifulSoup(html, "html.parser")

    for i in range(100):
        speed = float(bsObj.select('td')[6 + i * 10].div.get('title').replace('秒', ''))
        if speed < 0.6:  # 验证速度，只要速度在0.6秒之内的
            ip = bsObj.select('td')[1 + i * 10].get_text()
            port = bsObj.select('td')[2 + i * 10].get_text()
            proxy_host = ip + ':' + port
            proxy_temp = {"http": proxy_host}
            proxys.append(proxy_temp)
    print(proxys)

for proxy in proxys:
    try:
        url = 'http://ip.chinaz.com/getip.aspx/'
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, proxies=proxy, headers=header, timeout=3)
        code = requests.get(url, proxies=proxy, headers=header, timeout=3).status_code
        if code == 200:
            print(code)
            response.encoding = 'utf-8'
            if "address" in response.text:
                print(response.text)
                # r.sadd('ippool', proxy)
                f = open('succ_list.txt', 'a')
                f.write(str(proxy) + '\n')
                f.close()
    except:
        print("失败")