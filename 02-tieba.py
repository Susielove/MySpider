import requests

class TiebaSpider:

	def __init__(self,tieba_name):
		self.tieba_name = tieba_name  #后面用到了才加上去的
		self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
		self.headers ={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

	def get_url_list(self):  #1.构造url列表
		#url_list = []   
		#for i in range (100): 
			#url_list.append(self.url_temp.format(i*50))
		#return url_list         
		#主张用列表推导式的方式写 （扁平胜于嵌套）
		return [self.url_temp.format(i*50) for i in range(10)]

   
	def parse_url(self,url): #发送请求，获取响应
		print(url)
		response = requests.get(url,headers=self.headers)
		return response.content.decode()  #返回响应的html字符串

	def save_html(self,html_str,page_num):  #保存html字符串
		file_path = "{}——第{}页.html".format(self.tieba_name,page_num)
		with open(file_path,"w",encoding ="utf-8") as f: #保存格式为"李毅——第一页.html"
			f.write(html_str)


	def run(self):  #实现主要逻辑
    	#1.构造url列表
		url_list = self.get_url_list()
    	#2.遍历url_list，发送请求，获取响应
		for url in url_list:
			html_str = self.parse_url(url)      
    	#3.保存
			page_num = url_list.index(url)+1 #页码数
			self.save_html(html_str,page_num)

if __name__=='__main__':
	tieba_spider = TiebaSpider("李毅")
	tieba_spider.run()