from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS() #发送JS

# 改变截屏图片太小——方法一：设置窗口大小
driver.set_window_size(1920,1080)

# 方法二：最大化窗口
driver.maximize_window()

# 发送请求
driver.get("http://www.baidu.com")
#进行页面截屏
driver.save_screenshot("./baidu.png")

#元素定位的方法
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

print(driver.current_url) #click之后的url地址
#driver 获取html字符串
print(driver.page_source) #浏览器中element的内容

#driver获取cookie
cookies = driver.get_cookies()
print(cookies)
print("*"*100)
cookies = {i["name"]:i["value"] for i in cookies}
print(cookies)


# 退出浏览器
time.sleep(3)
driver.quit()
