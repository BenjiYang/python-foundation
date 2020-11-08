from urllib.request import urlopen

# 最简单的爬虫 - HTTP 静态网页的数据，如百度
resp = urlopen("http://www.baidu.com")
print(resp)
with open("urllib1_baidu.html", "wb") as f:
    f.write(resp.read())
resp.read().decode("utf-8")
