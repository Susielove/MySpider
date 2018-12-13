import requests

session = requests.session()

post_url = "http://www.renren.com/PLogin.do"

post_data = {"email":"13862332046","password":"shuji520WSX"}

headers =  {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

#使用session发送post请求，cookie保存在其中
session.post(post_url,data = post_data,headers=headers)
#再使用session进行请求登录之后才能访问的地址

r=session.get("http://www.renren.com/969029780",headers = headers)
#保存页面
file_path ="{}.html".format("人人网登录1")
with open(file_path,"w",encoding = "utf-8") as f:
	f.write(r.content.decode())

print(r.status_code)



