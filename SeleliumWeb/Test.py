from selenium import webdriver
import time
from selenium.webdriver.common.keys import *

driver = webdriver.Firefox()
#进入主页面
driver.get('http://www.sunagy.com:9999/Sa/Index/login.html')
driver.find_element_by_id('email').send_keys("eric@sunagy.com")
driver.find_element_by_id('password').send_keys("111111")
driver.find_element_by_id('login').click()
driver.implicitly_wait(10)

#进入组态
#/Sa/Index/indexDeviceUrl.html
startTime=time.time()
driver.find_element_by_css_selector("div.sy_xiaolanmu > a.noadd").click()


driver.implicitly_wait(30)
driver.switch_to_window(driver.window_handles[1])
jumpTime_s=time.time()

isNext=False
while not isNext:
    driver.implicitly_wait(3000)
    #print("current_url",driver.current_url)
    if str(driver.current_url)!="about:blank":
        isNext=True

jumpTime_e=time.time()
jumpUrl=driver.current_url
isNext=False
print("经过",jumpTime_e-jumpTime_s,"秒跳转至：",driver.current_url)
'''
drawTime_s=time.time()
while not isNext:
    driver.implicitly_wait(3000)
    #print("current_url",driver.current_url)
    if str(driver.current_url)!=jumpUrl:
        isNext=True
drawTime_e=time.time()
print("经过",drawTime_e-drawTime_s,"秒跳转至：",driver.current_url)
'''

endTime=time.time()
userTime=endTime-startTime

print("总耗时：",userTime,"秒");

#driver.quit()
#driver.close()