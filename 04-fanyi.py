import requests
import json
import sys

query_string = sys.argv[1]  #在终端下利用百度的接口完成翻译的工作

post_url = "https://fanyi.baidu.com/basetrans"
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

post_data = {          #之后再重新爬一下
	"from":"zh",
	"to":"en",
	#"query":"生活苦短，我用Python."
	"query":query_string}

response = requests.post(post_url,data =post_data ,headers = headers)

dic_res = json.loads(response.content.decode())
print(dic_res)
result = dic_res["trans"][0]["dst"]
print(result)



