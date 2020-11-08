''' selenium API for Python
访问指定网页：driver.get(target_url)
通过xpath获取页面的单个元素：driver.find_element_by_xpath(xpath_expression)
通过xpath获取页面的多个元素：driver.find_elements_by_xpath(xpath_expression)
获取元素的文本内容：driver.find_element_by_xpath(xpath_expression).text
点击页面元素：driver.find_element_by_xpath(xpath_expression).click()
往输入框输入内容：driver.find_element_by_xpath(xpath_expression).send_keys(input_text)
获取元素中的属性：driver.find_element_by_xpath(xpath_expression).get_attribute('href')
获取当前页面的URL：driver.current_url
关闭网页：driver.quit()
滚动鼠标到网页底部：driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
'''

from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("./chromedriver", options=option)

driver.get("https://www.baidu.com")

time.sleep(3)
driver.find_element_by_xpath("//input[@id='kw']").send_keys("Python")
driver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(3)

hot_ele_list = driver.find_elements_by_xpath(
    '//div[@title="百度热榜"]/../table//tr/td/a')

for hot_new in hot_ele_list:
    print(hot_new.text)

time.sleep(3)
driver.close()
