import requests

headers ={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

p = {"wd":"传智播客"}

#url_temp = "https://www.baidu.com/?" #没有大括号
url_temp = "https://www.baidu.com/"  #说明？可有可无
r = requests.get(url_temp,headers=headers,params=p)
print(r.status_code)
print(r.request.url) #打印请求的url地址
