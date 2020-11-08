### requests - 第三方库
# pip3 install requests
# requests的底层就是urllib

'''
response.text: 返回值是str -- 慎用，因为自动转码正确率不够，建议使用content，然后手动转码
response.content: 返回值是byte，可以调用decode方法转成str
response.status_code - 返回状态码
response.headers - 相应header 头
response.request.headers - 请求header 头
'''

import requests

resp = requests.get("https://www.baidu.com")
print(resp.status_code)
print(resp.headers)
print(resp.request.headers)
