import requests

response = requests.get("https://www.sina.com.cn/")

a = response.text

b = response.content.decode()

print(a)
print("*******------------------************************")
print(b)