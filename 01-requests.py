import requests

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

url_temp = "http://www.baidu.com/?wd={}".format("传智播客") #字符串格式化方法

r = requests.get(url_temp,headers=headers)

print(r.status_code)

print(r.request.url)