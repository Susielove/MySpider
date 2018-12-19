import requests
import re
import json

class Neihan:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
        self.next_url_temp = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"
        self.start_url = "http://neihanshequ.com/"

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self, html_str): #这是从html字符串中提取
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>", html_str, re.S)  # 用.*?来代替<p>前面的换行符等
        max_time = re.findall("max_time:'(.*?)',", html_str)[0]
        return content_list, max_time

    def save_content_list(self, content_list):
        with open("neihan.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def get_content_list(self,json_str): #提取从第二页开始的json中的数据
        dict_ret = json.loads(json_str)
        data = dict_ret["data"]["data"]
        content_list = [i["group"]["content"] for i in data]
        max_time = dict_ret["data"]["max_time"]
        has_more = dict_ret["data"]["has_more"]
        return content_list,max_time,has_more

    def run(self):  # 实现主要逻辑
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.parse_url(self.start_url)
        # 3.提取数据
        content_list, max_time = self.get_first_page_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)
        # 5.构造下一页的url地址
        has_more = True #有第二页
        while has_more:
            next_url = self.next_url_temp.format(max_time)
            # 6.发送请求，获取响应
            json_str = self.parse_url(next_url)
            # 7.提取数据，提取max_time
            content_list,max_time,has_more = self.get_content_list(json_str)
            # 8.保存
            self.save_content_list(content_list)
            # 9.循环5-8步


if __name__ == '__main__':
    nei = Neihan()
    nei.run()
