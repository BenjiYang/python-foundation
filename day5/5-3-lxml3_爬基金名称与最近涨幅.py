# 练习5: 给定基金网址: https://fund.eastmoney.com/004854.html
# 从网页中提取字段：1）基金名称；2）基金最近一次的涨跌幅度；3）基金最近三个月的涨跌幅度
import requests
from lxml.etree import HTML
# http://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1
# //*[@id="oTable"]/tbody/tr/td[@class="tol"]//a/@title


BASE_URL = "http://fund.eastmoney.com/004854.html"

# 基金名称：//div[@class="fundDetail-tit"]/div/text()
# 基金最近一次涨跌幅度： //div[@class='dataOfFund']/dl[2]/dd[@class='dataNums']/span[2]/text()
# 基金最近三个月的涨跌幅度： //div[@class='dataOfFund']/dl[2]/dd[2]/span[2]/text()


def get_content_by_xpath(url, xpath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    resp = requests.get(url, headers=headers)
    html_tree = HTML(resp.content)
    content = html_tree.xpath(xpath)
    return content


BASE_URL = "http://fund.eastmoney.com/"


with open('lxml3_爬基金涨跌.txt', 'w+', encoding='utf-8') as f:
    for i in range(10):
        import time
        time.sleep(1)
        url = BASE_URL + "%06d" % i + ".html"
        title = get_content_by_xpath(
            url, "//div[@class='fundDetail-tit']/div/text()")

        incr_lastday = get_content_by_xpath(
            url, "//div[@class='dataOfFund']/dl[2]/dd[@class='dataNums']/span[2]/text()")

        incr_last3Months = get_content_by_xpath(
            url, "//div[@class='dataOfFund']/dl[2]/dd[2]/span[2]/text()")

        # if-过滤掉空值
        if title and incr_lastday and incr_last3Months:
            print("基金ID：%s； 最近一天涨跌：%s； 最近3个月涨跌：%s； 基金名称：%s；" %
                  ("%06d" % i, incr_lastday[0], incr_last3Months[0], title[0]))
            f.write("基金ID：%s； 最近一天涨跌：%s； 最近3个月涨跌：%s； 基金名称：%s；" %
                    ("%06d" % i, incr_lastday[0], incr_last3Months[0], title[0]))
            f.write("\n")
