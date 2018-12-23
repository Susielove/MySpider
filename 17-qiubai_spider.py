import requests
from lxml import etree
import json


class QiuBaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/imgrank/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.part_url = "https:"

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):  # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")  # 按照div分组
        content_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//div[@class = 'content']/span/text()")
            item["content"] = [i.replace("\n","") for i in item["content"]] #将\n替换成空字符即可
            item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(
                item["author_gender"]) > 0 else None  # 按照空格切割，取后面的值,将Icon用空字符串代替，则只剩下了后面的值
            item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None
            item["content_img"] = div.xpath(".//div[@class = 'thumb']//img/@src") #获取内容中的图片
            item["content_img"] = self.part_url+item["content_img"][0] if len(item["content_img"]) > 0 else None
            item["author_img"] = div.xpath(".//div[@class = 'author clearfix']//img/@src")
            item["author_img"] = self.part_url+item["author_img"][0] if len(item["author_img"])>0 else None
            item["stats_vote"] = div.xpath(".//span[@class = 'stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self,content_list):
        file_path = "糗事百科.txt"
        with open(file_path,"a",encoding="utf-8")as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
        print("保存成功")


    def run(self):  # 实现主要逻辑
        # 1.url_list ---因为一共只有13页，所有构造一个列表
        url_list = self.get_url_list()
        # 2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
        # 3.提取数据
            content_list = self.get_content_list(html_str)
        # 4.保存
            self.save_content_list(content_list)



if __name__ == '__main__':
    qiubai = QiuBaiSpider()
    qiubai.run()
