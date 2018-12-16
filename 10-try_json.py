import json

from parse_url import parse_url
from pprint import pprint

url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288"
# url = "https://www.baidu.com"
str = parse_url(url)

# 使用json.loads把json字符串转化为python类型
ret = json.loads(str)
# pprint(ret1)
# print(type(ret1))

# json.dumps能够把python类型转化为json字符串,写入的时候必须要是字符串
with open("douban.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=2))  # 显示中文格式，换行并且空两格
with open("douban.json", "r") as f:
    ret2 = f.read()
    ret3 = json.loads(ret2)
    print(ret3)
    print(type(ret3))

#使用json.load提取类对象中的数据
with open("douban.json","r",encoding = "utf-8") as f:
    ret4 = json.load(f)
    print(ret4)
    print(type(ret4))
#使用json.dump能够把python类型放入类文件对象中
with open("douban.json","w",encoding = "utf-8") as f:
   json.dump(ret4,f,ensure_ascii=False,indent=2)