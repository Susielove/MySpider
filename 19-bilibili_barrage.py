import requests
from lxml import  etree
import re
class BiliBarrage: #18-08-01
    def __init__(self,url):
        self.url = url
        self.barrage_url = 'https://comment.bilibili.com/{}.xml'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_html(self,url): #发送请求，获取响应
        return requests.get(url,headers = self.headers).content.decode()

    def save_barrage(self,l,num):#保存弹幕
        print('保存')
        with open('danmu{}.txt'.format(num),'a') as f:
            for danmu_str in l:
                print(danmu_str)
                f.write(danmu_str)
                f.write("\n")
    def get_xml(self,li):
        print(li)
        for num in li: #遍历cid，设置弹幕请求url
            #拼接弹幕url，调用函数，发送请求，获取结果
            danmu_xml = self.get_html(self.barrage_url.format(num)).encode()
            #将获取到的xml类型转换为etrees对象
            xml_etr_obj = etree.HTML(danmu_xml)
            #获取弹幕列表
            l = xml_etr_obj.xpath('//d/text()')
            print("保存成功")
            self.save_barrage(l,num) #保存

    def run(self): #实现主要逻辑
        #发送请求，获取结果
        bl_html = self.get_html(self.url)
        print("正则获取cid")
        #提取此套的所有网页url地址和cid
        li = re.findall(r"<option value='.*?' cid='(\d+)'>",bl_html)
        if len(li)==0:#如果只有一个视频，上边这个列表为空，获取单个cid
            li = re.findall(r"EmbedPlayer\('player',.*?cid=(\d+)&aid",bl_html)
        #请求xml的url并保存弹幕
        self.get_xml(li)

if __name__ == '__main__':
    url = "https://www.bilibili.com/video/av18198653/"
    bilispider = BiliBarrage(url)
    bilispider.run()