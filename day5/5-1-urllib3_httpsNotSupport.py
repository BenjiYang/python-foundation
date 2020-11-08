from urllib.request import urlopen

# urllib 无法爬取到 HTTPS的页面
resp = urlopen("https://www.baidu.com")
print(resp)
with open("urllib3_baidu_HTTPS.html", "wb") as f:
    f.write(resp.read())
resp.read().decode("utf-8")
