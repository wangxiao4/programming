from selenium import webdriver
import time
from selenium.webdriver.common.keys import *

class Selelium:
    def __init__(self):
        self.selectList_industry = ["保险业", "采矿", "能源", "餐饮", "宾馆", "电讯业", "房地产", "服务", "服装业", "公益组织", "广告业", "航空航天", "化学",
                               "健康", "保健", "建筑业", "教育", "培训", "计算机", "金属冶炼", "警察", "消防", "军人", "会计", "美容", "媒体", "出版",
                               "木材", "造纸", "零售", "批发", "农业", "旅游业", "司法", "律师", "司机", "体育运动", "学术研究", "演艺", "医疗服务",
                               "艺术", "设计", "银行", "金融", "因特网", "音乐舞蹈", "邮政快递", "运输业", "政府机关", "机械制造", "咨询"]
        self.selectKeyword = "能耗统计分析效果报表"
        self.selectIndex = 0

        for i in range(len(self.selectList_industry)):
            print("---------------------", self.selectList_industry[i], "----------------------")
            self.selectKeywordByHtml()
            self.selectIndex += 1

    def selectKeywordByHtml(self):
        driver = webdriver.Firefox()
        driver.get('http://www.baidu.com/')
        driver.implicitly_wait(10)
        driver.find_element_by_id("kw").send_keys(self.selectList_industry[self.selectIndex] + self.selectKeyword)
        driver.find_element_by_id("su").click()
        driver.implicitly_wait(10)
        # print(driver.find_element_by_css_selector("#10 > h3.t > a >em").text)
        idIndex = 1
        for i in range(10):
            strID = str(idIndex + i)
            for i in driver.find_elements_by_css_selector("div.result.c-container[id=\"" + strID + "\"] > h3.t > a > em"):
                print(i.text, end=",")
            try:
                print("\t\t",driver.find_element_by_css_selector("div.result.c-container[id=\"" + strID + "\"] > h3.t > a").get_attribute('href'))
            except:
                print("\t\t路径异常")
            print()

        #driver.quit()
        driver.close()

Selelium()

'''
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
'''

endTime=time.time()
userTime=endTime-startTime

print("总耗时：",userTime,"秒");
'''
