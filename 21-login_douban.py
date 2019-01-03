from selenium import webdriver
import time
#实例化driver
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

driver.find_element_by_id("form_email").send_keys("794378411@qq.com")
driver.find_element_by_id("form_password").send_keys("shuji520")

time.sleep(5)
driver.find_element_by_class_name("bn-submit").click()

#获取cookie
cookies = { i["name"]:i["value"] for i in driver.get_cookies()}
print(cookies)
time.sleep(3)
driver.quit()
