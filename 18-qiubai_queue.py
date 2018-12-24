import requests
from lxml import etree
import json
import threading
from queue import Queue


class QiuBaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/imgrank/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.part_url = "https:"
        self.url_queue = Queue()  # url地址队列
        self.html_queue = Queue()  # 响应队列
        self.content_queue = Queue() #内容队列

    def get_url_list(self):
        # return [self.url_temp.format(i) for i in range(1, 14)]
        for i in range(1, 4):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            # return response.content.decode()
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done() #使用task_done才会减一

    def get_content_list(self):  # 提取数据
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")  # 按照div分组
            content_list = []
            for div in div_list:
                item = {}
                item["content"] = div.xpath(".//div[@class = 'content']/span/text()")
                item["content"] = [i.replace("\n", "") for i in item["content"]]  # 将\n替换成空字符即可
                item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
                item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(
                    item["author_gender"]) > 0 else None  # 按照空格切割，取后面的值,将Icon用空字符串代替，则只剩下了后面的值
                item["author_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
                item["author_age"] = item["author_age"][0] if len(item["author_age"]) > 0 else None
                item["content_img"] = div.xpath(".//div[@class = 'thumb']//img/@src")  # 获取内容中的图片
                item["content_img"] = self.part_url + item["content_img"][0] if len(item["content_img"]) > 0 else None
                item["author_img"] = div.xpath(".//div[@class = 'author clearfix']//img/@src")
                item["author_img"] = self.part_url + item["author_img"][0] if len(item["author_img"]) > 0 else None
                item["stats_vote"] = div.xpath(".//span[@class = 'stats-vote']/i/text()")
                item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
                content_list.append(item)
            # return content_list
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            for i in content_list:
                print(i)
            self.content_queue.task_done()

    def run(self):  # 实现主要逻辑
        thread_list = []
        # 1.url_list ---因为一共只有13页，所有构造一个列表
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2.遍历，发送请求，获取响应
        for i in range(20):  #使用多个线程来做，提高效率
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        t_content = threading.Thread(target=self.get_content_list)
        thread_list.append(t_content)
        # 4.保存
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True) #把子线程设置为守护线程，改线程不重要，主线程结束，子线程结束
            t.start()  #启动线程
        print("主线程结束")
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join() #让主线程阻塞，等待队列的任务完成之后再完成

if __name__ == '__main__':
    qiubai = QiuBaiSpider()
    qiubai.run()
