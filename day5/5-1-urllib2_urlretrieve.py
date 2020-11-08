from urllib.request import urlretrieve

# urlretrieve("website", filename="fileName.html") -- 简洁方式一行代码获取
urlretrieve("http://www.baidu.com", filename="urllib2_baidu.html")
