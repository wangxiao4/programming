#假设有一个以点a（0,0）为圆心，半径为50的圆，通过蒙特卡洛模拟计算圆的面积
import random
import math
count=0
inCircleCount=0
maxCount=10000
while count<maxCount:
    x,y=random.randint(-50,50),random.randint(-50,50)
    #判断到圆心的距离是否小于等于半径
    if (x**2+y**2)**0.5<=50:
        inCircleCount+=1
    count+=1

#求得命中圆的概率,也就是圆与外接矩形的面积比
prob=inCircleCount/maxCount
#求得外接矩形的面积
area_range=100**2
#所以圆的面积为
area_circle=area_range*prob
print("半径为50的圆的面积大约为：",area_circle)
