# 练习： 将以上31篇名人名言内容（包含标题）保存到本地的‘mrmy.txt'文件中
import requests
from lxml.etree import HTML


BASE_URL = "http://www.geyanw.com"


def get_content_by_xpath(url, xpath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    resp = requests.get(url, headers=headers)
    html_tree = HTML(resp.content)
    content = html_tree.xpath(xpath)
    return content


title_list = get_content_by_xpath(
    BASE_URL, "//div[@class='sidebar']//a/text()")
link_list = get_content_by_xpath(BASE_URL, "//div[@class='sidebar']//a/@href")
print("==================================================== link_list ======================================================== \n %s" % link_list)


with open("lxml2_爬名人名言文本.txt", "w+", encoding='utf-8') as f:
    for index, link in enumerate(link_list):
        sub_full_url = BASE_URL + link
        print(sub_full_url)
        sub_content = get_content_by_xpath(
            sub_full_url, "//div[@id='p_left']//div[@class='content']/div/span/text()")
        sub_content = [sub_content+"\n" for sub_content in sub_content]
        print(sub_content)
        print("============================================================================================================")

        f.write(title_list[index] + "\n")
        f.writelines(sub_content)
        f.write("\n\n")
