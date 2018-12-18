import requests

import requests
import json


class DoubanSpider:
    def __init__(self):
        # self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?&start={}&count=18&loc_id=108288"
        # 获取多个分类下的电视剧信息，构造一个url的列表
        self.url_temp_list = [
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?&start={}&count=18&loc_id=108288",
                "country": "US"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?&start={}&count=18&loc_id=108288",
                "country": "UK"
            }, {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?&start={}&count=18&loc_id=108288",
                "country": "CN"
            }

        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url):  # 2.发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):  # 3.提取数据
        dict_ret = json.loads(json_str)  # 将json字符串转化为字典
        content_list = dict_ret["subject_collection"]  # 取subject_collection里面的值，得到一个列表
        total = dict_ret["total"]
        return content_list, total

    def save_content_list(self, content_list,country):  # 4.保存
        with open("douban.txt", "a", encoding="utf-8") as f:  # 使用a的方式追加数据
            for content in content_list:
                content["country"] = country
                f.write(json.dumps(content, ensure_ascii=False))  # 转换成字符串写入,中文显示中文
                f.write("\n")  # 写入换行符，一行输入一条数据
        print("保存成功")

    def run(self):
        # 1.start_url
        for url_temp in self.url_temp_list:
            num = 0
            total = 100  # 假设有第一页
            while num < total + 18:  # 跳出循环方法二：总保存条目小于总条目数量
                url = url_temp["url_temp"].format(num)
                # 2.发送请求，获取响应
                json_str = self.parse_url(url)
                # 3.提取数据
                content_list, total = self.get_content_list(json_str)
                # 4.保存
                self.save_content_list(content_list,url_temp["country"])
                # 5.构造下一页的url地址，进入循环
                # if len(content_list)<18:  #跳出循环方法一：某一页的条目小于18
                #     break
                num += 18


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
