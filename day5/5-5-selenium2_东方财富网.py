from selenium import webdriver
import time


option = webdriver.ChromeOptions()

driver = webdriver.Chrome("./chromedriver", options=option)
driver.get("http://quote.eastmoney.com/center/gridlist.html#hs_a_board")

time.sleep(3)

stock_name_list = driver.find_elements_by_xpath(
    "//table[@id='table_wrapper-table']/tbody/tr/td[3]/a")
stock_incr_list = driver.find_elements_by_xpath(
    "//table[@id='table_wrapper-table']/tbody/tr/td[6]/span")


stock_name_list = [name.text for name in stock_name_list]
stock_incr_list = [incr.text for incr in stock_incr_list]
print(stock_name_list)
print(stock_incr_list)


driver.close()
