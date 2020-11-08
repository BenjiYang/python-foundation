# 动态网址，页面先加载出来，然后数据出来 - 异步加载
# 如果好分析 使用 jquery ajax，如果请求不好分析 使用selenium

# 爬取热门微博：https://m.weibo.cn
# 登录移动端微博web，然后使用chrome浏览器分析哪条是热门微博接口

# 微博热门微博接口：GET https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0
# 查看json： http://jsonviewer.stack.hu/
# 调试json路径： https://jsonpath.com/
# json热门微博内容路径第1条： data.cards[0].mblog.page_info.content2
# json热门微博内容路径第2条： data.cards[1].mblog.page_info.content2
# 使用requests 将内容从response里抽取出来
import requests
import json

agent_header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
resp = requests.get(
    "https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0", headers=agent_header)

# weibo_hit_text = resp.json(
# )['data']['cards'][0]['mblog']['page_info']['content2']
# print(weibo_hit_text)

resp_json = json.loads(
    resp.content, encoding='utf-8')
# print(resp_json)

for obj in resp_json['data']['cards']:
    weibo_content = obj['mblog']['page_info']['content2']
    if (weibo_content):
        print(weibo_content)
