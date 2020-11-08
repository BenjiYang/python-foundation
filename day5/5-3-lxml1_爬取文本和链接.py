# lxml - 第三方库，底层是用C语言写的，提取html页面内容
# pip3 install lxml
#
# https://www.w3school.com.cn/xpath/xpath_nodes.asp
# 人生格言网 http://www.geyanw.com/  - //*[@id="p_right"]/div/ul//a/@href
# Chrome 插件：xpath helper （Command + Shift + X）


''' Xpath语法
/      - 根结点
//      - 相对节点
.       - 当前current path
..      - 上一层path
div[@lang]      - 类名lang
div[@lang=‘eng']    - 缩小范围
text()      - 获取文本信息
'''

import requests
from lxml.etree import HTML

# 声明定义变量headers - "User-Agent"，伪装浏览器访问形式
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

# 获取response - 通过requests.get(url, headers）
resp = requests.get("http://www.geyanw.com/", headers=headers)

# 获取response的HTML文件形式
html_tree = HTML(resp.content)

# 获取HTML里部分"文本"信息 - 通过html.xpath(path/text()) 转成文本信息
title_list = html_tree.xpath("//div[@class='sidebar']//a/text()")
print(title_list)

# 获取HTML文件对应的超文本链接 - html.xpath(path/@href) 获取超链接信息
link_list = html_tree.xpath("//div[@class='sidebar']//a/@href")
print(link_list)
