import requests
from retrying import retry

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}

@retry(stop_max_attempt_number = 3) #下面的方法最大可以报错3次
def _parse_url(url,method,data,proxies):
    print("*"*20)  #显示出到底执行了几次
    if method =="POST":
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
    else :
        response = requests.get(url, headers=headers, timeout=3,proxies=proxies)
    assert response.status_code == 200  # 判断请求是否成功
    return response.content.decode()


def parse_url(url,method="GET",data = None,proxies={}):
    try:
        html = _parse_url(url,method,data,proxies)
    except:
        html = None
    return html


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url))

