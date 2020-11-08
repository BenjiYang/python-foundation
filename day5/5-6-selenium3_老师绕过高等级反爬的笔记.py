# https://note.youdao.com/ynoteshare1/index.html?id=aa30432f695e257873c7250fcd79a081&type=note
# 使用Chrome的调试模式和Selenium绕过高等级反爬

import os
import subprocess
from selenium import webdriver

# 定位到当前文件的父目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Windows平台下
# 用命令打开Chrome浏览器
# 先将程序的执行目录切换到Chrome的安装目录
# os.chdir("C:\\Program Files (x86)\\Google\\Chrome\\Application")
# 用os.system执行命令会阻塞程序，导致后续代码无法执行，故使用Popen代替
# os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"')
# 利用命令行打开Chrome浏览器
# subprocess.Popen('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# macOS平台下：/Applications/Google Chrome.app/Contents
# os.chdir("/Applications/Google Chrome.app/Contents/MacOS")
ret = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                       "--remote-debugging-port=9222"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(ret)
# ret1 = subprocess.Popen("/Applications/Google Chrome.app/Contents/MacOS Google Chrome --auto-open-devtools-for-tabs")
# subprocess.Popen("""/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --auto-open-devtools-for-tabs""", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 将程序空间切换到当前文件的父目录
os.chdir(BASE_DIR)


# 利用Selenium接管Chrome
option = webdriver.ChromeOptions()
# 这里配置的IP和端口，是前面执行命令的时候指定的
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# Windows平台下
# driver = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver.exe'), chrome_options=option)
# macOS平台下
driver = webdriver.Chrome('./chromedriver', options=option)
print("..."*20)

driver.get("http://www.baidu.com")
