import requests

'''
爬虫第一步，User-Agent header不能漏掉，否则被服务端反爬规则识别
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

resp = requests.get(
    "https://www.zhihu.com/signin?next=%2Fhot", headers=headers)

with open("request2_zhihu_header.html", "wb") as f:
    f.write(resp.content)
