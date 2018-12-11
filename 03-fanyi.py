import requests

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
data = {
	
	"from":"en",
	"to":"zh",
	"query":"hi",
	"transtype":"translang",
	"simple_means_flag":"3",
	"sign":"742533.1030068",
	"token":"585e096e76f17f43b0a6d3b4defad0dd"
}

post_url = "https://fanyi.baidu.com/v2transapi"

response = requests.post(post_url,data = data,headers = headers)

status = response.status_code

content = response.content.decode()
print(status)
print(content)
