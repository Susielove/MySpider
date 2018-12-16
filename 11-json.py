import requests
import json
from pprint import pprint
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288"

response = requests.get(url,headers=headers)

html_str = response.content.decode()
print(response.status_code)
print(html_str)

ret = json.loads(html_str)
pprint(ret)
with open("douban.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=2))