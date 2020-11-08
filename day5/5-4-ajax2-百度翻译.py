# 练习： 分析百度翻译的接口

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
kw = input("请输入你相翻译的单词：")
resp = requests.post("https://fanyi.baidu.com/sug",
                     headers=headers, data={"kw": "Python"})
data = resp.json()
print(data['data'])
