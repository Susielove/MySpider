import re
# from parse_url import parse_url

# url = "http://36kr.com/"
# html_str = parse_url(url)

import requests
import json
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
url = "http://36kr.com/"

response = requests.get(url,headers=headers)

html_str = response.content.decode()
ret = re.findall("<script>var props=(.*?),locationnal=", html_str)[0]
with open("36kr.json","w",encoding="utf-8")as f:   #解决json在某一列报错的问题，先写到本地，再具体看
    f.write(ret)
ret = json.loads(ret)
print(ret)
